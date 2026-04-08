import streamlit as st
import pandas as pd
from datetime import datetime
import os

# --- CONFIGURACIÓN DE AMBIENTE ---
FILE_DB = "ledger_flipping.csv"

def cargar_datos():
    if os.path.exists(FILE_DB):
        return pd.read_csv(FILE_DB)
    return pd.DataFrame(columns=["Fecha", "Proyecto", "Proveedor", "Rubro", "Monto", "Comprobante_Adjunto"])

def guardar_gasto(nueva_fila):
    df = cargar_datos()
    df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)
    df.to_csv(FILE_DB, index=False)

# --- UI CONFIG ---
st.set_page_config(page_title="Flipping-App Pro", layout="wide", initial_sidebar_state="expanded")

# --- NAVEGACIÓN ---
st.sidebar.title("🏢 Flipping-App Pro")
st.sidebar.markdown("---")
perfil = st.sidebar.radio("Vista de Usuario:", ["Socio Gestor (Obra)", "Socio Inversor (Dashboard)"])

# --- MODO: SOCIO GESTOR ---
if perfil == "Socio Gestor (Obra)":
    st.header("🏗️ Consola de Gestión de Obra")
    st.info("Registra los gastos y adjunta el comprobante para auditoría.")

    with st.form("form_carga_manual", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            fecha = st.date_input("Fecha del Gasto", datetime.now())
            proyecto = st.selectbox("Proyecto Seleccionado", ["Palermo PH", "Belgrano Depto", "Recoleta Studio"])
            proveedor = st.text_input("Nombre del Proveedor / Comercio")
        
        with col2:
            rubro = st.selectbox("Categoría / Rubro", ["Materiales", "Mano de Obra", "Impuestos/Tasas", "Honorarios Professionales", "Varios"])
            monto = st.number_input("Monto Total ($)", min_value=0.0, format="%.2f")
            adjunto = st.file_uploader("Adjuntar Comprobante (Opcional)", type=["jpg", "png", "pdf"])

        btn_registrar = st.form_submit_button("🔨 Registrar Gasto en Ledger")

    if btn_registrar:
        if monto > 0 and proveedor:
            nuevo_gasto = {
                "Fecha": fecha.strftime("%Y-%m-%d"),
                "Proyecto": proyecto,
                "Proveedor": proveedor,
                "Rubro": rubro,
                "Monto": monto,
                "Comprobante_Adjunto": adjunto.name if adjunto else "Sin adjunto"
            }
            guardar_gasto(nuevo_gasto)
            st.success(f"✅ Gasto de ${monto:,.2f} registrado en {proyecto}.")
        else:
            st.warning("⚠️ Por favor, ingresa un monto válido y el nombre del proveedor.")

    st.markdown("---")
    st.subheader("📋 Últimos movimientos registrados")
    st.dataframe(cargar_datos().tail(10), use_container_width=True)

# --- MODO: SOCIO INVERSOR ---
else:
    st.header("📊 Dashboard de Control de Inversión")
    df_actual = cargar_datos()
    
    # Simulación de Presupuesto Inicial (Esto luego vendrá de una tabla de Proyectos)
    BUDGET_TOTAL = 150000.00 
    
    total_gastado = df_actual["Monto"].sum()
    balance = BUDGET_TOTAL - total_gastado
    porcentaje_consumido = (total_gastado / BUDGET_TOTAL) * 100 if BUDGET_TOTAL > 0 else 0

    # KPIs Principales
    k1, k2, k3 = st.columns(3)
    k1.metric("Presupuesto de Obra", f"${BUDGET_TOTAL:,.2f}")
    k2.metric("Total Invertido", f"${total_gastado:,.2f}", delta=f"{porcentaje_consumido:.1f}% del total")
    k3.metric("Margen de Seguridad", f"${balance:,.2f}", delta_color="inverse")

    st.markdown("---")
    
    c_left, c_right = st.columns([2, 1])
    
    with c_left:
        st.subheader("Desglose por Rubro")
        if not df_actual.empty:
            chart_data = df_actual.groupby("Rubro")["Monto"].sum()
            st.bar_chart(chart_data)
        else:
            st.write("No hay datos suficientes para graficar.")

    with c_right:
        st.subheader("Distribución de Inversión")
        if not df_actual.empty:
            # Mostramos el top de proveedores
            top_prov = df_actual.groupby("Proveedor")["Monto"].sum().sort_values(ascending=False).head(5)
            st.table(top_prov)
