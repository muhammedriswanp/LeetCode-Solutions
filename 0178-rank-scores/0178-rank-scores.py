import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank']=scores['score'].rank(method = "dense",ascending = False).astype(int)
    scores.sort_values(by='score', ascending=False, inplace=True)

    return scores[['score','rank']]
    