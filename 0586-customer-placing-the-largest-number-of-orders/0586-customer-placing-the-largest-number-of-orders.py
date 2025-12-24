import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    counts = orders.groupby('customer_number').size().reset_index(name='cnt')
    counts =  counts.sort_values(by='cnt',ascending=False)

    return counts[['customer_number']].head(1)