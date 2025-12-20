import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categorys = ['Low Salary','Average Salary','High Salary'] 
    low_count = len(accounts[accounts['income']<20000])
    medium_count = len(accounts[(accounts['income']>=20000)&(accounts['income']<=50000)])
    high_count = len(accounts[accounts['income']>50000])
    income = [low_count,medium_count,high_count]
    
    result = pd.DataFrame({
        'category':categorys,
        'accounts_count':income
    })
    return result