import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import accuracy


ratings = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv")
books = pd.read_csv("https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv")


user_counts = ratings['user_id'].value_counts()
ratings = ratings[ratings['user_id'].isin(user_counts[user_counts >= 50].index)]

reader = Reader(rating_scale=(0, 5))
data = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)


trainset, testset = train_test_split(data, test_size=0.2, random_state=42)
model = SVD()
model.fit(trainset)


predictions = model.test(testset)
accuracy.rmse(predictions)


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


recomendar_svd(user_id=1)