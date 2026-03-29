import streamlit as st

st.set_page_config(page_title="Para você ❤️", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0a0a0a;
    color: white;
    text-align: center;
}

.container {
    margin-top: 100px;
}

.heart {
    font-size: 120px;
    animation: pulse 1.2s infinite;
    color: #ff4d6d;
    text-shadow: 0 0 20px #ff4d6d, 0 0 40px #ff4d6d;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}

.texto {
    font-size: 28px;
    margin-top: 30px;
    animation: fadeIn 3s ease-in-out;
}

.subtexto {
    font-size: 18px;
    margin-top: 15px;
    color: #ccc;
    animation: fadeIn 5s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
</style>

<div class="container">
    <div class="heart">❤️</div>
    <div class="texto">Eu te amo 💖</div>
    <div class="subtexto">Cada momento com você é especial</div>
</div>
""", unsafe_allow_html=True)
