import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates() 
    result_table = activities.groupby('sell_date')['product'].agg(
        num_sold = 'count',
        products =  lambda x : ','.join(sorted(x))
    ).reset_index()

    return result_table