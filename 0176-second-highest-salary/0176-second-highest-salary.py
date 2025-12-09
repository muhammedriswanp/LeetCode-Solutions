import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # step 1: distinct salaries
    # step 2: sort descending
    sorted_salaries  =  employee['salary'].drop_duplicates().sort_values(ascending = False)
    
    if len(sorted_salaries) >=2:
        second_value  = sorted_salaries.iloc[1]
    else:
        second_value  = None
    return pd.DataFrame({'SecondHighestSalary':[second_value]})