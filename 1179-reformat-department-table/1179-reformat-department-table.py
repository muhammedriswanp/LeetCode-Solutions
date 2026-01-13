import pandas as pd

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    df = department.pivot_table(index='id',columns='month',values='revenue',aggfunc='sum')
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df = df.reindex(columns=months)
    df.columns = [f"{m}_Revenue" for m in months]
    return df.reset_index()
