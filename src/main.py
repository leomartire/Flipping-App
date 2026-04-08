import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Flipping-App", layout="centered")

st.title("🏦 Flipping-App: Gestión de Gastos")
st.subheader("Carga de Transacciones")

# --- FORMULARIO DE ENTRADA ---
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    fecha = col1.date_input("Fecha", datetime.now())
    categoria = col2.selectbox("Categoría", ["Alimentación", "Servicios", "Transporte", "Ocio", "Salud", "Otros"])
    
    monto = col1.number_input("Monto", min_value=0.0, step=100.0)
    descripcion = col2.text_input("Descripción (ej. Supermercado)")
    
    submit = st.form_submit_button("Registrar Gasto")

# --- LÓGICA DE GUARDADO ---
if submit:
    nuevo_gasto = {
        "Fecha": [fecha],
        "Categoría": [categoria],
        "Monto": [monto],
        "Descripción": [descripcion]
    }
    df = pd.DataFrame(nuevo_gasto)
    
    st.success(f"✅ Gasto de ${monto} en {categoria} registrado correctamente.")
    st.write("Vista previa del registro:")
    st.table(df)

# --- RESUMEN TEMPORAL ---
st.info("Próximo paso: Conectar con una base de datos para persistir los datos.")
