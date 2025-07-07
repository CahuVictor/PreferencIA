# src\pos\dados.py
import pandas as pd

def carregar_dados(caminho_ratings, caminho_books, min_avaliacoes=50):
    ratings = pd.read_csv(caminho_ratings)
    books = pd.read_csv(caminho_books)
    user_counts = ratings['user_id'].value_counts()
    ratings_filtrados = ratings[ratings['user_id'].isin(user_counts[user_counts >= min_avaliacoes].index)]
    return ratings_filtrados, books

def carregar_dados_2(caminho_ratings, caminho_books, min_avaliacoes=50):
    ratings = pd.read_csv(caminho_ratings, sep=';', encoding='ISO-8859-1')
    books = pd.read_csv(caminho_books, sep=';', encoding='ISO-8859-1')
    
    ratings = pd.read_csv(
        caminho_ratings,
        sep=';',
        encoding='latin-1', # 'ISO-8859-1'
        quotechar='"',
        on_bad_lines='skip'  # Pandas >= 1.3.0
    )
    
    print("Ratings:")
    print(ratings.head())

    books = pd.read_csv(
        caminho_books,
        sep=';',
        encoding='latin-1', # 'ISO-8859-1'
        quotechar='"',
        on_bad_lines='skip'  # ignora linhas com erro de formatação
    )
    
    print("Books:")
    print(books.head())

    # Renomear colunas para manter compatibilidade
    ratings.rename(columns={"User-ID": "user_id", "ISBN": "book_id", "Book-Rating": "rating"}, inplace=True)
    books.rename(columns={"ISBN": "book_id", "Book-Title": "title"}, inplace=True)
    
    print("Ratings:")
    print(ratings.head())
    print("Books:")
    print(books.head())

    # Filtrar apenas usuários com no mínimo X avaliações
    user_counts = ratings['user_id'].value_counts()
    ratings_filtrados = ratings[ratings['user_id'].isin(user_counts[user_counts >= min_avaliacoes].index)]
    
    print("Rating Filtrados:")
    print(ratings_filtrados.head())

    return ratings_filtrados, books