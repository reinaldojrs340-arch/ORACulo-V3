import streamlit as st

import random, datetime, pytz

# CONFIGURACION BASICA

st.set_page_config(page_title="Oraculo V6", layout="centered")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

st.title(" ORÁCULO V6.0")

st.write("---")

# ENTRADAS DE DATOS

u_res = st.text_input("Último Resultado:", "0504")

sorteo = st.selectbox("Sorteo:", ["1 PM", "4 PM", "7 PM", "10 PM"])

if st.button("CALCULAR JUGADA"):

 # Generador de lógica simple para evitar errores

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.randint(0, 2)) % 10) for d in u_res if d.isdigit()])

 st.success(f"NÚMERO SUGERIDO: {res}")

 st.balloons()

st.write("---")

st.caption("Los Barrancos de Fajardo | Monagas")
