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

.neon-heart {
    text-shadow:
        0 0 8px #ff4d6d,
        0 0 16px #ff4d6d,
        0 0 32px #ff4d6d;
}

.neon-text {
    color: #39ff14;
    font-weight: bold;
    text-shadow:
        0 0 8px #39ff14,
        0 0 16px #39ff14,
        0 0 32px #39ff14;
}
</style>
""", unsafe_allow_html=True)

placeholder = st.empty()

# ======================
# CONFIG CORAÇÃO
# ======================
size = 40
x = np.linspace(-1.5, 1.5, size)
y = np.linspace(-1.5, 1.5, size)

X, Y = np.meshgrid(x, y)
F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# borda do coração
border = np.abs(F) < 0.02

grid = [["⠀" for _ in range(size)] for _ in range(size)]

# ======================
# CORAÇÃO BORDA CLEAN
# ======================
for i in range(size):
    for j in range(size):
        if border[i][j]:
            if random.random() < 0.6:  # densidade da borda
                grid[i][j] = "❤️"

def render(nome="", scale=1.0):
    html = "<div style='text-align:center; line-height:1;'>"

    for row in reversed(grid):
        html += "".join(
            f"<span class='neon-heart' style='font-size:{int(18*scale)}px'>{cell}</span>"
            for cell in row
        )
        html += "<br>"

    html += "<br>"

    if nome:
        html += f"<div class='neon-text' style='font-size:42px; letter-spacing:8px'>{nome}</div>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)

# ======================
# MOSTRAR CORAÇÃO
# ======================
render()
time.sleep(1)

# ======================
# NOME APARECENDO
# ======================
nome = "ARIEL"
nome_parcial = ""

for letra in nome:
    nome_parcial += letra
    render(nome_parcial)
    time.sleep(0.4)

# ======================
# BATIMENTO SUAVE
# ======================
while True:
    for scale in [1.0, 1.08, 1.0]:
        render(nome, scale)
        time.sleep(0.3)
