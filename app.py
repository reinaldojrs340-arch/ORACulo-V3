import streamlit as st

import random

import datetime

import pytz

# CONFIGURACION BASICA

st.set_page_config(page_title="Oraculo V5", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# INTERFAZ

st.title(" ORÁCULO V5.0 - UNLOCKED")

st.write("---")

# PREDICCION

u_res = st.text_input("Ultimo Resultado (4 cifras):", "0504")

sorteo = st.selectbox("Sorteo:", ["1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])

if st.button("GENERAR PREDICCION"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1])) % 10) for d in u_res if 

d.isdigit()])

 st.subheader(f"NUMERO SUGERIDO: {res}")

 st.success("Prediccion generada con exito")

st.write("---")

# MINI JUEGO

st.subheader(" SLOT MINI-GAME")

if st.button("GIRAR SLOT"):

 iconos = [" ", " ", " ", " "]

 resultado = f"{random.choice(iconos)} | {random.choice(iconos)} | 

{random.choice(iconos)}"

 st.header(resultado)

st.divider()

st.caption("Oraculo Infinito V5.0 - Monagas")
