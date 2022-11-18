import pandas as pd
from pricing_functions import data_treatment, request, product_pricing
import seaborn as sns
import matplotlib.pyplot as plt

product_database = {}
weeks = 36
all_df = pd.DataFrame([])
all_jsons = []

for week in range(weeks):
    json = request()
    json = data_treatment(request())
    json, product_database = product_pricing(json, product_database)
    all_jsons.append(json)

def df_to_analysis(all_jsons:list, column_name:str):
    new_json = {}
    n = 0
    for week in range(len(all_jsons)):
        for transaction in range(len(all_jsons[week])):
            balance = 0
            new_json[n] = {}
            new_json[n]['date'] = all_jsons[week][transaction]['date']
            new_json[n]['week'] = f'Week {week+1}'
            new_json[n]['month']=all_jsons[week][transaction]['date']
            new_json[n]['id'] = all_jsons[week][transaction]['id']
            for key in all_jsons[week][transaction]:
                if ('prod' in key):
                    if (type(all_jsons[week][transaction][key][column_name])==list): #teste
                        new_json[n][key] = float(all_jsons[week][transaction][key][column_name][0])
                    else:
                        new_json[n][key] = float(all_jsons[week][transaction][key][column_name])
                    balance += new_json[n][key]
            n += 1  
    df = pd.DataFrame(new_json).T
    df['balance'] = balance
    df['date'] = pd.to_datetime(df['date']).dt.date
    df['month'] = pd.to_datetime(df['month']).dt.month_name()
    df=df.fillna(0)
    return df

def consolidate(df_qnt:pd.DataFrame, df_price:pd.DataFrame, df_consolidate:pd.DataFrame):
    for prod in df_qnt.columns:
        df_consolidate[prod]=df_qnt[prod]*df_price[prod]
    return df_consolidate

def balance_product(df):
    list = []
    for row in df.index:
        list.append(df.loc[row].sum())
    return list

def calc_ratio(all_prices:pd.DataFrame, dict_dfs:dict, period: str, variable:str, unity_of_period:str):
    num_transactions = len(all_prices[all_prices[period]==unity_of_period])
    balance = dict_dfs[period][variable].loc[unity_of_period,'balance']
    ratio = balance/num_transactions
    return ratio

def join_all_ratios(teste:str,all_prices:pd.DataFrame, monthly_price:dict, dict_dfs:dict, period:str, variable: str, report:bool):
    all_ratios = []
    for unity in dict_dfs[period][variable].index:
        ratio = calc_ratio(all_prices=all_prices, dict_dfs=dict_dfs,period=period,variable=variable, unity_of_period=unity)
        all_ratios.append(ratio)
    if report:
        return all_ratios
    else:
        fig, ax = plt.subplots(figsize=(12, 5))
        sns.lineplot(x=monthly_price.index, y=all_ratios)
        sns.set_style('darkgrid')

def print_barplot(x,y):
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(x=x, y=y, palette="tab10")
    sns.set_style('darkgrid')

def consolidate_per_transaction(dict_dfs:dict, period:str, qnt:list, price:list):
    consolidate = [qnt[i]*price[i] for i in range(len(qnt))]
    print(consolidate[0])
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(x=dict_dfs[period]['qnt'].index, y=consolidate)
    sns.set_style('darkgrid')

def barplot_type(df:pd.DataFrame, type_column:list):
    new_df= df.T
    new_df = new_df.drop('balance')
    new_df['type'] = type_column
    new_df = new_df.groupby('type').agg({f'{x}':'sum' for x in new_df.columns[:-1]})
    new_df['balance'] = balance_product(new_df)

    print_barplot(x=new_df.index, y = new_df['balance'])
    return new_df.index
