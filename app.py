import streamlit as st
import random
import datetime
import pytz # Para asegurar la hora de Venezuela

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Oráculo Super Gana V3.1", page_icon="🇻🇪", layout="wide")

# Configurar hora de Venezuela
venezuela_tz = pytz.timezone('America/Caracas')
hora_actual = datetime.datetime.now(venezuela_tz).hour
minuto_actual = datetime.datetime.now(venezuela_tz).minute

# --- CONTROL DE CIERRE (10:00 PM a 7:00 AM) ---
# Si la hora es mayor o igual a 22 (10pm) o menor a 7 (7am)
estamos_cerrados = (hora_actual >= 22) or (hora_actual < 7)

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .header-bar { height: 15px; background: linear-gradient(90deg, #FFCC00 33%, #00247D 33%, #00247D 66%, #CF142B 66%); border-radius: 10px; margin-bottom: 20px; }
    .closed-card { background-color: #1a1a1a; color: #FFCC00; padding: 50px; border-radius: 30px; text-align: center; border: 4px solid #CF142B; margin-top: 50px; }
    .result-card { background-color: #00247D; color: #FFCC00; padding: 40px; border-radius: 30px; text-align: center; border: 4px solid #FFCC00; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
    .stButton>button { background-color: #CF142B !important; color: white !important; font-size: 20px !important; font-weight: bold !important; border-radius: 50px !important; width: 100% !important; border: 2px solid #FFCC00 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header-bar"></div>', unsafe_allow_html=True)

# --- LÓGICA DE VISUALIZACIÓN ---
if estamos_cerrados:
    st.markdown(f"""
        <div class="closed-card">
            <h1 style="font-size: 60px;">🌙 ORÁCULO EN REPOSO</h1>
            <p style="font-size: 25px;">El sistema está procesando las tendencias para el día de mañana.</p>
            <hr style="border-color: #FFCC00;">
            <p style="font-size: 20px; color: #fff;">Horario de servicio: 7:00 AM a 10:00 PM</p>
            <p style="font-size: 18px;">Vuelve temprano para las predicciones de la 1:00 PM</p>
        </div>
        """, unsafe_allow_html=True)
else:
    # --- INTERFAZ ACTIVA (De 7am a 10pm) ---
    col_t1, col_t2 = st.columns([1, 4])
    with col_t1: st.image("https://img.icons8.com/color/144/venezuela.png", width=80)
    with col_t2: 
        st.title("🇻🇪 ORÁCULO SUPER GANA V3.1")
        st.write("#### *Predicciones Activas*")

    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        ultimo = st.text_input("Último resultado:", "6416")
        horario = st.selectbox("Sorteo objetivo:", ["4:00 PM", "10:00 PM"])
    with col2:
        st.info(f"📅 **Fecha:** {datetime.datetime.now(venezuela_tz).strftime('%d/%m/%Y')}")
        st.write("🤖 **Estado:** Motor Calibrado")

    if st.button("🚀 CALCULAR PREDICCIÓN"):
        if len(ultimo) == 4 and ultimo.isdigit():
            fecha_hoy = datetime.datetime.now(venezuela_tz).strftime("%Y%m%d")
            prefijo = "16" if horario == "4:00 PM" else "22"
            random.seed(int(f"{fecha_hoy}{prefijo}"))
            
            historial = [int(d) for d in ultimo]
            res = "".join([str((h + random.randint(0, 9)) % 10) for h in historial])
            
            st.markdown(f"""
                <div class="result-card">
                    <p style="font-size: 20px;">NÚMERO SUGERIDO:</p>
                    <h1 style="font-size: 80px; margin: 0;">{res}</h1>
                    <p>¡Mucha suerte con el Super Gana!</p>
                </div>
                """, unsafe_allow_html=True)
            st.balloons()

st.divider()
st.caption("© 2026 Oráculo Super Gana - Los Barrancos de Fajardo 🇻🇪")
