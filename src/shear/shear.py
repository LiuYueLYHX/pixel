import pandas as pd
import numpy as np
from PIL import Image

# 1. 读取 Excel 或 CSV
df = pd.read_csv("matriz.csv", sep=";")  # 或 pd.read_csv("matriz.csv", sep=";")

# 2. 设置剪切系数
kx = 0.5  # 水平剪切
ky = 0.3  # 垂直剪切

# 3. 计算新的坐标
df["linha_nova"] = df["linha"] + kx * df["coluna"]  # 水平剪切
df["coluna_nova"] = df["coluna"] + ky * df["linha"]  # 垂直剪切

# 4. 将 float 坐标转为整数
df["linha_nova"] = df["linha_nova"].round().astype(int)
df["coluna_nova"] = df["coluna_nova"].round().astype(int)

# 5. 创建图像矩阵
altura = df["linha_nova"].max() + 1
largura = df["coluna_nova"].max() + 1
matriz = np.zeros((altura, largura, 3), dtype=np.uint8)

# 6. 填充像素
for _, row in df.iterrows():
    i = row["linha_nova"]
    j = row["coluna_nova"]
    matriz[i, j] = [int(row["R"]), int(row["G"]), int(row["B"])]

# 7. 生成图像
img = Image.fromarray(matriz)
img.show()
img.save("imagem_shear.png")