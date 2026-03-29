import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Configuração da página
st.set_page_config(page_title="Para você 💜", layout="centered")

# Fundo preto e texto rosa
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }
    h1 {
        color: #ff4da6;
        text-align: center;
        font-size: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Para você meu bem &lt;3</h1>", unsafe_allow_html=True)

# Função do coração
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

# Loop de pulsação
while True:
    for scale in np.linspace(0.85, 1.15, 12):
        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = heart(t)

        fig, ax = plt.subplots()

        ax.plot(x * scale, y * scale, color="#b266ff", linewidth=4)

        ax.set_aspect('equal')
        ax.axis("off")

        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        placeholder.pyplot(fig)
        time.sleep(0.07)

    for scale in np.linspace(1.15, 0.85, 12):
        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = heart(t)

        fig, ax = plt.subplots()

        ax.plot(x * scale, y * scale, color="#b266ff", linewidth=4)

        ax.set_aspect('equal')
        ax.axis("off")

        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        placeholder.pyplot(fig)
        time.sleep(0.07)
