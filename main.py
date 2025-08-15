import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from datetime import datetime


df = pd.read_csv('GovBA_Novos_Contagem.csv', sep=';')
df.columns = df.columns.str.strip().str.lower()


df['frequencia'] = df['frequencia'].astype(str).str.replace(',', '.').astype(float)


df['data_ultimo_emprestimo'] = pd.to_datetime(df['recencia'], dayfirst=True, errors='coerce')


hoje = datetime.now()
df['recencia_exata'] = (hoje - df['data_ultimo_emprestimo']).dt.days / 365.25


X = df[['frequencia', 'recencia_exata']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Método do cotovelo
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), sse, 'bo-')
plt.xlabel('Número de Clusters (k)')
plt.ylabel('Soma dos Erros Quadrados (SSE)')
plt.title('Método do Cotovelo')
plt.show()

# Clusterização com 4 clusters
kmeans = KMeans(n_clusters=5, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Centroides
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

# -------------------------
# 3. Visualização dos clusters
# -------------------------
plt.figure(figsize=(8,6))
plt.scatter(df['recencia_exata'], df['frequencia'], c=df['cluster'], cmap='viridis', s=40, alpha=0.7)
plt.scatter(centroids[:,1], centroids[:,0], marker='X', s=200, c='red', label='Centroides')
plt.xlabel('Recência (anos desde último empréstimo)')
plt.ylabel('Frequência')
plt.title('Segmentação de Clientes com KMeans')
plt.gca().invert_xaxis()
plt.legend()
plt.show()

# -------------------------
# 4. Estatísticas por cluster
# -------------------------
print("\n--- Estatísticas por cluster ---")
print(df.groupby('cluster').agg({
    'frequencia': ['mean', 'min', 'max'],
    'recencia_exata': ['mean', 'min', 'max'],
    'cpf': 'count'
}))

# -------------------------
# 5. Distribuição por faixas
# -------------------------
bins_freq = list(range(0, int(df['frequencia'].max()) + 2))
df['faixa_frequencia'] = pd.cut(df['frequencia'], bins=bins_freq, right=False)

bins_rec = [i/2 for i in range(0, int(df['recencia_exata'].max()*2 + 2))]
df['faixa_recencia'] = pd.cut(df['recencia_exata'], bins=bins_rec, right=False)

print("\n--- Distribuição por faixa de frequência ---")
print(df['faixa_frequencia'].value_counts().sort_index())

print("\n--- Distribuição por faixa de recência ---")
print(df['faixa_recencia'].value_counts().sort_index(ascending=False))
