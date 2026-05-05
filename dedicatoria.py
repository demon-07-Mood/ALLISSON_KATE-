import streamlit as st
import random
import base64

# CONFIGURACIÓN DE PÁGINA (Debe ser la primera línea)
st.set_page_config(page_title="Para Ti", page_icon="🌸")

# 1. FUNCIÓN PARA MÚSICA DE FONDO (Base64 para anonimato)
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
        pass # Si no encuentra el audio, la app sigue funcionando

# 2. BLOQUE DE ANONIMATO Y DISEÑO (CSS)
st.markdown("""
    <style>
    /* OCULTAR INTERFAZ DE STREAMLIT Y GITHUB PARA ANONIMATO */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stSidebarNav"] {display: none;}
    .st-emotion-cache-zq5wms {display: none !important;} 

    /* ESTILO VISUAL ROSA CEREZO */
    .stApp { background-color: #ffb6c1; }
    
    h1, h2, h3, p, span, label { 
        color: #8b0000 !important; 
        font-family: 'Comic Sans MS', cursive !important; 
        text-align: center;
    }

    /* BOTÓN PERSONALIZADO */
    .stButton > button {
        background-color: #ff69b4; color: white !important; 
        border-radius: 20px; border: 2px solid #8b0000; 
        width: 100%; font-weight: bold;
        height: 3em;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #ff1493;
        border-color: #ffffff;
    }

    /* CONTENEDOR DE HELLO KITTY */
    .espacio-kitty {
        display: flex; justify-content: center; padding: 10px;
    }
    
    /* TARJETA DE MENSAJE */
    .mensaje-card {
        background-color: rgba(255, 255, 255, 0.9); padding: 25px;
        border-radius: 20px; border: 2px solid #ff69b4;
        text-align: center; color: #8b0000; font-size: 1.2em;
        margin-top: 20px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. LÓGICA DE CARGA DE MENSAJES
def cargar_mensajes():
    try:
        with open("mensajes.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except:
        return ["Eres una persona muy especial 🌸"]

mensajes = cargar_mensajes()

# --- INICIO DE LA INTERFAZ ---

# Título
st.title("🌸 Algo especial para ti 🌸")

# Reproducir música (busca el archivo musica.mp3 en tu carpeta)
reproducir_musica("musica.mp3")

# Mostrar Hello Kitty (archivo local hello_kity.gif)
st.markdown('<div class="espacio-kitty">', unsafe_allow_html=True)
st.image("hello_kity.gif", width=280)
st.markdown('</div>', unsafe_allow_html=True)

# Botón interactivo
if st.button("Presiona aquí ❤️"):
    if mensajes:
        mensaje_random = random.choice(mensajes)
        st.markdown(f'<div class="mensaje-card">{mensaje_random}</div>', unsafe_allow_html=True)
        st.balloons()
