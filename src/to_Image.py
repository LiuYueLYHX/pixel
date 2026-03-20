from PIL import Image
import pandas as pd
import numpy as np

# carregar os dados
df = pd.read_csv("girar.csv", sep=";")

# descobrir tamanho da imagem
altura = df["linha"].max() + 1
largura = df["coluna"].max() + 1

# criar matriz vazia
matriz = np.zeros((altura, largura, 3), dtype=np.uint8)

# preencher a matriz com os pixels
for _, row in df.iterrows():
    i = int(row["linha"])
    j = int(row["coluna"])
    matriz[i, j] = [row["R"], row["G"], row["B"]]

# reconstruir imagem
img = Image.fromarray(matriz)

# mostrar ou salvar
img.show()
img.save("girar.png")