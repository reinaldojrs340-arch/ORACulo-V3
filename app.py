import streamlit as st
import random, datetime, pytz, time

# 1. SETUP Y ESTILO PROFESIONAL
st.set_page_config(page_title="Oráculo V8.5 - Modo Seguimiento", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b1117; color: #e6edf3; }
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff, #0050ff) !important;
        color: white !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 3em !important; width: 100% !important;
    }
    .status-past { background: #1c2128; border: 1px solid #30363d; padding: 15px; border-radius: 10px; opacity: 0.6; }
    .status-future { background: #161b22; border: 2px solid #00d4ff; padding: 15px; border-radius: 15px; text-align: center; box-shadow: 0 0 15px rgba(0, 212, 255, 0.1); }
    .neon-blue { color: #00d4ff; text-shadow: 0 0 5px rgba(0,212,255,0.5); font-weight: bold; }
    .res-val { font-size: 45px; font-weight: 900; color: #ffffff; }
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

# 2. MOTOR DE PREDICCIÓN EN CADENA
def generar_cadena_pendiente(ultimo_res, tipo):
    random.seed(sum(ord(c) for c in str(ultimo_res)) + int(ahora.strftime("%d%m")))
    pendientes = ["4pm", "5pm", "6pm", "7pm", "10pm"]
    resultados = {}
    
    for hora in pendientes:
        if tipo == "Animalitos":
            num = str(random.randint(0, 36))
            nom = animalitos.get(num, "Ballena" if num=="00" else "Animal")
            resultados[hora] = f"{num} ({nom})"
        else: # Super Gana
            num = "".join([str(random.randint(0, 9)) for _ in range(4)])
            resultados[hora] = num
        # Alterar semilla para el siguiente de la cadena
        random.seed(random.randint(1, 9999))
    return resultados

# 3. INTERFAZ PRÁCTICA
st.markdown("<h1 style='text-align:center;'>🛡️ ORÁCULO V8.5: PANEL DE PENDIENTES</h1>", unsafe_allow_html=True)
st.write(f"<p style='text-align:center;'>Sincronizado: Los Barrancos de Fajardo | {ahora.strftime('%H:%M:%S')}</p>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        tipo_juego = st.radio("Tipo de Juego:", ["Animalitos", "Super Gana"], horizontal=True)
    with col2:
        ultimo_dato = st.text_input("Resultado de la 1:00 PM:", placeholder="Ej: 2345 o Mono")

if st.button("🔍 CALCULAR SORTEOS RESTANTES"):
    if ultimo_dato:
        with st.spinner("Procesando secuencia de cierre..."):
            time.sleep(1)
            predicciones = generar_cadena_pendiente(ultimo_dato, tipo_juego)
            
            # Mostrar el pasado (informativo)
            st.markdown("<div class='status-past'>✅ Sorteo 1:00 PM: <b>" + ultimo_dato + "</b> (Completado)</div>", unsafe_allow_html=True)
            
            st.markdown("### ⏳ PROYECCIÓN DE CIERRE (SORTEOS PENDIENTES)")
            
            # Mostrar el futuro en columnas
            cols = st.columns(len(predicciones))
            for i, (hora, res) in enumerate(predicciones.items()):
                with cols[i]:
                    color = "#ff4b2b" if hora == "10pm" else "#00d4ff"
                    st.markdown(f"""
                    <div class='status-future' style='border-color: {color};'>
                        <p class='neon-blue' style='color: {color};'>{hora.upper()}</p>
                        <div class='res-val'>{res.split(' ')[0]}</div>
                        <small>{res.split(' ')[1] if '(' in res else ''}</small>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Botón de compartir consolidado
            msg = f"https://wa.me/?text=🎯+*PROYECCIÓN+CIERRE+BÚNKER*+%0A📍+Basado+en+1PM:+{ultimo_dato}%0A"
            for h, r in predicciones.items():
                msg += f"%0A⏰+{h}:+{r}"
            
            st.markdown(f"<br><a href='{msg}' style='background:#25d366; color:white; padding:15px; display:block; border-radius:10px; text-decoration:none; text-align:center; font-weight:bold;'>📲 COMPARTIR HOJA DE RUTA EN WHATSAPP</a>", unsafe_allow_html=True)
    else:
        st.warning("Introduce el resultado de la 1:00 PM para proyectar el resto del día[span_2](start_span)[span_2](end_span).")

st.divider()
st.caption("© 2026 Sistema de Encadenamiento Probabilístico - Los Barrancos de Fajardo[span_3](start_span)[span_3](end_span).")
