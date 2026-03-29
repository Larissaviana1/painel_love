import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Para você meu bem ❤️", layout="centered")

st.markdown("<h2 style='text-align:center;'>Para você meu bem 💖</h2>", unsafe_allow_html=True)

# Placeholder para atualizar gráfico
placeholder = st.empty()

# Curva do coração
t = np.linspace(0, 2*np.pi, 800)

base_x = 16 * np.sin(t)**3
base_y = (13 * np.cos(t)
          - 5 * np.cos(2*t)
          - 2 * np.cos(3*t)
          - np.cos(4*t))

# Animação
for frame in range(1000):
    
    # efeito de batimento
    scale = 1 + 0.05 * np.sin(frame * 0.2)
    
    x = base_x * scale
    y = base_y * scale

    fig, ax = plt.subplots()

    # cor dinâmica (RGB suave)
    r = (np.sin(frame * 0.1) + 1) / 2
    g = (np.sin(frame * 0.1 + 2) + 1) / 2
    b = (np.sin(frame * 0.1 + 4) + 1) / 2

    color = (r, g, b)

    # efeito LED (vários pontos com ruído)
    for _ in range(6):
        ax.scatter(
            x + np.random.normal(0, 0.1, len(x)),
            y + np.random.normal(0, 0.1, len(y)),
            s=8,
            color=color,
            alpha=0.7
        )

    ax.set_facecolor("black")
    fig.patch.set_facecolor("black")
    ax.axis('off')

    placeholder.pyplot(fig)
    plt.close(fig)

    time.sleep(0.05)

st.markdown(
    "<h3 style='text-align:center; color:#ff4d6d;'>Eu te amo 💕</h3>",
    unsafe_allow_html=True
)
