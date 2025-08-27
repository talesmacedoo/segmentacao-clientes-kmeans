import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from datetime import datetime

class TratamentoDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.dataframe = None
        self.scaler = None

    def _to_float(self, s):
        # aceita "1,23" ou "1.23"
        return pd.to_numeric(
            pd.Series(s).astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False),
            errors='coerce'
        )

    def carregar_dados(self):
        df = pd.read_csv(self.caminho_arquivo, sep=';')
        df.columns = df.columns.str.strip().str.lower()

        # renomeações convenientes
        rename_map = {
            'total de emprestimos': 'total_de_emprestimos',
            'data ultimo emprestimo': 'data_ultimo_emprestimo',
            'data primeiro emprestimo': 'data_primeiro_emprestimo',
            'recência': 'recencia',  # caso venha acentuado
        }
        df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

        # tipagens
        if 'data_ultimo_emprestimo' in df.columns:
            df['data_ultimo_emprestimo'] = pd.to_datetime(df['data_ultimo_emprestimo'], dayfirst=True, errors='coerce')

        if 'frequencia' in df.columns:
            df['frequencia'] = self._to_float(df['frequencia'])

        # RECENCIA: se vier pronto (coluna 'recencia' ou 'recencia_exata'), usa; senão calcula pela data_ultimo_emprestimo
        if 'recencia_exata' in df.columns:
            df['recencia_exata'] = self._to_float(df['recencia_exata'])
        elif 'recencia' in df.columns:
            df['recencia_exata'] = self._to_float(df['recencia'])
        elif 'data_ultimo_emprestimo' in df.columns:
            hoje = datetime.now()
            df['recencia_exata'] = (hoje - df['data_ultimo_emprestimo']).dt.days / 365.25
        else:
            raise ValueError("Informe 'recencia'/'recencia_exata' ou 'data_ultimo_emprestimo' para que eu derive a recência.")

        # mantemos apenas o que precisamos e removemos nulos
        cols_need = ['frequencia', 'recencia_exata']
        faltando = [c for c in cols_need if c not in df.columns]
        if faltando:
            raise ValueError(f"Colunas faltando no CSV: {faltando}")

        df = df.dropna(subset=cols_need).reset_index(drop=True)

        self.dataframe = df
        return self.dataframe

    def escalar_dados(self, colunas=['frequencia', 'recencia_exata']):
        self.scaler = StandardScaler()
        self.dataframe[colunas] = self.scaler.fit_transform(self.dataframe[colunas])
        return self.dataframe

    def inverter_escalonamento(self, dados):
        if self.scaler is None:
            raise ValueError("Rode escalar_dados antes de inverter.")
        return self.scaler.inverse_transform(dados)
