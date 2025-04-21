import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energiedashboard", layout="wide")
 
st.title("🔆 Marktwert Solar (Monatlich, 2025)")
 
# CSV von GitHub laden
url = "https://raw.githubusercontent.com/sourci91/Energie-Dashboard/refs/heads/main/Monatsmarktwerte%20%5B2025-04-21%2012-43-37%5D.csv"
df = pd.read_csv(url, sep=';', encoding='latin1', skiprows=5)

# Zeige die Spaltennamen
st.write(df.columns)


