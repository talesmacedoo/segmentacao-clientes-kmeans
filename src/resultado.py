import pandas as pd

class Resultado:
    def __init__(self, df):
        self.dataframe = df.copy()
        self.df_export = None

    def estatisticas_por_cluster(self):
        """
        Exibe estatísticas agregadas por cluster.
        """
        stats = self.dataframe.groupby('cluster').agg({
            'frequencia': ['mean', 'min', 'max'],
            'recencia_exata': ['mean', 'min', 'max'],
            'cpf': 'count'
        }).sort_index()

        print("\n--- Estatísticas por cluster ---")
        print(stats)
        return stats

    def preparar_exportacao(self):
        """
        Cria o DataFrame final para exportação.
        """
        cols = ['cpf', 'total_de_emprestimos', 'data_ultimo_emprestimo',
                'recencia_exata', 'frequencia', 'cluster']


        self.df_export = self.dataframe[cols].copy()

        # Ordena por cluster e recência para facilitar análise
        self.df_export = self.df_export.sort_values(
            by=['cluster', 'recencia_exata', 'frequencia'],
            ascending=[True, True, False]
        ).reset_index(drop=True)

        return self.df_export

    def salvar_csv(self, caminho='resultado_clusters.csv'):
        """
        Salva um único CSV com todos os clientes e seus respectivos clusters.
        """
        if self.df_export is None:
            self.preparar_exportacao()

        self.df_export.to_csv(caminho, index=False)
        print(f"\n✅ Arquivo salvo em: {caminho}")
        return self.df_export
