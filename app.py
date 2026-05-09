import streamlit as st

import random, datetime, pytz, time, pandas as pd

st.set_page_config(page_title="Oráculo V7 Pro-Max", layout="wide")

vztz = pytz.timezone('America/Caracas')

ahora = datetime.datetime.now(vztz)

st.markdown("""<style>

.stApp { background-color: #0b0e11; color: #e6edf3; }

.card { background: #161b22; border: 1px solid #30363d; padding: 20px; border-radius: 15px; text-align: center; }

.big-num { font-size: 80px; color: #ffcc00; font-weight: 900; }

.wa-link { background: #25d366; color: white !important; padding: 15px; border-radius: 12px; text-decoration: 

none; display: block; font-weight: bold; }

</style>""", unsafe_allow_html=True)

with st.sidebar:

 st.title(" CONTROL CENTER V7")

 inv = st.number_input("Monto:", value=10.0)

 st.metric("PREMIO (4C)", f"{inv * 4500:,.2f}")

 st.progress(99, text="X6 Engine Active")

 st.caption(" Los Barrancos de Fajardo")

def motor_x6(base, sorteo):

 res = ""

 random.seed(int(ahora.strftime("%y%m%d%H")) + len(sorteo))

 digits = [int(d) for d in base if d.isdigit()]

 if len(digits) < 4: digits = [0, 5, 0, 4]

 for d in digits:

 temp = d

 for _ in range(6):

 temp = (temp + random.randint(0, 9) * random.choice([1, -1])) % 10

 res += str(temp)

 return res

t1, t2 = st.tabs([" INFERENCIA", " JUEGOS"])

with t1:

 col1, col2 = st.columns([3, 2])

 with col1:

 hist = st.text_input("Último Ganador (4 cifras):", "0504")

 target = st.selectbox("Sorteo:", ["Lotto Activo", "La Granjita", "Chance", "Zulia"])

 if st.button(" EJECUTAR X6"):

 with st.spinner('Procesando...'):

 time.sleep(1)

 num = motor_x6(hist, target)

 st.markdown(f"""<div class='card'><h3>NÚMERO EXACTO</h3><div class='big-num'>{num}</div>

 <a href='https://wa.me/?text=V7+PRO+{target}:+{num}' class='wa-link'> WHATSAPP</a></div>""", 

unsafe_allow_html=True)

 with col2:

 st.area_chart(pd.DataFrame({'Prob': [10, 45, 30, 80, 55, 95]}))

with t2:

 if st.button(" SLOT"):

 e = [" ", " ", " ", " "]

 st.header(f"{random.choice(e)} | {random.choice(e)} | {random.choice(e)}")

st.caption("Oráculo V7.0 | Monagas | 2026")
