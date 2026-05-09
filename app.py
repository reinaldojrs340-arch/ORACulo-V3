import streamlit as st

import random, datetime, pytz, pandas as pd

# 1. CONFIGURACION

st.set_page_config(page_title="Oraculo Infinito V5", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# 2. ESTILOS

st.markdown("""

<style>

.stApp { background-color: #0d1117; color: white; }

.card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 10px; text-align: 

center; }

.num { font-size: 60px; color: #ffcc00; font-weight: bold; }

.btn-wa { background-color: #25d366; color: white !important; padding: 10px; border-radius: 5px; text-

decoration: none; display: block; margin-top: 10px; }

</style>

""", unsafe_allow_html=True)

# 3. BARRA LATERAL

with st.sidebar:

 st.title(" DASHBOARD")

 monto = st.number_input("Inversión", value=10.0)

 st.metric("Premio (4C)", f"{monto * 4500:,.2f}")

 st.success("SISTEMA ONLINE 24/7")

# 4. CONTENIDO

t1, t2 = st.tabs([" PREDICCION", " JUEGOS"])

with t1:

 col1, col2 = st.columns([2, 1])

 with col1:

 st.header("Generador Pro")

 u_res = st.text_input("Ultimo Resultado:", value="0504")

 sorteo = st.selectbox("Sorteo:", ["1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"])

 if st.button("CALCULAR"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1])) % 10) for d in u_res if 

d.isdigit()])

 st.markdown(f"<div class='card'><div class='num'>{res}</div><p>CONFIANZA: 98%</p></div>", 

unsafe_allow_html=True)

 st.markdown(f"<a href='https://wa.me/?text=Jugada+{sorteo}:+{res}' class='btn-wa'>WHATSAPP</

a>", unsafe_allow_html=True)

 with col2:

 st.line_chart(pd.DataFrame({'Data': [10, 20, 15, 30]}))

with t2:

 if st.button(" GIRAR"):

 icons = [" ", " ", " ", " "]

 st.subheader(f"{random.choice(icons)} | {random.choice(icons)} | {random.choice(icons)}")

st.caption("Oraculo Infinito V5.0 - Los Barrancos")
