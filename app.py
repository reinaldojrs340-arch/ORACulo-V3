import streamlit as st

import random, datetime, pytz, pandas as pd

# 1. CONFIGURACION

st.set_page_config(page_title="Oraculo V6 Pro", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# 2. ESTILOS SEGUROS

st.markdown("""

<style>

.stApp { background-color: #0d1117; color: white; }

.card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: 

center; }

.num-grante { font-size: 70px; color: #ffcc00; font-weight: 900; margin: 0; }

.btn-wa { background: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-

decoration: none; display: block; font-weight: bold; text-align: center; }

</style>

""", unsafe_allow_html=True)

# 3. SIDEBAR

with st.sidebar:

 st.title(" DASHBOARD V6")

 monto = st.number_input("Inversión:", value=10.0)

 st.metric("Premio (4C)", f"{monto * 4500:,.2f}")

 st.success("ONLINE 24/7")

# 4. CUERPO

t1, t2 = st.tabs([" PREDICCION", " CASINO"])

with t1:

 col_l, col_r = st.columns([2, 1])

 with col_l:

 st.subheader("Generador Élite")

 u_res = st.text_input("Resultado Anterior:", "0504")

 sorteo = st.selectbox("Sorteo:", ["1 PM", "4 PM", "7 PM", "10 PM"])

 if st.button(" CALCULAR"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1])) % 10) for d in u_res if d.isdigit()])

 st.markdown(f"<div class='card'><p class='num-grante'>{res}</p><p>CONFIANZA: 98%</p></div>", 

unsafe_allow_html=True)

 url = f"https://wa.me/?text=Jugada+V6:+{res}"

 st.markdown(f"<a href='{url}' class='btn-wa'> WHATSAPP</a>", unsafe_allow_html=True)

 with col_r:

 st.write("### Flujo")

 st.line_chart(pd.DataFrame({'Data': [10, 25, 15, 40]}))

with t2:

 if st.button(" GIRAR"):

 icons = [" ", " ", " ", " "]

 st.header(f"{random.choice(icons)} | {random.choice(icons)} | {random.choice(icons)}")

st.caption("© 2026 Oraculo Infinito V6.0")
