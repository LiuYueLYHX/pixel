from PIL import Image
import pandas as pd
import numpy as np

# carregar os dados
df = pd.read_csv("diminuir.csv", sep=";")

# descobrir tamanho da imagem (converter para inteiro)
altura = int(round(df["linha"].max())) + 1
largura = int(round(df["coluna"].max())) + 1

# criar matriz vazia
matriz = np.zeros((altura, largura, 3), dtype=np.uint8)

# preencher a matriz com os pixels
for _, row in df.iterrows():
    i = int(round(row["linha"]))
    j = int(round(row["coluna"]))
    matriz[i, j] = [int(row["R"]), int(row["G"]), int(row["B"])]

# reconstruir imagem
img = Image.fromarray(matriz)

# mostrar ou salvar
img.show()
img.save("diminuir.png")