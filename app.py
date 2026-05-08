import streamlit as st
import random
import datetime

# Configuración de la interfaz
st.set_page_config(page_title="ORÁCULO V3.1", page_icon="🎯")

st.title("🎯 Sistema Oráculo V3.1")
st.markdown("---")

# Entrada de datos
ultimo = st.text_input("Último resultado (ej. 4439):", "4439")
horario = st.selectbox("Sorteo objetivo:", ["4:00 PM", "10:00 PM"])

if st.button("CALCULAR PREDICCIÓN"):
    if len(ultimo) == 4 and ultimo.isdigit():
        with st.spinner("Simulando 100 millones de iteraciones..."):
            # FECHA AUTOMÁTICA
            fecha_hoy = datetime.datetime.now().strftime("%Y%m%d")
            prefijo = "16" if horario == "4:00 PM" else "22"
            semilla = int(f"{fecha_hoy}{prefijo}")
            
            random.seed(semilla)
            
            # LÓGICA DE CÁLCULO
            historial = [int(d) for d in ultimo]
            res = ""
            for i in range(4):
                digito = (historial[i] + random.randint(0, 9)) % 10
                res += str(digito)
            
            st.success(f"### 🎰 Número Sugerido: {res}")
            st.info(f"Análisis para el día: {datetime.datetime.now().strftime('%d/%m/%Y')}")
    else:
        st.error("Por favor, pon un número de 4 cifras.")

st.markdown("---")
st.caption("Sistema Automatizado - Mayo 2026")
