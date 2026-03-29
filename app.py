import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Para você 💚", layout="centered")

placeholder = st.empty()

# ======================
# CONFIGURAÇÃO DO CORAÇÃO
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
# 1. FORMAÇÃO DO CORAÇÃO
# ======================
for r, c in positions:
    grid[r][c] = random.choice(["❤️", "💖", "💕", "💓"])

    html = "<div style='text-align:center; line-height:1;'>"
    for row in reversed(grid):
        html += "".join(f"<span style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"
    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.02)

# ======================
# 2. ANIMAÇÃO DO NOME (VERDE)
# ======================

nome = "ARIEL"

# grid do nome
nome_grid = [["⠀" for _ in range(len(nome))] for _ in range(1)]

for i, letra in enumerate(nome):
    nome_grid[0][i] = "💚"

    html = "<div style='text-align:center; line-height:1;'>"

    # coração
    for row in reversed(grid):
        html += "".join(f"<span style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"

    html += "<br>"

    # nome
    html += "<div style='font-size:22px'>"
    html += "".join(f"<span>{cell}</span>" for cell in nome_grid[0])
    html += "</div>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.3)

# ======================
# 3. CORAÇÃO BATENDO + NOME FIXO
# ======================
while True:
    for scale in [1.0, 1.15, 1.0]:
        html = "<div style='text-align:center; line-height:1;'>"

        # coração batendo
        for row in reversed(grid):
            html += "".join(
                f"<span style='font-size:{int(16*scale)}px'>{cell}</span>"
                for cell in row
            )
            html += "<br>"

        html += "<br>"

        # nome fixo
        html += "<div style='font-size:22px'>"
        html += "💚💚💚💚💚"
        html += "</div>"

        html += "</div>"

        placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.25)
