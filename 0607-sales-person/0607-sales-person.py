import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merg = company.merge(orders,on='com_id')
    unique = merg[merg['name']=='RED']['sales_id'].unique()
    return sales_person[~sales_person['sales_id'].isin(unique)][['name']]