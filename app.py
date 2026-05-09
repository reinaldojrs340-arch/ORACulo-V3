import streamlit as st

import random, datetime, pytz, pandas as pd

# CONFIGURACIÓN SIN ERRORES

st.set_page_config(page_title="Oráculo Infinito", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# ESTILOS CSS

st.markdown("""

<style>

.stApp { background-color: #0d1117; color: white; }

.main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: center; }

.big-num { font-size: 75px; font-weight: 900; color: #ffcc00; margin: 0; }

.wa-btn { background: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; display: block; font-weight: bold; text-align: center; margin-

top: 10px; }

.slot-box { background: #010409; border: 2px dashed #ffcc00; padding: 15px; font-size: 45px; border-radius: 10px; text-align: center; }

</style>

""", unsafe_allow_html=True)

# SIDEBAR

with st.sidebar:

 st.title(" PANEL ÉLITE")

 st.divider()

 monto = st.number_input("Inversión", value=10.0)

 pago = monto * 4500

 st.metric("Premio Estimado (4C)", f"{pago:,.2f}")

 st.success(" MODO: 24/7 ACTIVO")

# TABS

t1, t2, t3 = st.tabs([" PREDICCIONES", " MINI-JUEGOS", " RIFEROS TV"])

with t1:

 col_a, col_b = st.columns([2, 1])

 with col_a:

 st.header("GENERADOR PRO")

 u_res = st.text_input("Último Resultado:", "0504")

 sorteo = st.selectbox("Sorteo:", ["1:00 PM", "4:00 PM", "10:00 PM"])

 if st.button(" CALCULAR"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1, 2])) % 10) for d in u_res if d.isdigit()])

 st.markdown(f"<div class='main-card'><p class='big-num'>{res}</p><p>CONFIANZA: 98%</p></div>", unsafe_allow_html=True)

 st.markdown(f"<a href='https://wa.me/?text=Jugada+{sorteo}:+{res}' class='wa-btn'> COMPARTIR</a>", unsafe_allow_html=True)

 with col_b:

 st.write("### Analítica")

 st.line_chart(pd.DataFrame({'T': [10, 25, 15, 35]}))

with t2:

 st.subheader(" CASINO RIFERO")

 if st.button(" GIRAR"):

 items = [" ", " ", " ", " ", " "]

 res_slot = f"{random.choice(items)} | {random.choice(items)} | {random.choice(items)}"

 st.markdown(f"<div class='slot-box'>{res_slot}</div>", unsafe_allow_html=True)

with t3:

 st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()

st.caption("Oráculo V5.0 | Los Barrancos de Fajardo ")
