import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Coração Pulsando", layout="centered")

st.title("❤️ Coração Pulsando")

# Função para desenhar coração
def heart(t):
    x = 16 * np.sin(t)**3
    y = (
        13 * np.cos(t)
        - 5 * np.cos(2 * t)
        - 2 * np.cos(3 * t)
        - np.cos(4 * t)
    )
    return x, y

# Placeholder para atualizar o gráfico
placeholder = st.empty()

# Loop de animação
while True:
    for scale in np.linspace(0.8, 1.2, 10):
        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = heart(t)

        fig, ax = plt.subplots()
        ax.plot(x * scale, y * scale, color="red", linewidth=3)

        ax.set_aspect('equal')
        ax.axis("off")

        placeholder.pyplot(fig)
        time.sleep(0.08)

    for scale in np.linspace(1.2, 0.8, 10):
        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = heart(t)

        fig, ax = plt.subplots()
        ax.plot(x * scale, y * scale, color="red", linewidth=3)

        ax.set_aspect('equal')
        ax.axis("off")

        placeholder.pyplot(fig)
        time.sleep(0.08)
