import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Para você 💚", layout="centered")

# ======================
# FUNDO PRETO + NEON
# ======================
st.markdown("""
<style>
.stApp {
    background-color: black;
}

html, body {
    background-color: black;
}

.neon-heart {
    text-shadow:
        0 0 5px #ff4d6d,
        0 0 10px #ff4d6d,
        0 0 20px #ff4d6d,
        0 0 40px #ff4d6d;
}

.neon-green {
    text-shadow:
        0 0 5px #39ff14,
        0 0 10px #39ff14,
        0 0 20px #39ff14,
        0 0 40px #39ff14;
}
</style>
""", unsafe_allow_html=True)

placeholder = st.empty()

# ======================
# CONFIG CORAÇÃO
# ======================
size = 30
x = np.linspace(-1.5, 1.5, size)
y = np.linspace(-1.5, 1.5, size)

X, Y = np.meshgrid(x, y)
heart = (X**2 + Y**2 - 1)**3 - X**2 * Y**3 <= 0

grid = [["⠀" for _ in range(size)] for _ in range(size)]

# ======================
# 1. CORAÇÃO APARECE DE UMA VEZ
# ======================
for i in range(size):
    for j in range(size):
        if heart[i][j]:
            grid[i][j] = random.choice(["❤️", "💖", "💕", "💓"])

html = "<div style='text-align:center; line-height:1;'>"
for row in reversed(grid):
    html += "".join(f"<span class='neon-heart' style='font-size:16px'>{cell}</span>" for cell in row)
    html += "<br>"
html += "</div>"

placeholder.markdown(html, unsafe_allow_html=True)

time.sleep(1)

# ======================
# MATRIZ DO NOME (AJUSTADA)
# ======================
letters = {
    "A": [" 11 ","1  1","1111","1  1","1  1"],
    "R": ["111 ","1  1","111 ","1 1 ","1  1"],
    "I": ["111"," 1 "," 1 "," 1 ","111"],
    "E": ["1111","1   ","111 ","1   ","1111"],
    "L": ["1   ","1   ","1   ","1   ","1111"]
}

nome = "ARIEL"

nome_grid = []
for linha in range(5):
    row = ""
    for letra in nome:
        row += letters[letra][linha] + "  "
    nome_grid.append(row)

nome_matrix = [list(linha) for linha in nome_grid]

pos_nome = [(i, j) for i in range(len(nome_matrix)) for j in range(len(nome_matrix[0])) if nome_matrix[i][j] == "1"]
random.shuffle(pos_nome)

nome_display = [["⠀" for _ in range(len(nome_matrix[0]))] for _ in range(len(nome_matrix))]

# ======================
# 2. NOME APARECENDO
# ======================
for r, c in pos_nome:
    nome_display[r][c] = "💚"

    html = "<div style='text-align:center; line-height:1;'>"

    for row in reversed(grid):
        html += "".join(f"<span class='neon-heart' style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"

    html += "<br>"

    for row in nome_display:
        html += "".join(f"<span class='neon-green' style='font-size:18px'>{cell}</span>" for cell in row)
        html += "<br>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.04)

# ======================
# 3. BATIMENTO
# ======================
while True:
    for scale in [1.0, 1.18, 1.0]:
        html = "<div style='text-align:center; line-height:1;'>"

        for row in reversed(grid):
            html += "".join(
                f"<span class='neon-heart' style='font-size:{int(16*scale)}px'>{cell}</span>"
                for cell in row
            )
            html += "<br>"

        html += "<br>"

        for row in nome_display:
            html += "".join(f"<span class='neon-green' style='font-size:18px'>{cell}</span>" for cell in row)
            html += "<br>"

        html += "</div>"

        placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.25)
