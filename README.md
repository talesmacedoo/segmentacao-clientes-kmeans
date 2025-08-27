# 📊 Segmentação de Clientes com KMeans

Este projeto tem como objetivo **segmentar clientes** com base em seu **histórico de empréstimos**, utilizando o algoritmo **KMeans**.  
A partir dos dados de **frequência de empréstimos** e **recência** (tempo desde o último empréstimo), o sistema agrupa os clientes em **clusters** para apoiar **campanhas comerciais** e **estratégias de retenção**.

---

## 🚀 Funcionalidades

- Leitura de dados de clientes a partir de um arquivo CSV.
- Cálculo automático de **recência** (quando não fornecida).
- Padronização dos dados com **normalização**.
- Segmentação dos clientes via **KMeans**.
- Visualização gráfica dos clusters com **legenda automática**.
- Geração de um **relatório CSV único** com:
  - CPF do cliente
  - Total de empréstimos
  - Frequência de empréstimos
  - Data do último empréstimo
  - Recência (anos desde o último empréstimo)
  - Cluster atribuído

---

## 🛠 Tecnologias utilizadas

- **Python 3.10+**
- **Pandas** → Manipulação de dados
- **Scikit-learn** → KMeans e normalização
- **Matplotlib** → Visualização de gráficos
- **NumPy** → Cálculos numéricos

---

## 📂 Estrutura do projeto

```
segmentacao-clientes-kmeans/
├── data/
│   └── GovBA_Novos_Contagem.csv      # Arquivo de entrada com os dados
├── src/
│   ├── tratamento_dados.py          # Carrega e prepara os dados
│   ├── clustering.py                # Implementa o KMeans
│   ├── graficos.py                  # Plota clusters e cotovelo
│   ├── resultado.py                 # Gera estatísticas e salva CSV
├── resultado_clusters.csv           # Saída final (gerado automaticamente)
├── main.py                         # Arquivo principal para executar o projeto
└── README.md                       # Documentação do projeto
```

---

## ⚙️ Como configurar o ambiente

### **1️⃣ Criar ambiente virtual e ativar**

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar no Windows
venv\Scripts\activate

# Ativar no Linux/Mac
source venv/bin/activate
```

### **2️⃣ Instalar dependências**

```bash
pip install -r requirements.txt
```

> Caso não tenha o arquivo `requirements.txt`, instale manualmente:

```bash
pip install pandas scikit-learn matplotlib numpy
```

---

## ▶️ Como executar o projeto

```bash
python main.py
```

---

## 🔄 Fluxo do `main.py`

1. Carrega os dados do CSV.
2. Normaliza e prepara os dados.
3. Aplica o **KMeans** para segmentar os clientes.
4. Mostra o **método do cotovelo** para avaliar o número de clusters ideal.
5. Plota os **clusters com cores, legendas e centróides**.
6. Gera o arquivo **resultado_clusters.csv** com todos os clientes e seus respectivos clusters.

---

## 📈 Como interpretar os resultados

### **Gráfico do Cotovelo**
- Ajuda a escolher o **número ideal de clusters**.

### **Gráfico de Clusters**
- **Eixo X** → Recência (anos desde o último empréstimo)
- **Eixo Y** → Frequência (número médio de empréstimos por ano)
- **Cores** → Cada cluster tem uma cor única
- **X Preto** → Representa o centróide do cluster

### **CSV de Saída**
Contém todos os clientes, o cluster e as principais métricas.

| CPF         | Total Empréstimos | Último Empréstimo | Recência (anos) | Frequência | Cluster |
|------------|--------------------|--------------------|------------------|------------|---------|
| 99997240510 | 10 | 24/07/2025 | 0,91 | 2,0 | 2 |
| 9995620510  | 21 | 24/02/2025 | 1,91 | 3,5 | 1 |
| 9994283553  | 5  | 19/08/2024 | 2,45 | 1,1 | 3 |

---

## 🔄 Ajustando o número de clusters

Para alterar o número de grupos, edite no `main.py`:

```python
centroids_scaled = cluster.rodar_kmeans(n_clusters=5)
```

Exemplo, para criar **3 clusters**:

```python
centroids_scaled = cluster.rodar_kmeans(n_clusters=3)
```

