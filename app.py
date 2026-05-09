import streamlit as st
import random, datetime, pytz, time

# 1. SETUP
st.set_page_config(page_title="Oráculo V9.6 - Inteligente", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

# 2. MOTOR DE PREDICCIÓN CORREGIDO
def motor_elite(dato, hora_objetivo):
    # Convertimos el dato a minúsculas para comparar
    dato_clean = str(dato).lower().strip()
    
    # LISTA DE ANIMALITOS PARA DETECCIÓN
    animales_nombres = ["delfin", "ballena", "carnero", "toro", "ciempies", "alacran", "leon", "rana", "perico", "raton", "aguila", "tigre", "gato", "caballo", "mono", "paloma", "zorro", "oso", "pavo", "burro", "chivo", "cochino", "gallo", "camello", "cebra", "iguana", "gallina", "vaca", "perro", "zamuro", "elefante", "caiman", "lapa", "ardilla", "pescado", "venado", "jirafa", "culebra"]

    # DETECCIÓN AUTOMÁTICA: ¿Es Animalito o Super Gana?
    es_animalito = False
    if dato_clean in animales_nombres or (dato_clean.isdigit() and int(dato_clean) <= 36) or dato_clean == "00":
        es_animalito = True

    # CREAR SEMILLA ÚNICA
    random.seed(sum(ord(c) for c in dato_clean) + int(hora_objetivo.replace("pm","").replace("am","")))

    if es_animalito:
        # RESULTADO DE 0 A 36 (LOTTO ACTIVO)
        num = str(random.randint(0, 36))
        return f"ANIMALITO: {num}", es_animalito
    else:
        # RESULTADO DE 4 CIFRAS (SUPER GANA)
        num = "".join([str(random.randint(0, 9)) for _ in range(4)])
        return f"SUPER GANA: {num}", es_animalito

# 3. INTERFAZ
st.title("🛡️ BÚNKER V9.6: DETECCIÓN AUTOMÁTICA")
st.write(f"Los Barrancos de Fajardo | {ahora.strftime('%H:%M:%S')}")

dato_usuario = st.text_input("Ingresa el último resultado (Animal o Número):", placeholder="Ej: Toro o 2345")
hora_sel = st.selectbox("Sorteo a calcular:", ["9am", "10am", "11am", "12pm", "1pm", "4pm", "10pm"])

if st.button("🚀 CALCULAR AHORA"):
    if dato_usuario:
        resultado, tipo = motor_elite(dato_usuario, hora_sel)
        
        with st.container():
            st.markdown(f"""
            <div style="background: #161b22; padding: 20px; border-radius: 15px; border: 2px solid {'#ffcc00' if tipo else '#00d4ff'}; text-align: center;">
                <h2 style="color: {'#ffcc00' if tipo else '#00d4ff'};">{'MODO ANIMALITO DETECTADO' if tipo else 'MODO 4 CIFRAS DETECTADO'}</h2>
                <h1 style="font-size: 80px; color: white;">{resultado.split(': ')[1]}</h1>
                <p>Predicción para las {hora_sel.upper()}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Escribe un resultado previo para iniciar el algoritmo.")
