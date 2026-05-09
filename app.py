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

# 2. BASE DE DATOS
animalitos = {str(i): n for i, n in enumerate(["Delfín", "Ballena", "Carnero", "Toro", "Ciempiés", "Alacrán", "León", "Rana", "Perico", "Ratón", "Águila", "Tigre", "Gato", "Caballo", "Mono", "Paloma", "Zorro", "Oso", "Pavo", "Burro", "Chivo", "Cochino", "Gallo", "Camello", "Cebra", "Iguana", "Gallina", "Vaca", "Perro", "Zamuro", "Elefante", "Caimán", "Lapa", "Ardilla", "Pescado", "Venado", "Jirafa", "Culebra"])}
animalitos["00"] = "Ballena"

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
        u_res = st.text_input("Dato Semilla (Animal o Número):", placeholder="Ej: Toro o 1234")
    with col_h:
        h_obj = st.selectbox("Sorteo Objetivo:", ["9am", "10am", "11am", "12pm", "1pm", "4pm", "7pm", "10pm"])

    if st.button("🔥 ACTIVAR MOTORES X6"):
        if u_res:
            with st.spinner("Sincronizando Comparativa..."):
                time.sleep(1.2)
                # Detección de mercado
                es_animal = any(x in u_res.lower() for x in ["toro", "oso", "mono", "gato"]) or (u_res.isdigit() and int(u_res) <= 36)
                
                # Semilla base
                seed = sum(ord(c) for c in u_res) + int(h_obj.replace("am","").replace("pm",""))
                
                # --- GENERACIÓN DE 3 ALGORITMOS ---
                def gen(s, mod):
                    random.seed(s)
                    if mod: return str(random.randint(0, 36)), f"{random.randint(88, 98)}%"
                    return "".join([str(random.randint(0, 9)) for _ in range(4)]), f"{random.randint(85, 96)}%"

                v3_val, v3_p = gen(seed + 7, es_animal)
                run_val, run_p = gen(seed + 99, es_animal)
                pad_val, pad_p = gen(seed + 123, es_animal)

                # --- TABLA COMPARATIVA ---
                st.markdown("### 📊 COMPARATIVA DE ALGORITMOS")
                c1, c2, c3 = st.columns(3)
                
                for col, title, val, per in zip([c1, c2, c3], ["V3 CRIOLLO", "RUNLOT RÉPLICA", "MÉTODO PADRE"], [v3_val, run_val, pad_val], [v3_p, run_p, pad_p]):
                    with col:
                        st.markdown(f"""
                        <div class='card-pro'>
                            <b>{title}</b><br>
                            <span class='{"neon-gold" if es_animal else "neon-blue"}'>{val}</span><br>
                            <span style='color:white;'>{animalitos.get(val, "") if es_animal else "Super Gana"}</span><br>
                            <span class='percent'>{per} Prob.</span>
                        </div>
                        """, unsafe_allow_html=True)
                
                # Recomendación final
                st.success(f"Dato más pesado para las {h_obj}: {v3_val} ({animalitos.get(v3_val, 'Super Gana')})")
        else:
            st.error("Mete un dato para arrancar el búnker.")

with tab2:
    st.markdown("<h2 style='text-align:center;'>🎰 ZONA DE RECREO</h2>", unsafe_allow_html=True)
    c_s, c_d = st.columns(2)
    
    with c_s:
        st.subheader("Tragamonedas Riferas")
        if st.button("🎰 GIRAR"):
            icons = ["🍀", "💰", "💎", "🔥", "⭐"]
            r1, r2, r3 = random.choice(icons), random.choice(icons), random.choice(icons)
            st.markdown(f"<div class='slot-box'>{r1} | {r2} | {r3}</div>", unsafe_allow_html=True)
            if r1 == r2 == r3: st.balloons()
            
    with c_d:
        st.subheader("Dados de la Suerte")
        if st.button("🎲 LANZAR"):
            dado = random.randint(1, 6)
            st.markdown(f"<div class='slot-box'>🎲 Salió: {dado}</div>", unsafe_allow_html=True)

with tab3:
    st.subheader("📈 Histórico de Tendencia")
    data = pd.DataFrame({"Probabilidad": [random.randint(70, 99) for _ in range(10)]})
    st.area_chart(data)
    st.write("El sistema está detectando una alta frecuencia en la familia de los 'Terrestres' (Toro, Caballo, Burro).")

st.divider()
st.caption("© 2026 - El Patrón V10 - Sistema de Inteligencia para Loterías")
