import streamlit as st
import numpy as np

st.set_page_config(page_title="Para você 💜", layout="centered")

# ======================
# ESTILO (FUNDO PRETO + TEXTO)
# ======================
st.markdown("""
<style>
.stApp {
    background-color: black;
    text-align: center;
}

.titulo {
    color: white;
    font-size: 32px;
    margin-bottom: 20px;
}

.nome {
    color: #b266ff;
    font-size: 36px;
    margin-top: 25px;
    letter-spacing: 6px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# TEXTO SUPERIOR
# ======================
st.markdown("<div class='titulo'>Para você meu bem</div>", unsafe_allow_html=True)

# ======================
# GERAR CORAÇÃO (CONTORNO)
# ======================
size = 40
x = np.linspace(-1.5, 1.5, size)
y = np.linspace(-1.5, 1.5, size)

X, Y = np.meshgrid(x, y)

F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

# contorno do coração
border = np.abs(F) < 0.02

# construir HTML
html = "<div style='line-height:1;'>"

for i in range(size-1, -1, -1):
    for j in range(size):
        if border[i][j]:
            html += "<span style='font-size:18px;'>💜</span>"
        else:
            html += "<span style='font-size:18px;'>⠀</span>"
    html += "<br>"

html += "</div>"

st.markdown(html, unsafe_allow_html=True)

# ======================
# TEXTO INFERIOR
# ======================
st.markdown("<div class='nome'>ARIEL 💜</div>", unsafe_allow_html=True)
