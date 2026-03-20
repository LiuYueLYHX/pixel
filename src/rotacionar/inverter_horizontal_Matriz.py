import pandas as pd

# carregar arquivo
df = pd.read_csv("matriz.csv", sep=";")

# nome da primeira coluna (ou pode usar df.columns[0])
coluna = df.columns[1]

# inverter apenas os dados da coluna, sem mexer no cabeçalho
df[coluna].iloc[1:] = df[coluna].iloc[1:][::-1].values

# salvar novo arquivo
df.to_csv("inverter_horizontal.csv", index=False, sep=";")