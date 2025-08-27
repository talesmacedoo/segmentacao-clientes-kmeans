from src.tratamento_dados import TratamentoDados
from src.clustering import Clustering
from src.graficos import Graficos
from src.resultado import Resultado

#1 Ler (sem calcular freq/recência; você já fornece)
dados = TratamentoDados('data/GovBA_Novos_Contagem.csv')
df = dados.carregar_dados()

df_orig = df.copy(deep=True)

#2- Normalizar e clusterizar 
df_norm = dados.escalar_dados(['frequencia', 'recencia_exata'])

cluster = Clustering(df_norm)          
cluster.preparar_dados()
sse = cluster.metodo_cotovelo()
Graficos.plot_cotovelo(sse)

centroids_scaled = cluster.rodar_kmeans(n_clusters=5)


df_orig['cluster'] = cluster.labels


centroids = dados.inverter_escalonamento(centroids_scaled)

Graficos.plot_clusters(df_orig, centroids)

# 3) Resultados
res = Resultado(df_orig)
res.salvar_csv()
