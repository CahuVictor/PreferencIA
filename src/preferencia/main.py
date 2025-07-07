# src\pos\main.py
import argparse
import logging

from dados import carregar_dados, carregar_dados_2
from modelo import treinar_modelo, avaliar_modelo
from recomendador import recomendar_livros

def main():
    parser = argparse.ArgumentParser(description="Sistema de recomendação de livros com SVD")
    parser.add_argument("--user_id", type=int, required=True, help="ID do usuário para recomendação")
    parser.add_argument("--top_n", type=int, default=5, help="Número de recomendações a exibir")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    
    # ---------------------------------------------------------------------------
    # TODO:
    # This project selector is a **temporary** bridge while the codebase is
    # evolving. Once the main application is consolidated, `main()` will accept
    # a *single, already-structured* dataset (ratings + items metadata) via an
    # argument, configuration file, or CLI flag. That change will eliminate the
    # hard-coded `project_number` switch below and turn this script into a more
    # robust, reusable module that other services can import without editing
    # source code.
    # ---------------------------------------------------------------------------
    
    project_number = 1
    
    if project_number == 1:
        caminho_ratings = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv"
        caminho_books = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv"
        
        ratings, books = carregar_dados(caminho_ratings, caminho_books)
    
    if project_number == 2:
        caminho_ratings = "data/BX-Book-Ratings.csv"
        caminho_books = "data/BX-Books.csv"
        
        ratings, books = carregar_dados_2(caminho_ratings, caminho_books)
    
    # ---------------------------------------------------------------------------
    # TODO
    # ---------------------------------------------------------------------------

    model, testset = treinar_modelo(ratings)
    avaliar_modelo(model, testset)
    recomendar_livros(model, ratings, books, args.user_id, args.top_n)

if __name__ == "__main__":
    main()
