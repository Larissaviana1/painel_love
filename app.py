import streamlit as st

st.markdown("""
<style>
.heart {
  animation: pulse 1s infinite;
  font-size: 120px;
  text-align: center;
}

@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.4); }
  100% { transform: scale(1); }
}
</style>

<div class="heart">❤️</div>
""", unsafe_allow_html=True)
