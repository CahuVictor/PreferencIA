# 📄 EXPLICACAO_PROJETO.md — Sistema de Recomendação com SVD usando a Biblioteca Surprise

## 📘 Sobre o Projeto

Este projeto implementa um **sistema de recomendação de livros** utilizando o algoritmo **SVD (Singular Value Decomposition)** da biblioteca `surprise`. Os dados utilizados são do **GoodBooks-10k**, um conjunto de dados contendo mais de 6 milhões de avaliações feitas por usuários para 10 mil livros.

## 🚀 Objetivo

Criar um sistema que:

- **Treina um modelo de recomendação** com base em avaliações reais de usuários.
- **Avalia a precisão** do modelo com métricas apropriadas (ex: RMSE).
- **Gera recomendações personalizadas** de livros para um determinado usuário com base no histórico de avaliações dele.

## 🛠️ Etapas detalhadas do código

### 📥 1. **Importação de bibliotecas**

```python
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy
```

- `pandas`: para ler e manipular os dados.
- `surprise`: biblioteca para recomendação colaborativa.
  - `SVD`: algoritmo de fatoração de matriz.
  - `Dataset` e `Reader`: para preparar os dados.
  - `train_test_split`: divide os dados.
  - `accuracy`: calcula métricas de erro como RMSE.

### 📂 2. **Carregamento dos dados**

```python
ratings = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
books = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")
```

- `ratings.csv`: contém colunas `user_id`, `book_id` e `rating`.
- `books.csv`: contém metadados dos livros (`title`, `authors`, etc.).

### 🧹 3. **Filtragem de usuários ativos**

```python
user_counts = ratings['user_id'].value_counts()
ratings = ratings[ratings['user_id'].isin(user_counts[user_counts >= 50].index)]
```

- Filtra apenas os usuários que avaliaram **50 ou mais livros**.
- Isso melhora a qualidade do modelo, pois usuários com poucas interações não fornecem informações suficientes.

### 📄 4. **Conversão para Dataset da biblioteca Surprise**

```python
reader = Reader(rating_scale=(0, 5))
data = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)
```

- `Reader`: define o intervalo de notas válidas (aqui de 0 a 5).
- `load_from_df`: converte o DataFrame em um dataset do `surprise`, pronto para treinamento.

### 🔀 5. **Divisão treino/teste**

```python
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
```

- Divide o dataset em:
  - **80% para treino** (`trainset`)
  - **20% para teste** (`testset`)
- O parâmetro `random_state` garante resultados reprodutíveis.

### 🧠 6. **Treinamento do modelo SVD**

```python
model = SVD()
model.fit(trainset)
```

- `SVD`: algoritmo de fatoração de matrizes.
- O modelo aprende **padrões de preferência dos usuários** com base em seus históricos de avaliações.

### 📊 7. **Avaliação da performance do modelo**

```python
predictions = model.test(testset)
accuracy.rmse(predictions)
```

- Testa o modelo com os dados de teste.
- `accuracy.rmse`: calcula o **erro quadrático médio** (quanto o modelo costuma errar na predição das notas).

### 🎯 8. **Função de recomendação personalizada**

```python
def recomendar_svd(user_id, n=5):
    livros_lidos = ratings[ratings['user_id'] == user_id]['book_id'].tolist()
    todos_livros = ratings['book_id'].unique()
    livros_nao_lidos = [livro for livro in todos_livros if livro not in livros_lidos]
    
    predicoes = [(livro, model.predict(user_id, livro).est) for livro in livros_nao_lidos]
    predicoes.sort(key=lambda x: x[1], reverse=True)

    print(f"\nRecomendações com SVD para usuário {user_id}:")
    for livro_id, score in predicoes[:n]:
        titulo = books[books['book_id'] == livro_id]['title'].values[0]
        print(f"- {titulo} (score: {score:.2f})")
```

**O que essa função faz:**

1. Coleta os livros que o usuário **já leu**.
2. Pega todos os outros livros do dataset.
3. Usa o modelo para **prever a nota estimada** que o usuário daria para cada livro não lido.
4. Ordena os livros por nota estimada (da maior para a menor).
5. Exibe os **top N livros recomendados**.

### ▶️ 9. **Exemplo de uso**

```python
recomendar_svd(user_id=1)
```

- Gera recomendações personalizadas para o usuário de ID `1`.

## 📌 Considerações finais

- Esse sistema é **colaborativo**, ou seja, as recomendações são baseadas nas **semelhanças entre usuários**.
- O `SVD` é um método eficiente e amplamente utilizado em sistemas como o da **Netflix, Amazon** etc.
- É possível integrar essa base a interfaces como **Streamlit, Flask ou FastAPI** para criar uma aplicação web.