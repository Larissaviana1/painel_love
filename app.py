import streamlit as st

st.set_page_config(page_title="Para você 💜", layout="centered")

st.markdown("""
<style>
body {
    background-color: black;
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 80vh;
}

/* Texto rosa */
.texto {
    color: #ff4da6;
    font-size: 42px;
    margin-bottom: 40px;
}

/* Coração */
.heart {
    width: 120px;
    height: 120px;
    background-color: #b266ff;
    position: relative;
    transform: rotate(-45deg);
    animation: pulse 1s infinite;
}

/* Partes do coração */
.heart::before,
.heart::after {
    content: "";
    width: 120px;
    height: 120px;
    background-color: #b266ff;
    border-radius: 50%;
    position: absolute;
}

.heart::before {
    top: -60px;
    left: 0;
}

.heart::after {
    left: 60px;
    top: 0;
}

/* Animação */
@keyframes pulse {
    0% {
        transform: scale(1) rotate(-45deg);
    }
    50% {
        transform: scale(1.2) rotate(-45deg);
    }
    100% {
        transform: scale(1) rotate(-45deg);
    }
}
</style>

<div class="container">
    <div class="texto">Para você meu bem &lt;3</div>
    <div class="heart"></div>
</div>
""", unsafe_allow_html=True)
