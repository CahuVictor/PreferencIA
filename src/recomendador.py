# src\pos\recomendador.py
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