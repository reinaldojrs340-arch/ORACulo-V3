import streamlit as st
import random, datetime, pytz, time

# 1. CONFIGURACIÓN Y ESTILO DRIP ROBUSTO
st.set_page_config(page_title="Oráculo Multi-Sorteo V9", layout="wide")
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
    .card-lotto { border-left: 5px solid #ffcc00; background: #161b22; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .card-super { border-left: 5px solid #00d4ff; background: #161b22; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .neon-gold { color: #ffcc00; font-weight: 900; font-size: 25px; }
    .neon-blue { color: #00d4ff; font-weight: 900; font-size: 25px; }
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

# 2. MOTORES DE CÁLCULO
def motor_lotto_activo(dato_base):
    # Sorteos cada hora de 9am a 7pm + 10pm (Total 11 sorteos)
    horas = ["9am", "10am", "11am", "12pm", "1pm", "3pm", "4pm", "5pm", "6pm", "7pm", "10pm"]
    random.seed(sum(ord(c) for c in str(dato_base)) + int(ahora.strftime("%d")))
    resultados = {}
    for h in horas:
        num = str(random.randint(0, 36))
        resultados[h] = f"{num} - {animalitos.get(num)}"
    return resultados

def motor_super_gana(dato_base):
    # Solo 3 sorteos a partir de la 1pm
    horas = ["1pm", "4pm", "10pm"]
    random.seed(sum(ord(c) for c in str(dato_base)) + 99)
    resultados = {}
    for h in horas:
        num = "".join([str(random.randint(0, 9)) for _ in range(4)])
        resultados[h] = num
    return resultados

# 3. INTERFAZ
st.title("🛡️ PANEL INTEGRAL DE SORTEOS")
st.write(f"Los Barrancos de Fajardo | {ahora.strftime('%d/%m/%Y')}")

col_config1, col_config2 = st.columns(2)
with col_config1:
    entrada_lotto = st.text_input("Dato semilla para Lotto Activo:", placeholder="Ej: 05 o Perro")
with col_config2:
    entrada_super = st.text_input("Dato semilla para Super Gana:", placeholder="Ej: 1234")

if st.button("🔥 GENERAR JORNADA COMPLETA"):
    if entrada_lotto and entrada_super:
        with st.spinner("Calculando ciclos X6..."):
            time.sleep(1)
            res_lotto = motor_lotto_activo(entrada_lotto)
            res_super = motor_super_gana(entrada_super)
            
            c1, c2 = st.columns(2)
            
            with c1:
                st.subheader("🐾 LOTTO ACTIVO (9AM - 10PM)")
                for hora, val in res_lotto.items():
                    color_hora = "#ffcc00" if hora == "10pm" else "#ffffff"
                    st.markdown(f"""
                    <div class='card-lotto'>
                        <b style='color:{color_hora}'>{hora.upper()}</b><br>
                        <span class='neon-gold'>{val}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            with c2:
                st.subheader("🎰 SUPER GANA (3 SORTEOS)")
                for hora, val in res_super.items():
                    st.markdown(f"""
                    <div class='card-super'>
                        <b style='color:#00d4ff'>{hora.upper()}</b><br>
                        <span class='neon-blue'>{val}</span>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.balloons()
    else:
        st.warning("Por favor, llena ambas semillas para calcular.")

st.divider()
st.caption("Sistema de predicción horaria optimizado - V9")
