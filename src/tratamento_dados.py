import pandas as pd
from sklearn.preprocessing import StandardScaler

class TratamentoDados:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def carregar_dados(self):
        pass

    def escalar_dados(self, colunas):
        """Aplica StandardScaler nas colunas indicadas"""
        pass

    def inverter_escalonamento(self, dados):
        """Retorna dados para escala original"""
        pass