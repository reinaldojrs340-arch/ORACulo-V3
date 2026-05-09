import streamlit as st

import random, datetime, pytz, pandas as pd

# CONFIGURACIÓN INICIAL

st.set_page_config(page_title="Oráculo Infinito", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# ESTILOS CSS (Asegúrate de copiar esto tal cual)

st.markdown("""

<style>

.stApp { background-color: #0d1117; }

.main-card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 15px; text-align: center; }

.wa-btn { background: #25d366; color: white !important; padding: 10px; border-radius: 8px; text-decoration: none; display: block; text-align: center; 

font-weight: bold; }

.slot-box { background: #010409; border: 2px dashed #ffcc00; padding: 15px; font-size: 40px; border-radius: 10px; text-align: center; }

</style>

""", unsafe_allow_html=True)

# SIDEBAR (Calculadora)

with st.sidebar:

 st.title(" PANEL ÉLITE")

 monto = st.number_input("Inversión", value=10.0)

 tipo = st.radio("Premio:", ["4 Cifras (4500x)", "Terminal (60x)"])

 pago = monto * (4500 if "4" in tipo else 60)

 st.metric("Premio", f"{pago:,.2f}")

 st.success(" ESTADO: DESBLOQUEADO 24/7")

# CONTENIDO PRINCIPAL

t1, t2, t3 = st.tabs([" PREDICCIONES", " MINI-JUEGOS", " RIFEROS"])

with t1:

 col1, col2 = st.columns([2, 1])

 with col1:

 st.subheader("NÚCLEO DE PRECISIÓN")

 u_res = st.text_input("Último Resultado:", "0504")

 sorteo = st.selectbox("Sorteo:", ["1:00 PM", "4:00 PM", "10:00 PM"])

 if st.button(" CALCULAR"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1, 2])) % 10) for d in u_res if d.isdigit()])

 st.markdown(f"<div class='main-card'><h1 style='color:#ffcc00; font-size:70px;'>{res}</h1><p>CONFIANZA: 98%</p></div>", 

unsafe_allow_html=True)

 st.markdown(f"<a href='https://wa.me/?text=Jugada+{sorteo}:+{res}' class='wa-btn'> COMPARTIR</a>", unsafe_allow_html=True)

 with col2:

 st.write("### Tendencia")

 st.line_chart(pd.DataFrame({'T': [10, 20, 15, 30, 45]}))

with t2:

 st.subheader(" TRAGAMONEDAS")

 if st.button(" GIRAR"):

 items = [" ", " ", " ", " ", " "]

 s1, s2, s3 = random.choice(items), random.choice(items), random.choice(items)

 st.markdown(f"<div class='slot-box'>{s1} | {s2} | {s3}</div>", unsafe_allow_html=True)

with t3:

 st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.caption("© 2026 Oráculo Infinito | Los Barrancos ")
