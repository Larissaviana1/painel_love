import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Para você 💜", layout="centered")

# ======================
# TEXTO SUPERIOR
# ======================
st.markdown(
    "<h2 style='text-align:center; color:white;'>Para você meu bem</h2>",
    unsafe_allow_html=True
)

# ======================
# GERAR CORAÇÃO
# ======================
t = np.linspace(0, 2*np.pi, 800)

x = 16 * np.sin(t)**3
y = (13 * np.cos(t)
     - 5 * np.cos(2*t)
     - 2 * np.cos(3*t)
     - np.cos(4*t))

# ======================
# PLOT
# ======================
fig, ax = plt.subplots()

# efeito contorno com pontos (mais limpo)
for _ in range(4):
    ax.scatter(
        x + np.random.normal(0, 0.05, len(x)),
        y + np.random.normal(0, 0.05, len(y)),
        s=8,
        color="#b266ff",
        alpha=0.8
    )

# fundo preto
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

ax.axis('off')

st.pyplot(fig)

# ======================
# TEXTO INFERIOR
# ======================
st.markdown(
    "<h3 style='text-align:center; color:#b266ff;'>ARIEL 💜</h3>",
    unsafe_allow_html=True
)
