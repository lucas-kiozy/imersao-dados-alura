import pandas as pd

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
print(df.describe(include="object"))