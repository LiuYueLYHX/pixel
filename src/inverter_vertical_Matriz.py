import pandas as pd

# carregar arquivo
df = pd.read_csv("matriz.csv", sep=";")

# nome da primeira coluna (ou pode usar df.columns[0])
linha = df.columns[0]

# inverter apenas os dados da coluna, sem mexer no cabeçalho
df[linha].iloc[1:] = df[linha].iloc[1:][::-1].values

# salvar novo arquivo
df.to_csv("inverter_Verticalmente.csv", index=False, sep=";")