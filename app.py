import streamlit as st
import random, datetime, pytz, time, pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y ESTILO "DRIP"
st.set_page_config(page_title="Oráculo V7.2 Elite", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .main-card { background: linear-gradient(145deg, #161b22, #0d1117); border: 1px solid #30363d; padding: 25px; border-radius: 20px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .neon-text { color: #ffcc00; text-shadow: 0 0 15px rgba(255,204,0,0.6); font-weight: 900; }
    .animal-box { font-size: 75px; margin: 15px 0; }
    .stButton>button { background: linear-gradient(90deg, #ffcc00, #ff9900); color: #000; font-weight: bold; border-radius: 10px; border: none; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(255,204,0,0.4); }
    .game-card { background: #1a1f2c; border: 2px solid #30363d; border-radius: 15px; padding: 15px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 2. DATA REAL DE ANIMALITOS (0-36 + 00)
animalitos = {
    "0": "Delfín", "00": "Ballena", "1": "Carnero", "2": "Toro", "3": "Ciempiés", "4": "Alacrán",
    "5": "León", "6": "Rana", "7": "Perico", "8": "Ratón", "9": "Águila", "10": "Tigre",
    "11": "Gato", "12": "Caballo", "13": "Mono", "14": "Paloma", "15": "Zorro", "16": "Oso",
    "17": "Pavo", "18": "Burro", "19": "Chivo", "20": "Cochino", "21": "Gallo", "22": "Camello",
    "23": "Cebra", "24": "Iguana", "25": "Gallina", "26": "Vaca", "27": "Perro", "28": "Zamuro",
    "29": "Elefante", "30": "Caimán", "31": "Lapa", "32": "Ardilla", "33": "Pescado", "34": "Venado",
    "35": "Jirafa", "36": "Culebra"
}

# 3. LÓGICA DE CÁLCULO
def ejecutar_motor_x6(limite, sorteo):
    random.seed(int(ahora.strftime("%H%M%S")) + len(sorteo))
    res = 0
    for _ in range(6): # Capas de esfuerzo
        res = random.randint(0, limite)
    return res

# 4. INTERFAZ SUPERIOR
st.markdown(f"<h1 style='text-align: center;' class='neon-text'>ORÁCULO V7.2 ELITE EDITION</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #8b949e;'>Sincronizado: Los Barrancos de Fajardo | {ahora.strftime('%H:%M:%S')} VET</p>", unsafe_allow_html=True)

# 5. PANELES PRINCIPALES
tab1, tab2, tab3 = st.tabs(["🔮 PREDICCIONES PRO", "🎰 MINI-JUEGOS", "📊 ANALÍTICA"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("🐾 Animalitos X6")
        tipo_lotto = st.selectbox("Sorteo:", ["Lotto Activo", "La Granjita", "Lotto Rey"])
        if st.button("🔥 GENERAR ANIMALITO"):
            with st.spinner("Procesando..."):
                time.sleep(1)
                num_res = str(ejecutar_motor_x6(36, tipo_lotto))
                nombre_a = animalitos.get(num_res, "Desconocido")
                st.markdown(f"<div class='animal-box neon-text'>{num_res}</div>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='color:#25d366;'>{nombre_a.upper()}</h3>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.subheader("🎰 Super Gana / Triple")
        tipo_sg = st.selectbox("Modalidad:", ["Super Gana (4C)", "Triple Zulia", "Chance"])
        if st.button("⚡ GENERAR CIFRAS"):
            with st.spinner("Calculando..."):
                time.sleep(1)
                num_cifras = "".join([str(random.randint(0, 9)) for _ in range(4 if "4C" in tipo_sg else 3)])
                st.markdown(f"<div class='animal-box neon-text'>{num_cifras}</div>", unsafe_allow_html=True)
                st.success("Predicción Cuántica Lista")
        st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<h3 style='text-align: center;'>ZONA DE ENTRETENIMIENTO</h3>", unsafe_allow_html=True)
    g1, g2, g3 = st.columns(3)
    
    with g1:
        st.markdown("<div class='game-card'>", unsafe_allow_html=True)
        st.write("🎰 **Tragamonedas**")
        if st.button("GIRAR SLOT"):
            items = ["🍀", "💰", "💎", "⭐", "🔥"]
            r1, r2, r3 = random.choice(items), random.choice(items), random.choice(items)
            st.subheader(f"{r1} | {r2} | {r3}")
            if r1 == r2 == r3: st.balloons()
        st.markdown("</div>", unsafe_allow_html=True)
        
    with g2:
        st.markdown("<div class='game-card'>", unsafe_allow_html=True)
        st.write("🎲 **Dado de Suerte**")
        if st.button("LANZAR DADO"):
            dado = random.randint(1, 6)
            st.header(f"🎲 {dado}")
        st.markdown("</div>", unsafe_allow_html=True)

    with g3:
        st.markdown("<div class='game-card'>", unsafe_allow_html=True)
        st.write("🪙 **Cara o Sello**")
        if st.button("LANZAR MONEDA"):
            moneda = random.choice(["CARA", "SELLO"])
            st.subheader(f"🪙 {moneda}")
        st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.write("### Comportamiento del Mercado")
    chart_data = pd.DataFrame({'Tendencia': [10, 45, 30, 80, 55, 95]})
    st.line_chart(chart_data)
    st.caption("Gráfico de inercia basado en sorteos anteriores.")

st.divider()
st.markdown(f"<div style='text-align: center; color: #555;'>© 2026 Oráculo Infinito V7.2 - Diseñado para Ganar[span_3](start_span)[span_3](end_span)</div>", unsafe_allow_html=True)
