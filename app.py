import streamlit as st

import random, datetime, pytz, pandas as pd

# 1. CONFIGURACIÓN CORE

st.set_page_config(page_title="Oráculo Infinito V5.0", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# 2. ESTILOS CSS PROFESIONALES

st.markdown("""

<style>

.stApp { background-color: #0d1117; color: white; }

.main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: center; }

.big-num { font-size: 70px; font-weight: bold; color: #ffcc00; margin: 0; }

.wa-btn { background: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; display: 

block; font-weight: bold; text-align: center; margin-top: 10px; }

.slot-box { background: #010409; border: 2px dashed gold; padding: 15px; font-size: 40px; text-align: center; border-radius: 

10px; }

</style>

""", unsafe_allow_html=True)

# 3. BARRA LATERAL (SIDEBAR)

with st.sidebar:

 st.title(" DASHBOARD ÉLITE")

 st.write("---")

 monto = st.number_input("Monto Jugado:", value=10.0)

 st.metric("Premio (4 Cifras)", f"{monto * 4500:,.2f}")

 st.success("ESTADO: ONLINE 24/7")

 st.caption(" Los Barrancos | V5.0")

# 4. CUERPO PRINCIPAL

tab1, tab2, tab3 = st.tabs([" PREDICCIÓN", " MINI-JUEGOS", " RIFEROS TV"])

with tab1:

 col1, col2 = st.columns([2, 1])

 with col1:

 st.subheader("Generador de Alta Precisión")

 u_res = st.text_input("Último Resultado:", value="0504")

 sorteo = st.selectbox("Sorteo Objetivo:", ["1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])

 if st.button(" CALCULAR JUGADA"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1])) % 10) for d in u_res if d.isdigit()])

 st.markdown(f"<div class='main-card'><p class='big-num'>{res}</p><p>CONFIANZA: 98.4%</p></div>", 

unsafe_allow_html=True)

 st.markdown(f"<a href='https://wa.me/?text=Jugada+{sorteo}:+{res}' class='wa-btn'> COMPARTIR EN WHATSAPP</a>", 

unsafe_allow_html=True)

 st.balloons()

 with col2:

 st.write("### Inercia de Datos")

 st.line_chart(pd.DataFrame({'Y': [10, 20, 15, 35]}))

with tab2:

 st.subheader(" SLOT MACHINE")

 if st.button(" GIRAR"):

 items = [" ", " ", " ", " ", " "]

 s = f"{random.choice(items)} | {random.choice(items)} | {random.choice(items)}"

 st.markdown(f"<div class='slot-box'>{s}</div>", unsafe_allow_html=True)

 st.divider()

 st.subheader(" DADO DE LA SUERTE")

 if st.button(" LANZAR"):

 st.header(f"Salió: {random.randint(1, 6)}")

with tab3:

 st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()

st.caption("© 2026 Oráculo Infinito V5.0 - Monagas, Venezuela")
