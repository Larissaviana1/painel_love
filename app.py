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

.neon-green-text {
    color: #39ff14;
    font-weight: bold;
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
# 1. CORAÇÃO MAIS CLEAN
# ======================
for i in range(size):
    for j in range(size):
        if heart[i][j]:
            # controla densidade aqui
            if random.random() < 0.35:   # ↓ menor valor = menos emojis
                grid[i][j] = random.choice(["❤️", "💖"])

def render(nome_texto="", scale=1.0):
    html = "<div style='text-align:center; line-height:1;'>"

    for row in reversed(grid):
        html += "".join(
            f"<span class='neon-heart' style='font-size:{int(16*scale)}px'>{cell}</span>"
            for cell in row
        )
        html += "<br>"

    html += "<br>"

    if nome_texto:
        html += f"<div class='neon-green-text' style='font-size:40px; letter-spacing:6px'>{nome_texto}</div>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)

# mostrar coração
render()
time.sleep(1)

# ======================
# 2. NOME ANIMADO
# ======================
nome = "ARIEL"
nome_parcial = ""

for letra in nome:
    nome_parcial += letra
    render(nome_parcial)
    time.sleep(0.4)

# ======================
# 3. BATIMENTO
# ======================
while True:
    for scale in [1.0, 1.18, 1.0]:
        render(nome, scale)
        time.sleep(0.25)
