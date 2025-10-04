import streamlit as st
import pandas as pd
from transformers import pipeline

# IA para resumen
summarizer = pipeline("summarization", model="t5-small")

def resumir_texto(texto):
    resumen = summarizer(texto, max_length=150, min_length=40, do_sample=False)
    return resumen[0]['summary_text']

# Interfaz
st.title("🔬 Panel de Biociencia Espacial - NASA")
st.sidebar.selectbox("Filtrar por misión", ["Todas", "Apolo", "ISS", "Artemis"])

# Carga de datos
data = pd.read_csv("publicaciones.csv")
st.dataframe(data)

# Botón para resumen
if st.button("Ver resumen de artículo"):
    texto = open("articulo.txt").read()
    st.write(resumir_texto(texto))

# Gráfico de conocimiento
st.markdown("### 🌐 Gráfico de conocimiento")
st.components.v1.html(open("grafo.html").read(), height=800)
