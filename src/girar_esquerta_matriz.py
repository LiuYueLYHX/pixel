import pandas as pd

# carregar arquivo
df = pd.read_csv("matriz.csv", sep=";")

coluna = df.columns[1]
df.loc[1:, coluna] = df.loc[1:, coluna].iloc[::-1].values

# trocar colunas A e B
df[["linha", "coluna"]] = df[["coluna", "linha"]]

# salvar novo arquivo
df.to_csv("girar_esquerta.csv", index=False, sep=";")