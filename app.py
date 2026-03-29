import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Para você 💜", layout="centered")

# Estilo
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    .titulo {
        color: #ff4da6 !important;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="titulo">Para você meu bem &lt;3</div>', unsafe_allow_html=True)

# Função coração
def heart(t):
    x = 16 * np.sin(t)**3
    y = (
        13 * np.cos(t)
        - 5 * np.cos(2 * t)
        - 2 * np.cos(3 * t)
        - np.cos(4 * t)
    )
    return x, y

placeholder = st.empty()

t = np.linspace(0, 2 * np.pi, 1000)

# Animação controlada (SEM while infinito)
for frame in range(200):
    scale = 1 + 0.2 * np.sin(frame * 0.2)

    x, y = heart(t)

    fig, ax = plt.subplots()

    ax.plot(x * scale, y * scale, color="#b266ff", linewidth=5)

    ax.set_aspect('equal')
    ax.axis("off")

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    placeholder.pyplot(fig)

    time.sleep(0.03)
