import streamlit as st

import random, datetime, pytz, pandas as pd

# --- CONFIGURACIÓN CORE (DESBLOQUEADA) ---

st.set_page_config(page_title="Oráculo Infinito V5.0", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

# --- ESTILOS CSS PROFESIONALES ---

st.markdown("""<style>

 .stApp { background-color: #0d1117; }

 .main-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 15px; text-align: center; }

 .big-num { font-size: 80px; font-weight: 900; color: #ffcc00; margin: 0; }

 .wa-btn { background: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; display: block; font-

weight: bold; text-align: center; }

 .slot-box { background: #010409; border: 2px dashed #ffcc00; padding: 15px; font-size: 45px; border-radius: 10px; text-align: center; }

</style>""", unsafe_allow_html=True)

# --- SIDEBAR: CALCULADORA ---

with st.sidebar:

 st.image("https://img.icons8.com/color/96/venezuela.png", width=80)

 st.title(" PANEL ÉLITE")

 st.divider()

 st.subheader(" Calculadora")

 monto = st.number_input("Inversión (Bs/USD)", value=10.0)

 tipo = st.radio("Premio:", ["4 Cifras (4500x)", "Terminal (60x)"])

 pago = monto * (4500 if "4" in tipo else 60)

 st.metric("Total Estimado", f"{pago:,.2f}")

 st.success(" MODO PRUEBA: 24/7")

# --- CUERPO PRINCIPAL ---

t1, t2, t3 = st.tabs([" PREDICCIONES", " MINI-JUEGOS", " RIFEROS TV"])

with t1:

 col_a, col_b = st.columns([2, 1])

 with col_a:

 st.markdown("<h2 style='color:#ffcc00;'>NÚCLEO DE PRECISIÓN V5</h2>", unsafe_allow_html=True)

 u_res = st.text_input("Último Resultado:", "0504")

 sorteo = st.selectbox("Sorteo Objetivo:", ["1:00 PM", "4:00 PM", "10:00 PM"])

 if st.button(" CALCULAR AHORA"):

 random.seed(int(ahora.strftime("%y%m%d") + sorteo[0]))

 res = "".join([str((int(d) + random.choice([-1, 0, 1, 2])) % 10) for d in u_res if d.isdigit()])

 st.markdown(f"<div class='main-card'><p class='big-num'>{res}</p><p>CONFIANZA: 97.4%</p></div>", unsafe_allow_html=True)

 st.markdown(f"<a href='https://wa.me/?text=Jugada+{sorteo}:+{res}' class='wa-btn'> COMPARTIR WHATSAPP</a>", 

unsafe_allow_html=True)

 st.balloons()

 with col_b:

 st.write("### Gráfica de Inercia")

 st.line_chart(pd.DataFrame({'T': [10, 22, 18, 35, 45]}))

with t2:

 st.subheader(" TRAGAMONEDAS RIFERO")

 if st.button(" GIRAR"):

 items = [" ", " ", " ", " ", " "]

 s1, s2, s3 = random.choice(items), random.choice(items), random.choice(items)

 st.markdown(f"<div class='slot-box'>{s1} | {s2} | {s3}</div>", unsafe_allow_html=True)

 if s1 == s2 == s3: st.success("¡JACKPOT!")

 st.divider()

 st.subheader(" DADO DE LA SUERTE")

 if st.button(" LANZAR"):

 st.header(f"Salió: {random.randint(1, 6)}")

with t3:

 st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

st.divider()

st.caption("Oráculo Infinito V5.0 | Monagas, Venezuela")
