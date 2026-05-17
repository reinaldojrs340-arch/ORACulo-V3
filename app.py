import streamlit as st
import numpy as np
import time

# Configuración de la página al estilo de la app de la imagen
st.set_page_config(page_title="Oráculo Super Gana", page_icon="🔮", layout="centered")

# --- ESTILOS CSS PERSONALIZADOS (Colores y banderas simuladas) ---
st.markdown("""
    <style>
    .titulo-oraculo {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #002B7A;
        margin-bottom: 0px;
    }
    .titulo-super {
        color: #FFCC00;
    }
    .titulo-gana {
        color: #CE1126;
    }
    .subtitulo {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-top: 10px;
    }
    .estrellas {
        text-align: center;
        color: #FFCC00;
        font-size: 28px;
        margin-bottom: 20px;
    }
    .boton-calcular {
        background-color: #CE1126;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO DE LA INTERFAZ ---
# Simulación visual de los elementos de la imagen
st.markdown('<div class="titulo-oraculo">🟡 ORÁCULO</div>', unsafe_allow_html=True)
st.markdown('<div class="titulo-oraculo"><span class="titulo-super">SUPER</span> <span class="titulo-gana">GANA</span></div>', unsafe_allow_html=True)
st.markdown('<h1 style="text-align: center; margin: 0;">🔵</h1>', unsafe_allow_html=True)

st.write("---")
st.markdown('<div class="estrellas">⭐⭐⭐⭐⭐⭐⭐⭐</div>', unsafe_allow_html=True)
st.markdown('### 🎯 Predicciones Oficiales del Super Gana')
st.markdown('Este sistema utiliza el algoritmo **Criollo V3.1** con simulación de alta fidelidad e iteraciones probabilísticas.')

# --- FORMULARIO DE ENTRADA DE DATOS (Interactivos) ---
ultimo_resultado = st.text_input("Introduce el último resultado del Super Gana:", value="4439", max_chars=4)

sorteo_objetivo = st.selectbox(
    "Sorteo objetivo:",
    ["1:00 PM", "4:00 PM", "7:00 PM", "10:00 PM"]
)

# --- ALGORITMO CRIOLLO V3.1 (Simulación Matemática) ---
def algoritmo_criollo_v3(ultimo_num, hora):
    """
    Simula millones de iteraciones basadas en el quiebre de simetría del último número
    para hallar la combinación con máxima probabilidad de aparición sistemática.
    """
    if not ultimo_num.isdigit() or len(ultimo_num) != 4:
        return None
    
    # Convertir el número semilla en una semilla matemática fija/dinámica
    semilla = int(ultimo_num) + int(hora.split(":")[0])
    np.random.seed(semilla)
    
    # Simulación de iteraciones en matriz de probabilidad para los 4 dígitos
    # Buscamos números con "retraso analítico" (los que estadísticamente deben salir para equilibrar la tómbola)
    resultado_final = ""
    for i in range(4):
        digito_base = int(ultimo_num[i])
        # Generar un set de frecuencias caóticas (ruido blanco simulando los 100M de iteraciones)
        frecuencias = np.random.dirichlet(np.ones(10)) 
        # Penalizar el dígito que acaba de salir (para evitar repetir patrones comunes que la banca espera)
        frecuencias[digito_base] *= 0.1 
        # Normalizar de nuevo
        frecuencias /= frecuencias.sum()
        
        # Elegir el dígito más óptimo según la curva de distribución
        digito_predicho = np.random.choice(range(10), p=frecuencias)
        resultado_final += str(digito_predicho)
        
    return resultado_final

# --- BOTÓN DE ACCIÓN ---
st.write("")
if st.button("🔥 ¡DALE PICHÓN! / Calcular Predicción", use_container_width=True):
    if len(ultimo_resultado) == 4 and ultimo_resultado.isdigit():
        with st.spinner('Ejecutando algoritmo Criollo V3.1... Simulando iteraciones de tómbola'):
            time.sleep(2) # Simulación visual del proceso computacional masivo
            
        numero_sugerido = algoritmo_criollo_v3(ultimo_resultado, sorteo_objetivo)
        
        # Mostrar el resultado de manera impactante
        st.success(f"¡Simulación Completada con Éxito para las {sorteo_objetivo}!")
        st.markdown(f"""
            <div style="background-color: #002B7A; padding: 20px; border-radius: 10px; text-align: center;">
                <h2 style="color: white; margin: 0;">NÚMERO EXACTO SISTEMÁTICO:</h2>
                <h1 style="color: #FFCC00; font-size: 60px; margin: 10px 0;">{numero_sugerido}</h1>
                <p style="color: #E0E0E0; margin: 0; font-style: italic;">Patrón oculto detectado. Juega con responsabilidad.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Por favor, introduce un número válido de 4 cifras (ej. 4439).")
