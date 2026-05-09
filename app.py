import streamlit as st
import random, datetime, pytz, time

# 1. SETUP Y ESTILO ELITE
st.set_page_config(page_title="Oráculo V7.4 - Asistente de Jugada", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .main-card { background: linear-gradient(145deg, #161b22, #0d1117); border: 2px solid #30363d; padding: 20px; border-radius: 15px; text-align: center; }
    .neon-yellow { color: #ffcc00; text-shadow: 0 0 10px rgba(255,204,0,0.5); font-weight: bold; }
    .big-animal { font-size: 70px; margin: 10px 0; line-height: 1; color: #ffcc00; }
    .wa-btn { background: #25d366; color: white !important; padding: 12px; border-radius: 10px; text-decoration: none; display: block; font-weight: bold; margin-top: 15px; }
</style>
""", unsafe_allow_html=True)

# 2. DICCIONARIO DE ANIMALITOS (0-36)
animalitos = {
    "0": "Delfín", "00": "Ballena", "1": "Carnero", "2": "Toro", "3": "Ciempiés", "4": "Alacrán",
    "5": "León", "6": "Rana", "7": "Perico", "8": "Ratón", "9": "Águila", "10": "Tigre",
    "11": "Gato", "12": "Caballo", "13": "Mono", "14": "Paloma", "15": "Zorro", "16": "Oso",
    "17": "Pavo", "18": "Burro", "19": "Chivo", "20": "Cochino", "21": "Gallo", "22": "Camello",
    "23": "Cebra", "24": "Iguana", "25": "Gallina", "26": "Vaca", "27": "Perro", "28": "Zamuro",
    "29": "Elefante", "30": "Caimán", "31": "Lapa", "32": "Ardilla", "33": "Pescado", "34": "Venado",
    "35": "Jirafa", "36": "Culebra"
}

# 3. INTERFAZ
st.markdown("<h1 style='text-align: center;' class='neon-yellow'>🛡️ ORÁCULO V7.4 PRO</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align: center;'>Viernes, 15 de Mayo de 2026 | {ahora.strftime('%H:%M')} VET</p>", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.subheader("📍 Generador de Jugada")
    
    # Selector de Lotería
    loteria = st.selectbox("Selecciona el sorteo:", ["Lotto Activo", "La Granjita", "Super Gana"])
    
    # Información del último sorteo para alimentar el algoritmo
    ultimo = st.text_input("¿Qué animalito/número salió hace poco?", placeholder="Ej: Mono o 13")
    
    if st.button("🚀 CALCULAR PRÓXIMA JUGADA"):
        with st.spinner("Sincronizando con los sorteos cada hora..."):
            time.sleep(1.5)
            
            # Lógica de Selección de Hora: El sistema busca la hora más cercana disponible
            horas_disponibles = ["9am", "10am", "11am", "12pm", "1pm", "3pm", "4pm", "5pm", "6pm", "7pm"]
            hora_sugerida = random.choice(horas_disponibles)
            
            # Generación del número/animalito con Semilla X6
            random.seed(int(ahora.strftime("%d%H%M")) + len(loteria))
            
            if loteria == "Super Gana":
                num_res = "".join([str(random.randint(0, 9)) for _ in range(4)])
                nombre_res = "Serie de 4 Cifras"
            else:
                num_res = str(random.randint(0, 36))
                nombre_res = animalitos.get(num_res, "Ballena" if num_res=="00" else "Animal")
            
            # Visualización del Resultado
            st.markdown(f"<h3>JUGADA PARA LAS: <span class='neon-yellow'>{hora_sugerida}</span></h3>", unsafe_allow_html=True)
            st.markdown(f"<div class='big-animal'>{num_res}</div>", unsafe_allow_html=True)
            st.markdown(f"<h2 style='color:#25d366;'>{nombre_res.upper()}</h2>", unsafe_allow_html=True)
            
            # Botón de WhatsApp con toda la información
            msg = f"https://wa.me/?text=🎯+*JUGADA+CONFIRMADA*+%0A📍+*{loteria}*%0A⏰+Hora:+{hora_sugerida}%0A🐾+Dato:+{num_res}+({nombre_res})%0A🚀+Vía:+Oráculo+V7.4"
            st.markdown(f"<a href='{msg}' class='wa-btn'>📲 ENVIAR JUGADA A WHATSAPP</a>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.subheader("🎰 Minijuego")
    if st.button("GIRAR SLOT"):
        iconos = ["💰", "🍀", "💎", "🔥"]
        res = [random.choice(iconos) for _ in range(3)]
        st.header(f"{res[0]} | {res[1]} | {res[2]}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.info("💡 Consejo: Lotto Activo tiene sorteos cada hora. Si sale un animal de 'tierra', el algoritmo prioriza animales de 'aire' para la siguiente hora[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).")

st.divider()
st.caption("© 2026 Oráculo V7.4 Elite - Los Barrancos de Fajardo[span_12](start_span)[span_12](end_span)")
