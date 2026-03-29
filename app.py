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

t = np.linspace(0, 2 * np.pi, 1000)

# Animação contínua com seno (batimento natural)
frame = 0

while True:
    scale = 1 + 0.15 * np.sin(frame)

    x, y = heart(t)

    fig, ax = plt.subplots()

    ax.plot(x * scale, y * scale, color="#b266ff", linewidth=4)

    ax.set_aspect('equal')
    ax.axis("off")

    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    placeholder.pyplot(fig)

    frame += 0.2
    time.sleep(0.03)
