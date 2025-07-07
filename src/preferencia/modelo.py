# src\pos\modelo.py
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
