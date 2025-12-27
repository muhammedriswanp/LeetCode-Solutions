import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    conditon = actor_director.groupby(['actor_id','director_id'])['director_id'].count().reset_index(name = 'cnt')
    
    return conditon[['actor_id','director_id']][conditon['cnt']>=3]