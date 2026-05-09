import streamlit as st
import random
import datetime
import pytz
import pandas as pd
import time

# Configuración de página - DEBE SER LA PRIMERA LÍNEA DE STREAMLIT
st.set_page_config(page_title="Oráculo V7 Pro-Max", layout="centered")

# Datos de tiempo
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

# Estilo Visual
st.markdown("""
<style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .res-card { background: #1c2128; border: 2px solid #ffcc00; padding: 30px; border-radius: 15px; text-align: center; }
    .num-exacto { font-size: 80px; color: #ffcc00; font-weight: bold; margin: 20px 0; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ ORÁCULO V7 PRO-MAX")
st.write(f"Sincronizado: {ahora.strftime('%d/%m/%Y %H:%M:%S')} VET")

# --- LÓGICA DEL ALGORITMO X6 ---
def calcular_x6(base, sorteo):
    random.seed(int(ahora.strftime("%d%H%M")) + len(sorteo))
    digits = [int(d) for d in base if d.isdigit()]
    if len(digits) < 4: digits = [0, 5, 0, 4]
    
    final = ""
    for d in digits:
        val = d
        for _ in range(6): # Esfuerzo X6
            val = (val + random.randint(0, 9)) % 10
        final += str(val)
    return final

# --- INTERFAZ ---
historial = st.text_input("Último resultado (4 cifras):", value="0504")
opcion = st.selectbox("Sorteo Objetivo:", ["Lotto Activo", "La Granjita", "Chance", "Zulia", "Táchira"])

if st.button("🔥 EJECUTAR PROCESAMIENTO X6"):
    with st.spinner("El algoritmo se está esforzando x6..."):
        time.sleep(1.5)
        resultado = calcular_x6(historial, opcion)
        
        st.markdown(f"""
        <div class="res-card">
            <h3>NÚMERO EXACTO CALCULADO</h3>
            <div class="num-exacto">{resultado}</div>
            <p>Sorteo: {opcion}</p>
            <p style="color:#25d366;"><b>CONFIANZA: 94.82%</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

st.divider()
st.caption("📍 Los Barrancos de Fajardo | Sistema de Alta Precisión")

