import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURACIÓN PRO ---
st.set_page_config(page_title="Flipping-App Pro", layout="wide")

# Inicialización de "Base de Datos" temporal
if 'db_gastos' not in st.session_state:
    st.session_state.db_gastos = pd.DataFrame(columns=[
        "Fecha", "Proyecto", "Proveedor", "Categoría", "Monto", "OCR_Status"
    ])

# --- NAVEGACIÓN (ROLES) ---
st.sidebar.title("🏗️ Flipping-App Pro")
perfil = st.sidebar.radio("Entrar como:", ["Socio Gestor (Obra)", "Socio Inversor (Reportes)"])

# --- MODO: SOCIO GESTOR ---
if perfil == "Socio Gestor (Obra)":
    st.header("🏗️ Gestión de Obra y Gastos")
    
    with st.expander("➕ Cargar Nuevo Gasto / Scan OCR", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            uploaded_file = st.file_uploader("Subir foto de ticket/factura", type=['jpg', 'png', 'pdf'])
            if uploaded_file:
                st.info("Simulando procesamiento OCR... Extraído: $45,200.00") # Aquí conectaremos la IA luego
        
        with col2:
            with st.form("form_gasto"):
                proyecto = st.selectbox("Proyecto", ["Palermo PH", "Belgrano Depto"])
                prov = st.text_input("Proveedor")
                cat = st.selectbox("Rubro", ["Materiales", "Mano de Obra", "Permisos", "Varios"])
                monto = st.number_input("Monto Final ($)", min_value=0.0)
                submit = st.form_submit_button("Confirmar e Impactar")
                
                if submit:
                    nuevo = pd.DataFrame([[datetime.now().date(), proyecto, prov, cat, monto, "Manual/OCR"]], 
                                         columns=st.session_state.db_gastos.columns)
                    st.session_state.db_gastos = pd.concat([st.session_state.db_gastos, nuevo], ignore_index=True)
                    st.success("Gasto registrado con éxito.")

    st.subheader("📋 Ledger de la Obra")
    st.dataframe(st.session_state.db_gastos, use_container_width=True)

# --- MODO: SOCIO INVERSOR ---
else:
    st.header("📊 Dashboard del Socio Inversor")
    
    # KPIs de alto nivel
    presupuesto_total = 120000.00 # Ejemplo
    gastado = st.session_state.db_gastos["Monto"].sum()
    disponible = presupuesto_total - gastado
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Presupuesto Obra", f"${presupuesto_total:,.2f}")
    c2.metric("Total Invertido", f"${gastado:,.2f}", delta=f"{gastado/presupuesto_total:.1%}")
    c3.metric("Margen de Seguridad", f"${disponible:,.2f}")

    if not st.session_state.db_gastos.empty:
        st.subheader("Desglose por Rubro")
        st.bar_chart(st.session_state.db_gastos.groupby("Categoría")["Monto"].sum())
