import streamlit as st
import pandas as pd
import joblib

# Cargar modelo
modelo = joblib.load("modelo_casas.pkl")

# Configuración de la página
st.set_page_config(
    page_title="Predicción del valor de viviendas",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Predicción del valor mediano de la vivienda")

st.write(
    "Modifica las características de la zona y obtén una predicción del valor medio de la vivienda."
)

# Entradas del usuario
longitud = st.number_input(
    "Longitud",
    min_value=-125.0,
    max_value=-113.0,
    value=-118.49,
    step=0.01
)

latitud = st.number_input(
    "Latitud",
    min_value=32.0,
    max_value=42.0,
    value=34.26,
    step=0.01
)

edad_mediana_vivienda = st.slider(
    "Edad mediana de la vivienda",
    min_value=1,
    max_value=52,
    value=29
)

total_habitaciones = st.number_input(
    "Total de habitaciones",
    min_value=1,
    value=2127
)

total_dormitorios = st.number_input(
    "Total de dormitorios",
    min_value=1,
    value=435
)

poblacion = st.number_input(
    "Población",
    min_value=1,
    value=1166
)

hogares = st.number_input(
    "Número de hogares",
    min_value=1,
    value=409
)

ingreso_mediano = st.number_input(
    "Ingreso mediano",
    min_value=0.0,
    value=3.53,
    step=0.01
)

proximidad_oceano = st.selectbox(
    "Proximidad al océano",
    [
        "<1H OCEAN",
        "INLAND",
        "ISLAND",
        "NEAR BAY",
        "NEAR OCEAN"
    ]
)

# Crear DataFrame con los nombres EXACTOS usados al entrenar
datos = pd.DataFrame({
    "longitud": [longitud],
    "latitud": [latitud],
    "edad_mediana_vivienda": [edad_mediana_vivienda],
    "total_habitaciones": [total_habitaciones],
    "total_dormitorios": [total_dormitorios],
    "poblacion": [poblacion],
    "hogares": [hogares],
    "ingreso_mediano": [ingreso_mediano],
    "proximidad_oceano": [proximidad_oceano]
})

# Botón de predicción
if st.button("Predecir valor de la vivienda"):

    prediccion = modelo.predict(datos)[0]

    st.success(
        f"🏡 Valor mediano estimado de la vivienda: ${prediccion:,.2f}"
    )

    st.balloons()
