import streamlit as st
from datetime import datetime
import base64

# Configuração da página
st.set_page_config(page_title="Para você ❤️", layout="centered")

# Fundo com cor suave
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .main {
        background-color: #fff0f5;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='text-align: center; color: #ff4b6e;'>💖 Para o amor da minha vida 💖</h1>", unsafe_allow_html=True)

# Mensagem
st.markdown("""
<div style='text-align: center; font-size:18px;'>
Desde que você entrou na minha vida, tudo ficou mais bonito.<br>
Você é a minha pessoa favorita no mundo inteiro ❤️
</div>
""", unsafe_allow_html=True)

st.write("")

# Contador de tempo juntos
data_inicio = datetime(2023, 1, 1)  # ALTERA AQUI
hoje = datetime.now()
dias = (hoje - data_inicio).days

st.markdown(f"<h3 style='text-align:center;'>Estamos juntos há {dias} dias 💕</h3>", unsafe_allow_html=True)

st.write("")

# Barra de amor
st.markdown("### Nível de amor por você:")
st.progress(100)

# Fotos
st.markdown("### Nossos momentos 📸")
st.image("foto1.jpg", caption="Um dos nossos momentos favoritos")
st.image("foto2.jpg", caption="Outro dia especial")

# Playlist (opcional)
st.markdown("### Nossa música 🎶")
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g")  # pode trocar

# Rodapé
st.markdown("""
<hr>
<div style='text-align:center;'>
Feito com ❤️ só para você
</div>
""", unsafe_allow_html=True)
