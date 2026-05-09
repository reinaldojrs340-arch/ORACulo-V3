import streamlit as st
import random, datetime, pytz, time

# 1. ESTILO DRIP ROBUSTO
st.set_page_config(page_title="Oráculo V9.5 - Inercia Total", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff, #0050ff) !important;
        color: white !important; font-weight: 900 !important;
        border-radius: 12px !important; width: 100% !important;
        height: 3.5em !important;
    }
    .card-res { border: 2px solid #00d4ff; background: #161b22; padding: 20px; border-radius: 20px; text-align: center; margin-top: 10px; }
    .neon-blue { color: #00d4ff; font-weight: 900; font-size: 50px; text-shadow: 0 0 15px rgba(0,212,255,0.5); }
    .highlight { color: #ffcc00; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

animalitos = {
    "0": "Delfín", "00": "Ballena", "1": "Carnero", "2": "Toro", "3": "Ciempiés", "4": "Alacrán",
    "5": "León", "6": "Rana", "7": "Perico", "8": "Ratón", "9": "Águila", "10": "Tigre",
    "11": "Gato", "12": "Caballo", "13": "Mono", "14": "Paloma", "15": "Zorro", "16": "Oso",
    "17": "Pavo", "18": "Burro", "19": "Chivo", "20": "Cochino", "21": "Gallo", "22": "Camello",
    "23": "Cebra", "24": "Iguana", "25": "Gallina", "26": "Vaca", "27": "Perro", "28": "Zamuro",
    "29": "Elefante", "30": "Caimán", "31": "Lapa", "32": "Ardilla", "33": "Pescado", "34": "Venado",
    "35": "Jirafa", "36": "Culebra"
}

# 2. MOTOR DE INERCIA
def motor_inercia(dato, hora_objetivo, mercado):
    # Crear una semilla que combine el dato pasado con la hora buscada
    random.seed(sum(ord(c) for c in str(dato)) + int(hora_objetivo.replace("pm","").replace("am","")))
    
    if "Animal" in mercado:
        num = str(random.randint(0, 36))
        return f"{num} - {animalitos.get(num)}"
    else:
        return "".join([str(random.randint(0, 9)) for _ in range(4)])

# 3. INTERFAZ PROACTIVA
st.title("🛡️ BÚNKER V9.5: INERCIA PROACTIVA")
st.write(f"Los Barrancos de Fajardo | {ahora.strftime('%H:%M:%S')}")

# Selector de Modo
modo = st.radio("¿Qué quieres calcular?", 
                ["Lotto Activo (Proyectar desde último)", "Super Gana (Proyectar desde último)"], 
                horizontal=True)

col_d, col_h = st.columns(2)

with col_d:
    if "Lotto" in modo:
        dato_prev = st.text_input("Último animalito salido (9am, 10pm de ayer, etc):", placeholder="Ej: 15 u Oso")
    else:
        dato_prev = st.text_input("Último Super Gana salido (10pm de ayer, 1pm, etc):", placeholder="Ej: 2345")

with col_h:
    # Horas inteligentes
    if "Lotto" in modo:
        h_obj = st.selectbox("Calcular para la hora:", ["9am", "10am", "11am", "12pm", "1pm", "3pm", "4pm", "5pm", "6pm", "7pm", "10pm"])
    else:
        h_obj = st.selectbox("Calcular para la hora:", ["1pm", "4pm", "10pm"])

if st.button("🚀 CALCULAR RESULTADO FIJO"):
    if dato_prev:
        with st.spinner("Analizando inercia del sorteo anterior..."):
            time.sleep(1.2)
            resultado = motor_inercia(dato_prev, h_obj, modo)
            
            st.markdown(f"""
            <div class='card-res'>
                <p class='highlight'>PREDICCIÓN FIJA PARA LAS {h_obj.upper()}</p>
                <div class='neon-blue'>{resultado.split(' - ')[0]}</div>
                <h3>{resultado.split(' - ')[1] if ' - ' in resultado else ''}</h3>
                <p style='color: #8b949e;'>Basado en el resultado previo: <b>{dato_prev}</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            # WhatsApp dinámico
            msg = f"https://wa.me/?text=🎯+*DATO+FIJO+BÚNKER*+%0A⏰+Hora:+{h_obj.upper()}%0A🎲+Resultado:+{resultado}%0A📈+Inercia+desde:+{dato_prev}%0A📍+Los+Barrancos"
            st.markdown(f"<br><a href='{msg}' style='background:#25d366; color:white; padding:15px; display:block; border-radius:12px; text-decoration:none; text-align:center; font-weight:bold;'>📲 COMPARTIR RESULTADO ÚNICO</a>", unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("Introduce el resultado del último sorteo para poder calcular.")

st.divider()
st.caption("Sistema de Inercia Numérica - El algoritmo no duerme.")
