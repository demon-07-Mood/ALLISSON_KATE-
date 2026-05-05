import streamlit as st
import random
import base64

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Para Ti", page_icon="🌸")

# 2. FUNCIÓN PARA MÚSICA (Base64 para anonimato total)
def reproducir_musica(archivo_audio):
    try:
        with open(archivo_audio, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true" loop="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# 3. ESTILO CSS Y ANONIMATO
st.markdown("""
    <style>
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none;}
    .stApp { background-color: #ffb6c1; }
    
    h1, h2, h3, p { 
        color: #8b0000 !important; 
        font-family: 'Comic Sans MS', cursive !important; 
        text-align: center;
    }
    .mensaje-card {
        background-color: rgba(255, 255, 255, 0.9); padding: 20px;
        border-radius: 20px; border: 2px solid #ff69b4;
        color: #8b0000; text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. SISTEMA DE ACCESO (CASE-INSENSITIVE)
# Según tu requerimiento, el login no debe distinguir entre mayúsculas y minúsculas
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title("🔐 Acceso Especial")
    # Usamos .lower() para que el sistema sea insensible a mayúsculas
    password = st.text_input("Introduce la palabra clave:", type="password").lower()
    
    if st.button("Entrar"):
        if password == "allisson": # Aquí puedes cambiar la clave
            st.session_state['autenticado'] = True
            st.rerun()
        else:
            st.error("Palabra clave incorrecta ❌")
else:
    # --- CONTENIDO DE LA APP (Solo se ve si el login es correcto) ---
    
    # Música y Título
    reproducir_musica("musica.mp3")
    st.title("🌸 Detalle para mi Allisson 🌸")

    # Imagen de Hello Kitty (local según image_cdb14a.png)
    st.image("hello_kity.gif", use_container_width=True)

    # Lógica de mensajes aleatorios
    try:
        with open("mensajes.txt", "r", encoding="utf-8") as f:
            mensajes = [line.strip() for line in f.readlines() if line.strip()]
    except:
        mensajes = ["Eres especial 🌸"]

    if st.button("Recibir un mensaje ❤️"):
        msg = random.choice(mensajes)
        st.markdown(f'<div class="mensaje-card">{msg}</div>', unsafe_allow_html=True)
        st.balloons()
