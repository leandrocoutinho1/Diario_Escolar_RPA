import pandas as pd


df = pd.read_csv('data/in/Dados Diário - Página1.csv')

for index, row in df.iterrows():
    nome = row['Nome']
    idade = row['Idade']
    cpf = row['CPF']

    print(f"Linha {index}: Nome: {nome}, Idade: {idade}, CPF: {cpf}")


novo_df = df.copy()
novo_df['Sucesso'] = 'Não'

for index, row in df.iterrows():
    if True:
         novo_df.at[index, 'Sucesso'] = 'Sim'
    

print(novo_df.head())

output_file_path = './data/out/resultado.csv'

# Salvar o novo DataFrame como um arquivo Excel
novo_df.to_csv(output_file_path, index=False)