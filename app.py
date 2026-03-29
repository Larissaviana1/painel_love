import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Para você 💚", layout="centered")

# ======================
# ESTILO GLOBAL (NEON + FUNDO PRETO)
# ======================
st.markdown("""
<style>
body {
    background-color: #000000;
}

.neon {
    color: #39ff14;
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

positions = [(i, j) for i in range(size) for j in range(size) if heart[i][j]]
random.shuffle(positions)

grid = [["⠀" for _ in range(size)] for _ in range(size)]

# ======================
# 1. FORMAR CORAÇÃO
# ======================
for r, c in positions:
    grid[r][c] = random.choice(["❤️", "💖", "💕", "💓"])

    html = "<div style='text-align:center; line-height:1;'>"
    for row in reversed(grid):
        html += "".join(f"<span class='neon' style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"
    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.02)

# ======================
# NOME "ARIEL" EM LED
# ======================
letters = {
    "A": [" 1 ","1 1","111","1 1","1 1"],
    "R": ["11 ","1 1","11 ","1 1","1 1"],
    "I": ["111"," 1 "," 1 "," 1 ","111"],
    "E": ["111","1  ","111","1  ","111"],
    "L": ["1  ","1  ","1  ","1  ","111"]
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
# 2. ANIMAÇÃO DO NOME
# ======================
for r, c in pos_nome:
    nome_display[r][c] = "💚"

    html = "<div style='text-align:center; line-height:1;'>"

    for row in reversed(grid):
        html += "".join(f"<span class='neon' style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"

    html += "<br>"

    for row in nome_display:
        html += "".join(f"<span class='neon' style='font-size:18px'>{cell}</span>" for cell in row)
        html += "<br>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.04)

# ======================
# 3. BATIMENTO NEON
# ======================
while True:
    for scale in [1.0, 1.2, 1.0]:
        html = "<div style='text-align:center; line-height:1;'>"

        for row in reversed(grid):
            html += "".join(
                f"<span class='neon' style='font-size:{int(16*scale)}px'>{cell}</span>"
                for cell in row
            )
            html += "<br>"

        html += "<br>"

        for row in nome_display:
            html += "".join(f"<span class='neon' style='font-size:18px'>{cell}</span>" for cell in row)
            html += "<br>"

        html += "</div>"

        placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.25)
