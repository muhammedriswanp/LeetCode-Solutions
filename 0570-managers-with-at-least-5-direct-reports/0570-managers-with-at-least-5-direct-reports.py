import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_counts = employee['managerId'].value_counts()
    top_managers_ids = manager_counts[manager_counts>=5].index
    result = employee[employee['id'].isin(top_managers_ids)][['name']]
    return result