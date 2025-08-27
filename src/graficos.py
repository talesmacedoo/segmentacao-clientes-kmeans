import matplotlib.pyplot as plt
import numpy as np

class Graficos:
    @staticmethod
    def plot_cotovelo(sse):
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(sse)+1), sse, 'bo-')
        plt.xlabel('Número de Clusters (k)')
        plt.ylabel('Soma dos Erros Quadrados (SSE)')
        plt.title('Método do Cotovelo')
        plt.show()

    @staticmethod
    def plot_clusters(df, centroids):
        """
        Plota os clusters com legenda automática e centróides identificados.
        """
        plt.figure(figsize=(10, 7))

        unique_clusters = sorted(df['cluster'].unique())
        colors = plt.cm.get_cmap("tab10", len(unique_clusters))


        for cluster_id in unique_clusters:
            cluster_data = df[df['cluster'] == cluster_id]
            plt.scatter(
                cluster_data['recencia_exata'],
                cluster_data['frequencia'],
                s=40,
                c=[colors(cluster_id)],
                alpha=0.7,
                label=f"Cluster {cluster_id} ({len(cluster_data)} clientes)"
            )


        plt.scatter(
            centroids[:, 1],  #Recência
            centroids[:, 0],  #Frequência
            marker='X',
            s=250,
            c='black',
            edgecolors='white',
            linewidths=1.5,
            label='Centróides'
        )

        for i, (x, y) in enumerate(zip(centroids[:, 1], centroids[:, 0])):
            plt.text(
                x, y,
                f"C{i}",
                fontsize=9,
                fontweight="bold",
                color="white",
                ha="center",
                va="center",
                bbox=dict(facecolor="black", alpha=0.7, boxstyle="round,pad=0.3")
            )


        plt.title("Segmentação de Clientes com KMeans", fontsize=15, fontweight="bold")
        plt.xlabel("Recência (anos desde último empréstimo)")
        plt.ylabel("Frequência (nº de empréstimos/ano)")

        plt.legend(title="Clusters", loc="best")

        plt.gca().invert_xaxis()

        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
