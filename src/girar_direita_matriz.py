import pandas as pd

# carregar arquivo
df = pd.read_csv("matriz.csv", sep=";")

# trocar colunas A e B
df[["linha", "coluna"]] = df[["coluna", "linha"]]

# salvar novo arquivo
df.to_csv("girar.csv", index=False, sep=";")