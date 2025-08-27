from sklearn.cluster import KMeans
import numpy as np

class Clustering:
    def __init__(self, df):
        self.df = df
        self.X = None
        self.kmeans = None
        self.labels = None

    def preparar_dados(self):
        self.X = self.df[['frequencia', 'recencia_exata']].values

    def metodo_cotovelo(self, max_k=10):
        sse = []
        for k in range(1, max_k + 1):
            km = KMeans(n_clusters=k, random_state=42, n_init='auto')
            km.fit(self.X)
            sse.append(km.inertia_)
        return sse

    def rodar_kmeans(self, n_clusters=5):
        self.kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init='auto')
        self.kmeans.fit(self.X)
        self.labels = self.kmeans.labels_
        return self.kmeans.cluster_centers_
