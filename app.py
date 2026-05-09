import streamlit as st
import random, datetime, pytz, time, pandas as pd

# 1. CONFIGURACIÓN DEL SISTEMA Y HORARIO
st.set_page_config(page_title="Oráculo V7 Pro-Max", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

# 2. INTERFAZ ÉLITE (DISEÑO OSCURO)
st.markdown("""
<style>
    .stApp { background-color: #0b0e11; color: #e6edf3; }
    .status-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: center; }
    .result-box { font-size: 85px; color: #ffcc00; font-weight: 900; text-shadow: 0 0 30px rgba(255,204,0,0.5); margin: 15px 0; }
    .wa-link { background: #25d366; color: white !important; padding: 15px; border-radius: 12px; text-decoration: none; display: block; font-weight: bold; font-size: 1.1rem; }
</style>
""", unsafe_allow_html=True)

# 3. MOTOR DE ESFUERZO X6 (CÁLCULO EXACTO)
def motor_robusto_x6(base_str, sorteo_name):
    resultado_final = ""
    # Semilla única basada en hora
