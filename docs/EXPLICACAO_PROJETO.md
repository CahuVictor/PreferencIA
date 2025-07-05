# 📘 Explicação Detalhada do Projeto de Recomendação com SVD

## 📘 Sobre o Projeto

Este documento fornece uma explicação detalhada sobre o funcionamento do projeto de sistema de recomendação de livros utilizando o algoritmo **SVD (Singular Value Decomposition)**, com base nos arquivos atualizados do diretório `src/pos`.
O projeto faz as seguintes tarefas:

- **Treina um modelo de recomendação** com base em avaliações reais de usuários.
- **Avalia a precisão** do modelo com métricas apropriadas (ex: RMSE).
- **Gera recomendações personalizadas** de livros para um determinado usuário com base no histórico de avaliações dele.

---

## 📁 Estrutura Geral dos Arquivos

* `dados.py`: Responsável por carregar e filtrar os dados.
* `modelo.py`: Contém a lógica de treinamento e avaliação do modelo SVD.
* `recomendador.py`: Gera as recomendações a partir do modelo treinado.
* `main.py`: Arquivo principal que orquestra a execução completa do projeto via linha de comando.

---

## 📄 `dados.py`

```python
import pandas as pd

def carregar_dados(caminho_ratings, caminho_books, min_avaliacoes=50):
    ratings = pd.read_csv(caminho_ratings)
    books = pd.read_csv(caminho_books)
    user_counts = ratings['user_id'].value_counts()
    ratings_filtrados = ratings[ratings['user_id'].isin(user_counts[user_counts >= min_avaliacoes].index)]
    return ratings_filtrados, books
```

- `pandas`: para ler e manipular os dados.
- `ratings.csv`: contém colunas `user_id`, `book_id` e `rating`.
- `books.csv`: contém metadados dos livros (`title`, `authors`, etc.).
- Filtra apenas os usuários que avaliaram **50 ou mais livros**.
- Isso melhora a qualidade do modelo, pois usuários com poucas interações não fornecem informações suficientes.

### O que faz:

* Lê dois conjuntos de dados CSV da internet: `ratings.csv` e `books.csv`.
* Filtra os usuários que avaliaram menos de 50 livros para manter apenas usuários ativos.

---

## 📄 `modelo.py`

```python
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy

def treinar_modelo(ratings):
    reader = Reader(rating_scale=(0, 5))
    data = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
    model = SVD()
    model.fit(trainset)
    return model, testset

def avaliar_modelo(model, testset):
    predictions = model.test(testset)
    rmse = accuracy.rmse(predictions)
    return rmse
```

- `surprise`: biblioteca para recomendação colaborativa.
  - `SVD`: algoritmo de fatoração de matriz.
  - `Dataset` e `Reader`: para preparar os dados.
  - `train_test_split`: divide os dados.
  - `accuracy`: calcula métricas de erro como RMSE.
- `Reader`: define o intervalo de notas válidas (aqui de 0 a 5).
- `load_from_df`: converte o DataFrame em um dataset do `surprise`, pronto para treinamento.
- Divide o dataset em:
  - **80% para treino** (`trainset`)
  - **20% para teste** (`testset`)
- O parâmetro `random_state` garante resultados reprodutíveis.
- `SVD`: algoritmo de fatoração de matrizes.
- O modelo aprende **padrões de preferência dos usuários** com base em seus históricos de avaliações.
- Testa o modelo com os dados de teste.
- `accuracy.rmse`: calcula o **erro quadrático médio** (quanto o modelo costuma errar na predição das notas).

### O que faz:

* Utiliza a lib `surprise` como biblioteca para recomendação colaborativa.
  * `SVD`: algoritmo de fatoração de matriz.
  * `Dataset` e `Reader`: para preparar os dados.
  * `train_test_split`: divide os dados.
  * `accuracy`: calcula métricas de erro como RMSE.
* Treina o modelo de recomendação com o algoritmo SVD usando a biblioteca `scikit-surprise`.
* Realiza a divisão treino/teste.
* Avalia o modelo utilizando a métrica RMSE (Root Mean Squared Error).

---

## 📄 `recomendador.py`

```python
import argparse
import logging
import pandas as pd

def recomendar_livros(model, ratings, books, user_id, n=5):
    if user_id not in ratings['user_id'].values:
        raise ValueError(f"Usuário {user_id} não encontrado nos dados.")

    livros_lidos = set(ratings[ratings['user_id'] == user_id]['book_id'])
    todos_livros = set(ratings['book_id'].unique())
    livros_nao_lidos = todos_livros - livros_lidos

    predicoes = [(livro, model.predict(user_id, livro).est) for livro in livros_nao_lidos]
    predicoes.sort(key=lambda x: x[1], reverse=True)

    id_para_titulo = dict(zip(books['book_id'], books['title']))
    recomendacoes = [
        {"book_id": livro_id, "title": id_para_titulo.get(livro_id, "Desconhecido"), "score": score}
        for livro_id, score in predicoes[:n]
    ]

    for r in recomendacoes:
        logging.info(f"- {r['title']} (score: {r['score']:.2f})")

    pd.DataFrame(recomendacoes).to_csv(f"recomendacoes_usuario_{user_id}.csv", index=False)
    logging.info(f"Recomendações exportadas para recomendacoes_usuario_{user_id}.csv")
```

### O que faz:

* Gera as recomendações para um usuário específico com base nos livros que ele ainda não leu.
* Usa o modelo para prever a nota que o usuário daria a cada livro não lido.

* Ordena os livros por melhor score e exporta os resultados para um arquivo `.csv`.

1. Coleta os livros que o usuário **já leu**.
2. Pega todos os outros livros do dataset.
3. Usa o modelo para **prever a nota estimada** que o usuário daria para cada livro não lido.
4. Ordena os livros por nota estimada (da maior para a menor).
5. Exibe os **top N livros recomendados**.

---

## 📄 `main.py`

```python
import argparse
import logging

from dados import carregar_dados
from modelo import treinar_modelo, avaliar_modelo
from recomendador import recomendar_livros

def main():
    parser = argparse.ArgumentParser(description="Sistema de recomendação de livros com SVD")
    parser.add_argument("--user_id", type=int, required=True, help="ID do usuário para recomendação")
    parser.add_argument("--top_n", type=int, default=5, help="Número de recomendações a exibir")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")

    caminho_ratings = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv"
    caminho_books = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"

    ratings, books = carregar_dados(caminho_ratings, caminho_books)
    model, testset = treinar_modelo(ratings)
    avaliar_modelo(model, testset)
    recomendar_livros(model, ratings, books, args.user_id, args.top_n)

if __name__ == "__main__":
    main()
```

### O que faz:

* Centraliza a execução do pipeline completo do sistema de recomendação.
* Recebe parâmetros via linha de comando: `--user_id` e `--top_n`.
* Realiza o carregamento dos dados, o treinamento do modelo e a recomendação final.

---

## ✅ Exemplo de execução no terminal

```bash
poetry shell
python src/pos/main.py --user_id 1 --top_n 5
```

---

Se precisar gerar uma nova explicação ou exportar este conteúdo, posso converter para PDF ou HTML. Basta pedir!
