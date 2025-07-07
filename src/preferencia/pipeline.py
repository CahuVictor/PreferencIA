# pipeline.py
def run_full_pipeline(cfg: dict):
    df_ratings, df_items, df_users = preprocess(cfg["data"], cfg["filter"])
    model = train(df_ratings, cfg["train"])
    make_recommendations(model, df_items, cfg["recommend"])