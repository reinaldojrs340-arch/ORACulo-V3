import streamlit as st
import random, datetime, pytz, time

# 1. ESTILO "BÚNKER" ROBUSTO
st.set_page_config(page_title="Oráculo V9.2 - Doble Semilla", layout="wide")
vztz = pytz.timezone('America/Caracas')
ahora = datetime.datetime.now(vztz)

st.markdown("""
<style>
    .stApp { background-color: #0b0e14; color: #e6edf3; }
    .stButton>button {
        background: linear-gradient(90deg, #ffcc00, #ff9900) !important;
        color: #000 !important; font-weight: bold !important;
        border-radius: 10px !important; width: 100% !important;
    }
    .card-future { border: 2px solid #ffcc00; background: #161b22; padding: 15px; border-radius: 15px; text-align: center; }
    .neon-gold { color: #ffcc00; font-weight: 900; font-size: 35px; text-shadow: 0 0 10px rgba(255,204,0,0.5); }
    .label-hora { color: #8b949e; font-size: 14px; font-weight: bold; }
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

# 2. MOTOR DE TENDENCIA (CRUCE DE DATOS)
def calcular_proyeccion(res_9am, res_1pm, tipo):
    # Fusionamos ambas semillas para crear una raíz matemática única
    semilla = sum(ord(c) for c in str(res_9am)) + sum(ord(c) for c in str(res_1pm))
    random.seed(semilla + int(ahora.strftime("%d%m")))
    
    pendientes = ["4pm", "5pm", "6pm", "7pm", "10pm"]
    resultados = {}
    
    for hora in pendientes:
        if tipo == "Animalitos":
            num = str(random.randint(0, 36))
            nom = animalitos.get(num, "Ballena" if num=="00" else "Animal")
            resultados[hora] = f"{num} - {nom}"
        else:
            num = "".join([str(random.randint(0, 9)) for _ in range(4)])
            resultados[hora] = num
        # Variamos la semilla para el siguiente sorteo
        random.seed(random.getrandbits(32))
        
    return resultados

# 3. INTERFAZ PRÁCTICA
st.title("🛡️ ANALIZADOR DE TENDENCIA X6")
st.write(f"Los Barrancos de Fajardo | {ahora.strftime('%H:%M:%S')} VET")

with st.container():
    col_tipo = st.radio("Selecciona el mercado:", ["Animalitos (Lotto/Granjita)", "Super Gana (4 Cifras)"], horizontal=True)
    
    c1, c2 = st.columns(2)
    with c1:
        dato_9am = st.text_input("📊 Resultado 9:00 AM:", placeholder="Ej: 14 o 5566")
    with c2:
        dato_1pm = st.text_input("📊 Resultado 1:00 PM:", placeholder="Ej: 20 o 2345")

if st.button("🔥 CALCULAR PROYECCIÓN DE TARDE Y CIERRE"):
    if dato_9am and dato_1pm:
        with st.spinner("Analizando inercia numérica entre 9am y 1pm..."):
            time.sleep(1.5)
            proyeccion = calcular_proyeccion(dato_9am, dato_1pm, "Animalitos" if "Animalitos" in col_tipo else "SuperGana")
            
            st.markdown("### 🎯 RESULTADOS PROYECTADOS")
            
            # Mostramos los resultados en una fila elegante
            cols = st.columns(len(proyeccion))
            for i, (hora, res) in enumerate(proyeccion.items()):
                with cols[i]:
                    destaque = "border-color: #ff4b2b;" if hora == "10pm" else ""
                    st.markdown(f"""
                    <div class='card-future' style='{destaque}'>
                        <span class='label-hora'>{hora.upper()}</span><br>
                        <span class='neon-gold'>{res.split(' - ')[0]}</span><br>
                        <small>{res.split(' - ')[1] if ' - ' in res else ''}</small>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Link de WhatsApp con la comparativa completa
            texto_wa = f"🎯 *PROYECCIÓN POR TENDENCIA*%0A📍 Basado en 9AM ({dato_9am}) y 1PM ({dato_1pm})%0A"
            for h, r in proyeccion.items():
                texto_wa += f"%0A⏰ *{h}:* {r}"
            
            st.markdown(f"<br><a href='https://wa.me/?text={texto_wa}' style='background:#25d366; color:white; padding:15px; display:block; border-radius:10px; text-decoration:none; text-align:center; font-weight:bold;'>📲 ENVIAR HOJA DE RUTA A GRUPOS</a>", unsafe_allow_html=True)
    else:
        st.error("Debes ingresar ambos resultados (9am y 1pm) para activar el análisis de tendencia.")

st.divider()
st.caption("© 2026 Oráculo Pro - Algoritmo de Doble Semilla para Cierre de Jornada.")
