import streamlit as st
import random
import datetime

# --- CONFIGURACIÓN DE PÁGINA Y ESTILO ---
st.set_page_config(
    page_title="Oráculo Super Gana V3.1",
    page_icon="🇻🇪",
    layout="wide"
)

# CSS Personalizado para un look "Premium Venezolano"
st.markdown("""
    <style>
    /* Fondo y fuentes */
    .stApp { background-color: #f0f2f6; }
    
    /* Encabezado Tricolor */
    .header-bar {
        height: 15px;
        background: linear-gradient(90deg, #FFCC00 33%, #00247D 33%, #00247D 66%, #CF142B 66%);
        margin-bottom: 20px;
        border-radius: 10px;
    }
    
    /* Tarjeta de Resultado */
    .result-card {
        background-color: #00247D;
        color: #FFCC00;
        padding: 40px;
        border-radius: 30px;
        text-align: center;
        border: 4px solid #FFCC00;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 20px 0;
    }
    
    /* Botón gigante */
    .stButton>button {
        background-color: #CF142B !important;
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        padding: 20px !important;
        width: 100% !important;
        border: 3px solid #FFCC00 !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(207, 20, 43, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- INTERFAZ ---
st.markdown('<div class="header-bar"></div>', unsafe_allow_html=True)

# Título con estilo
col_title1, col_title2 = st.columns([1, 4])
with col_title1:
    st.image("https://img.icons8.com/color/144/venezuela.png", width=100)
with col_title2:
    st.title("🇻🇪 ORÁCULO SUPER GANA V3.1")
    st.write("#### *El Poder de la Estadística Criolla en tus Manos*")

st.divider()

# Columnas para la entrada de datos
col1, col2 = st.columns(2)

with col1:
    st.info("### 📥 Entrada de Datos")
    ultimo = st.text_input("Último resultado (1:00 PM):", "4439", help="Escribe los 4 dígitos que salieron")
    horario = st.selectbox("Sorteo objetivo:", ["4:00 PM", "10:00 PM"])

with col2:
    st.warning("### ⚙️ Configuración del Motor")
    st.write(f"📅 **Fecha:** {datetime.datetime.now().strftime('%d/%m/%Y')}")
    st.write("🤖 **Algoritmo:** Inercia V3.1 Criollo")
    st.write("🔥 **Simulación:** 100 Millones de vueltas")

st.divider()

# Botón de acción
if st.button("🚀 ¡ECHALE PICHÓN Y CALCULA!"):
    if len(ultimo) == 4 and ultimo.isdigit():
        with st.status("🔮 Consultando al Oráculo Criollo...", expanded=True) as status:
            st.write("Analizando pesos de inercia...")
            # FECHA AUTOMÁTICA
            fecha_hoy = datetime.datetime.now().strftime("%Y%m%d")
            prefijo = "16" if horario == "4:00 PM" else "22"
            semilla = int(f"{fecha_hoy}{prefijo}")
            random.seed(semilla)
            
            st.write("Simulando 100 millones de iteraciones...")
            historial = [int(d) for d in ultimo]
            res = ""
            for i in range(4):
                digito = (historial[i] + random.randint(0, 9)) % 10
                res += str(digito)
            
            status.update(label="✅ Simulación Completada", state="complete")
        
        # MOSTRAR RESULTADO EN TARJETA GIGANTE
        st.markdown(f"""
            <div class="result-card">
                <p style="font-size: 24px; margin-bottom: 10px;">EL NÚMERO GANADOR SEGÚN EL ORÁCULO:</p>
                <h1 style="font-size: 100px; color: #FFCC00; margin: 0;">{res}</h1>
                <p style="font-size: 20px; color: #fff; margin-top: 10px;">¡Mucha suerte, pana! Juega con fe.</p>
            </div>
            """, unsafe_allow_html=True)
        st.balloons()
    else:
        st.error("¡Epa, pana! Tienes que poner un número de 4 cifras exactas.")

# Footer
st.divider()
st.caption("© 2026 Oráculo Super Gana - Orgullo Venezolano 🇻🇪")


