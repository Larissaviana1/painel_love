import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Para você ❤️", layout="centered")

st.markdown("<h2 style='text-align:center;'>Para você 💖</h2>", unsafe_allow_html=True)

placeholder = st.empty()

# grid
size = 30
x = np.linspace(-1.5, 1.5, size)
y = np.linspace(-1.5, 1.5, size)

X, Y = np.meshgrid(x, y)

# equação do coração
heart = (X**2 + Y**2 - 1)**3 - X**2 * Y**3 <= 0

for frame in range(1000):
    html = "<div style='text-align:center; line-height:1;'>"

    for i in range(size):
        for j in range(size):
            if heart[i][j]:
                
                # efeito de animação (batendo)
                if (i + j + frame) % 6 < 3:
                    html += "<span style='font-size:16px;'>❤️</span>"
                else:
                    html += "<span style='font-size:16px;'>💖</span>"
            else:
                html += "<span style='font-size:16px;'>⠀</span>"

        html += "<br>"

    html += "</div>"

    placeholder.markdown(html, unsafe_allow_html=True)
    time.sleep(0.15)

st.markdown(
    "<h3 style='text-align:center;'>Eu te amo 💕</h3>",
    unsafe_allow_html=True
)
