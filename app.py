import streamlit as st
import numpy as np
import joblib

# Cargar modelo
modelo = joblib.load("modelo_casas.pkl")

st.title("🏠 Predicción de precio de casas")

st.write("Ingresa las características de la casa:")

# Ejemplo de inputs (ajústalos a tus variables reales)
area = st.number_input("Área (m²)", min_value=0)
habitaciones = st.number_input("Número de habitaciones", min_value=0)
banos = st.number_input("Número de baños", min_value=0)
ubicacion = st.number_input("Índice de ubicación (si lo usaste)", min_value=0)

# Botón de predicción
if st.button("Predecir precio"):
    datos = np.array([[area, habitaciones, banos, ubicacion]])
    prediccion = modelo.predict(datos)

    st.success(f"💰 El precio estimado es: {prediccion[0]:,.2f}")
