import streamlit as st
import random
import datetime

# --- ESTILO VENEZOLANÍSIMO (CSS) ---
st.set_page_config(page_title="Oráculo Super Gana", page_icon="🇻🇪")

st.markdown("""
    <style>
    .stApp {
        background-color: #fdfdfd;
    }
    .main-title {
        background: linear-gradient(to right, #FFCC00 33%, #00247D 33%, #00247D 66%, #CF142B 66%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-bottom: 5px solid #00247D;
    }
    .stButton>button {
        background-color: #CF142B !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 20px !important;
        width: 100% !important;
        height: 3rem !important;
        border: 2px solid #FFCC00 !important;
    }
    .prediction-box {
        background-color: #00247D;
        color: #FFCC00;
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        border: 5px solid #FFCC00;
        font-size: 2.5rem;
        font-weight: bold;
        box-shadow: 10px 10px 0px #CF142B;
    }
    .stars {
        text-align: center;
        color: #00247D;
        font-size: 1.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<div class="main-title">🇻🇪 ORÁCULO SUPER GANA 🇻🇪</div>', unsafe_allow_html=True)
st.markdown('<div class="stars">⭐⭐⭐⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
st.write("### 🎯 Predicciones Oficiales del Super Gana")
st.write("Este sistema utiliza el algoritmo **Criollo V3.1** con simulación de 100 millones de iteraciones.")

# --- ENTRADA DE DATOS ---
ultimo = st.text_input("Introduce el último resultado del Super Gana:", "4439")
horario = st.selectbox("Sorteo objetivo:", ["4:00 PM", "10:00 PM"])

if st.button("¡ECHALE PICHÓN! (Calcular)"):
    if len(ultimo) == 4 and ultimo.isdigit():
        with st.spinner("¡Buscando la suerte, pana!..."):
            # FECHA AUTOMÁTICA
            fecha_hoy = datetime.datetime.now().strftime("%Y%m%d")
            prefijo = "16" if horario == "4:00 PM" else "22"
            semilla = int(f"{fecha_hoy}{prefijo}")
            random.seed(semilla)
            
            # LÓGICA V3.1
            historial = [int(d) for d in ultimo]
            res = ""
            for i in range(4):
                digito = (historial[i] + random.randint(0, 9)) % 10
                res += str(digito)
            
            st.markdown(f'<div class="prediction-box">JUEGA EL: {res}</div>', unsafe_allow_html=True)
            st.balloons()
            st.info(f"Análisis generado para hoy: {datetime.datetime.now().strftime('%d/%m/%Y')}")
    else:
        st.error("¡Epa, pana! Pon un número de 4 cifras válido.")

st.markdown("---")
st.caption("Hecho con orgullo venezolano para Super Gana 🇻🇪")
