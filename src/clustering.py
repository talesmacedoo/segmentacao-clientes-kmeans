from sklearn.cluster import KMeans

class AgrupamentoClientes():
    def __init__(self, num_clusters=3, random_state=42):
        self.num_clusters = num_clusters
        self.random_state = random_state

    def metodo_cotovelo(self, dados, max_k=10):
        """Retorna lista de inércias para diferentes k"""
        pass

    def treinar_prever(self, dados):
        """Treina o KMeans e retorna os clusters previstos"""
        pass

    def obter_centroides(self):
        """Retorna os centroides do modelo"""
        pass

