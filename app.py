import streamlit as st
import numpy as np
import time
import random

st.set_page_config(page_title="Para você ❤️", layout="centered")

st.markdown("<h2 style='text-align:center;'>Para você 💖</h2>", unsafe_allow_html=True)

placeholder = st.empty()

# grid
size = 30
x = np.linspace(-1.5, 1.5, size)
y = np.linspace(-1.5, 1.5, size)

X, Y = np.meshgrid(x, y)

# equação do coração
heart = (X**2 + Y**2 - 1)**3 - X**2 * Y**3 <= 0

# posições do coração
positions = [(i, j) for i in range(size) for j in range(size) if heart[i][j]]

random.shuffle(positions)

# grid inicial vazio
grid = [["⠀" for _ in range(size)] for _ in range(size)]

# ======================
# 1. FORMAÇÃO DO CORAÇÃO
# ======================
for r, c in positions:
    grid[r][c] = random.choice(["❤️", "💖", "💕", "💓"])

    html = "<div style='text-align:center; line-height:1;'>"
    for row in reversed(grid):  # corrigido aqui
        html += "".join(f"<span style='font-size:16px'>{cell}</span>" for cell in row)
        html += "<br>"
    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.02)

# ======================
# 2. CORAÇÃO BATENDO
# ======================
while True:
    
    for scale in [1.0, 1.15, 1.0]:
        html = "<div style='text-align:center; line-height:1;'>"
        
        for row in reversed(grid):
            html += "".join(
                f"<span style='font-size:{int(16*scale)}px'>{cell}</span>"
                for cell in row
            )
            html += "<br>"
        
        html += "</div>"

        placeholder.markdown(html, unsafe_allow_html=True)
        time.sleep(0.25)

# mensagem final (fica antes do loop visual)
st.markdown(
    "<h3 style='text-align:center; margin-top:20px;'>Eu te amo 💕</h3>",
    unsafe_allow_html=True
)
