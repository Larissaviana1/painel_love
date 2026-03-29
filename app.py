import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Para você 💜", layout="centered")

# ======================
# TEXTO SUPERIOR
# ======================
st.markdown(
    "<h2 style='text-align:center; color:white;'>Para você meu bem</h2>",
    unsafe_allow_html=True
)

placeholder = st.empty()

# ======================
# BASE DO CORAÇÃO
# ======================
t = np.linspace(0, 2*np.pi, 800)

base_x = 16 * np.sin(t)**3
base_y = (13 * np.cos(t)
          - 5 * np.cos(2*t)
          - 2 * np.cos(3*t)
          - np.cos(4*t))

# ======================
# ANIMAÇÃO
# ======================
while True:
    for scale in [1.0, 1.08, 1.15, 1.08, 1.0]:

        x = base_x * scale
        y = base_y * scale

        fig, ax = plt.subplots()

        # efeito contorno com leve brilho
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

        placeholder.pyplot(fig)
        plt.close(fig)

        time.sleep(0.12)

# ======================
# TEXTO INFERIOR
# ======================
st.markdown(
    "<h3 style='text-align:center; color:#b266ff;'>ARIEL 💜</h3>",
    unsafe_allow_html=True
)
