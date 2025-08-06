import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df = df.rename(columns={
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_salario',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'local_empresa',
    'company_size': 'porte_empresa'
})

# print(df.head(6))

# df.info()

# print(df.describe())

# print(f'Quantidade de linhas: {df.shape[0]}, quantidade de colunas: {df.shape[1]}')

# print(df.columns)

# print(df["senioridade"].value_counts())

# print(df["contrato"].value_counts())

# print(df["remoto"].value_counts())

# print(df["porte_empresa"].value_counts())

senioridade = {
    'SE': 'Sênior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}
df["senioridade"] = df["senioridade"].replace(senioridade)
# print(df["senioridade"].value_counts())

contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Meio Período',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
df["contrato"] = df["contrato"].replace(contrato)
#print(df["contrato"].value_counts())

porte_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
}
df["porte_empresa"] = df["porte_empresa"].replace(porte_empresa)
#print(df["porte_empresa"].value_counts())

remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df["remoto"] = df["remoto"].replace(remoto)
#print(df["remoto"].value_counts())

# print(df.head(10))
# print(df.describe(include="object"))


#*** COMEÇANDO A AULA 2 COM TRATAMENTO DE DADOS ***

# print(df.isnull().sum())

# print(df['ano'].unique())  # Verifica os anos únicos

#print(df[df.isnull().any(axis=1)])  # Verifica linhas com valores nulos


# df_salarios = pd.DataFrame({
#     'nome': ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo'],
#     'salario': [3000, np.nan, 4000, np.nan, 4000]
# })

# df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))  #Média dos salários
# df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())  #Mediana dos salários

# print(df_salarios)


# df_temperaturas = pd.DataFrame({
#     'dia': ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo'],
#     'temperatura': [30, 27, np.nan, 28, np.nan, np.nan, 29]
# })

# df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()  # Preenche com o valor anterior
# df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()  # Preenche com o valor posterior

# print(df_temperaturas)


# df_cidades = pd.DataFrame({
#     'nome': ['Ana', 'Bia', 'Carlos', 'Daniel', 'Eduardo'],
#     'cidade': [np.nan, 'Rio de Janeiro', np.nan, 'Curitiba', 'Porto Alegre']
# })
# df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Não Informada')  # Preenche com 'Não Informada'

# print(df_cidades)


df_limpo = df.dropna()  # Remove linhas onde há campos NaN
# print(df_limpo.isnull().sum())

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int64'))  # Converte a coluna 'ano' para o tipo inteiro
print(df_limpo.info())
print(df_limpo.head(6))