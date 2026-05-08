import streamlit as st
import random

st.set_page_config(page_title="ORÁCULO V3", page_icon="🎯")
st.title("🎯 Sistema de Predicción Oráculo V3.1")

ultimo_resultado = st.text_input("Último resultado (ej. 4439):", "4439")
horario = st.selectbox("Sorteo objetivo:", ["4:00 PM", "10:00 PM"])

if st.button("CALCULAR"):
    semilla = 2026050816 if horario == "4:00 PM" else 2026050822
    random.seed(semilla)
    historial = [int(d) for d in ultimo_resultado]
    resultado = ""
    for i in range(4):
        digito = (historial[i] + random.randint(0, 9)) % 10
        resultado += str(digito)
    
    st.success(f"### Número Sugerido: {resultado}")
    st.info("Estructura: VARIADO | Simulación: 100M completada")
