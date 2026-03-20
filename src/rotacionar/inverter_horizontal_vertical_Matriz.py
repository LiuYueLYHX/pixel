import pandas as pd

# carregar arquivo
df = pd.read_csv("matriz.csv", sep=";")

# inverter primeira coluna
linha = df.columns[0]
df.loc[1:, linha] = df.loc[1:, linha].iloc[::-1].values

# inverter segunda coluna
coluna = df.columns[1]
df.loc[1:, coluna] = df.loc[1:, coluna].iloc[::-1].values

# salvar
df.to_csv("inverter_horizontal_vertical.csv", index=False, sep=";")