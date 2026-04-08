import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- CONFIGURACIÓN ---
FILE_DB = "ledger_flipping.csv"

def cargar_datos():
    if os.path.exists(FILE_DB):
        return pd.read_csv(FILE_DB)
    return pd.DataFrame(columns=["Fecha", "Proyecto", "Proveedor", "Rubro", "Monto", "Comprobante_Adjunto"])

# --- UI ---
st.set_page_config(page_title="Flipping-App Pro | Fase 3", layout="wide")
st.sidebar.title("🏢 Flipping-App Pro")
perfil = st.sidebar.radio("Vista de Usuario:", ["Socio Gestor", "Socio Inversor"])

df_actual = cargar_datos()

# --- MODO: SOCIO GESTOR (Mantenemos la carga manual funcional) ---
if perfil == "Socio Gestor":
    st.header("🏗️ Consola de Carga")
    # ... (El formulario que ya tienes funciona perfecto) ...
    st.write("Módulo de carga activo. Registra gastos para ver el impacto en Fase 3.")

# --- MODO: SOCIO INVERSOR (REFINAMIENTO FINANCIERO) ---
else:
    st.header("📊 Inteligencia de Inversión")
    
    # 1. FILTRO GLOBAL POR PROYECTO
    proyectos_disponibles = ["Todos"] + list(df_actual["Proyecto"].unique()) if not df_actual.empty else ["Todos"]
    proyecto_sel = st.sidebar.selectbox("Seleccionar Proyecto para Analizar:", proyectos_disponibles)
    
    df_filtrado = df_actual if proyecto_sel == "Todos" else df_actual[df_actual["Proyecto"] == proyecto_sel]

    # 2. DEFINICIÓN DE OBJETIVOS (Simulados por ahora)
    # En la Fase 3.2 los traeremos de una tabla de 'Proyectos'
    target_venta = st.sidebar.number_input("Precio de Venta Estimado (USD)", value=180000.0)
    presupuesto_obra = st.sidebar.number_input("Presupuesto de Obra (USD)", value=40000.0)
    costo_adquisicion = st.sidebar.number_input("Costo Adquisición (USD)", value=110000.0)

    # 3. CÁLCULOS DE RENTABILIDAD
    total_gastado_obra = df_filtrado["Monto"].sum()
    costo_total_actual = costo_adquisicion + total_gastado_obra
    roi_estimado = ((target_venta - costo_total_actual) / costo_total_actual) * 100 if costo_total_actual > 0 else 0

    # 4. DASHBOARD DE KPIs
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gasto Real en Obra", f"${total_gastado_obra:,.2f}")
    c2.metric("Inversión Total", f"${costo_total_actual:,.2f}")
    c3.metric("ROI Proyectado", f"{roi_estimado:.2f}%", delta=f"{roi_estimado - 15:.1f}% vs Target")
    c4.metric("Desvío Presupuesto", f"${total_gastado_obra - presupuesto_obra:,.2f}", delta_color="inverse")

    st.markdown("---")
    
    col_chart, col_table = st.columns([2, 1])
    with col_chart:
        st.subheader("Distribución de Gastos")
        if not df_filtrado.empty:
            st.bar_chart(df_filtrado.groupby("Rubro")["Monto"].sum())
    
    with col_table:
        st.subheader("Mayores Proveedores")
        if not df_filtrado.empty:
            st.dataframe(df_filtrado.groupby("Proveedor")["Monto"].sum().sort_values(ascending=False))
