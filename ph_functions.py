import pandas as pd
from ys_functions import df_to_analysis

def plot_prod_qnt(all_df):
    group_qnt = all_df.groupby('product')['qnt'].sum()
    df_prod = pd.DataFrame(group_qnt)
    plot_prod = df_prod.plot(kind='bar')
    return plot_prod


def plot_month_balance(all_df):
    df_balance = all_df.copy()
    df_balance['balance'] = df_balance['qnt'] * df_balance['price']
    df_months_balance = pd.DataFrame(df_balance.groupby('month')['balance'].sum())
    plot_months = df_months_balance.plot(kind='pie', subplots=True)
    return plot_months


def all_sales_csv(all_jsons):
    all_qnt = df_to_analysis(all_jsons=all_jsons, column_name='qnt')
    all_qnt.to_csv('all_sales.csv', index=False)
