import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Para você ❤️", layout="centered")

st.markdown("<h2 style='text-align:center;'>Para você 💖</h2>", unsafe_allow_html=True)

# Gerar pontos do coração
t = np.linspace(0, 2*np.pi, 800)

x = 16 * np.sin(t)**3
y = (13 * np.cos(t)
     - 5 * np.cos(2*t)
     - 2 * np.cos(3*t)
     - np.cos(4*t))

# Plot
fig, ax = plt.subplots()

# Simular efeito LED com vários pontos
for i in range(10):
    ax.scatter(
        x + np.random.normal(0, 0.1, len(x)),
        y + np.random.normal(0, 0.1, len(y)),
        s=10,
        alpha=0.6
    )

# Cor e estilo
ax.set_facecolor("black")
fig.patch.set_facecolor("black")

ax.axis('off')

st.pyplot(fig)

st.markdown(
    "<h3 style='text-align:center; color:#ff4d6d;'>Eu te amo 💕</h3>",
    unsafe_allow_html=True
)
