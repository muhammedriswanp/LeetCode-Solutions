import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column_name = f'getNthHighestSalary({N})'
    if N <= 0:
        return pd.DataFrame({column_name: [None]})
    salary  = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    if N > len(salary):
        nth_salary = None
    else:
        nth_salary = salary.iloc[N - 1]

    column_name = f'getNthHighestSalary({N})'

    result = pd.DataFrame({column_name: [nth_salary]})
    
    return result