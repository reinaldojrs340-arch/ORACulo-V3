import streamlit as st
import random, datetime, pytz, time, pandas as pd

# 1. CONFIGURACIÓN Y ESTILO "DRIP" PROFESIONAL
st.set_page_config(page_title="Oráculo V10 El Patrón", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stButton>button {
        background: linear-gradient(90deg, #ffcc00, #ff9900) !important;
        color: #000 !important; font-weight: 900 !important;
        border-radius: 12px !important; height: 3.5em !important; border: none !important;
    }
    .card-pro { background: #1c2128; border: 1px solid #30363d; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 10px; }
    .neon-gold { color: #ffcc00; font-weight: 900; font-size: 45px; text-shadow: 0 0 15px rgba(255,204,0,0.4); }
    .neon-blue { color: #00d4ff; font-weight: 900; font-size: 45px; }
    .percent { color: #25d366; font-weight: bold; font-size: 18px; }
    .slot-box { background: #0d1117; border: 2px gold dashed; padding: 20px; border-radius: 10px; font-size: 40px; }
</style>
""", unsafe_allow_html=True)

# 2. BASE DE DATOS CORREGIDA (MAESTRA)
# Se usa un diccionario explícito para evitar errores de conteo
animalitos = {
    "0": "Delfín", "00": "Ballena", "1": "Carnero", "2": "Toro", "3": "Ciempiés",
    "4": "Alacrán", "5": "León", "6": "Rana", "7": "Perico", "8": "Ratón",
    "9": "Águila", "10": "Tigre", "11": "Gato", "12": "Caballo", "13": "Mono",
    "14": "Paloma", "15": "Zorro", "16": "Oso", "17": "Pavo", "18": "Burro",
    "19": "Chivo", "20": "Cochino", "21": "Gallo", "22": "Camello", "23": "Cebra",
    "24": "Iguana", "25": "Gallina", "26": "Vaca", "27": "Perro", "28": "Zamuro",
    "29": "Elefante", "30": "Caimán", "31": "Lapa", "32": "Ardilla", "33": "Pescado",
    "34": "Venado", "35": "Jirafa", "36": "Culebra"
}

# 3. SIDEBAR (CALCULADORA)
with st.sidebar:
    st.markdown("<h2 style='color:#ffcc00;'>💰 CAJA CHICA</h2>", unsafe_allow_html=True)
    monto = st.number_input("Monto Apostado (Bs/USD):", min_value=1.0, value=10.0)
    opcion = st.selectbox("Tipo de Jugada:", ["Animalito (30x)", "Terminal (60x)", "Super Gana (4500x)"])
    multi = 30 if "Animal" in opcion else (60 if "Term" in opcion else 4500)
    st.metric("PAGO ESTIMADO", f"{monto * multi:,.2f}")
    st.divider()
    st.caption("📍 Los Barrancos de Fajardo | 2026")

# 4. CUERPO PRINCIPAL (TABS)
tab1, tab2, tab3 = st.tabs(["🔮 PREDICCIÓN ÉLITE", "🎰 MINI-JUEGOS", "📊 ESTADÍSTICAS"])

with tab1:
    st.markdown("<h1 style='text-align:center;'>🛡️ BÚNKER V10: EL PATRÓN</h1>", unsafe_allow_html=True)
    
    col_in, col_h = st.columns([2, 1])
    with col_in:
        u_res = st.text_input("Dato Semilla (Animal o Número):", placeholder="Ej: Toro o 17")
    with col_h:
        h_obj = st.selectbox("Sorteo Objetivo:", ["9am", "10am", "11am", "12pm", "1pm", "4pm", "7pm", "10pm"])

    if st.button("🔥 ACTIVAR MOTORES X6"):
        if u_res:
            with st.spinner("Sincronizando Comparativa..."):
                time.sleep(1.2)
                # Detección de mercado (Si es número de animalito o nombre)
                es_animal = any(x in u_res.lower() for x in ["toro", "oso", "pavo", "burro"]) or (u_res.isdigit() and int(u_res) <= 36)
                
                # Semilla base
                seed = sum(ord(c) for c in u_res) + int(h_obj.replace("am","").replace("pm","").replace("12","12"))
                
                # --- GENERACIÓN DE 3 ALGORITMOS ---
                def gen(s, mod):
                    random.seed(s)
