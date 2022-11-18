import pandas as pd

def resume (produtos, semana):

   df = produtos.copy()
   somas = []
   prices = []
   colunas = list(df.columns)

   for i in range(df.shape[1]):
      somas.append(sum(df.iloc[0,i]))
      prices.append(df.iloc[1,i])
      
   lista_de_tuplas = list(zip(colunas, somas, prices))
   new_df = pd.DataFrame(lista_de_tuplas, columns = ['produto', 'soma', 'preço'])
   new_df['receita'] = new_df['soma'] * new_df['preço']
   
   new_df['week'] = semana
   
   return new_df
