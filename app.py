import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energiedashboard", layout="wide")
 
st.title("🔆 Marktwert Solar (Monatlich, 2025)")
 
# CSV von GitHub laden
url = "https://raw.githubusercontent.com/sourci91/Energie-Dashboard/refs/heads/main/Monatsmarktwerte%20%5B2025-04-21%2012-43-37%5D.csv"
df = pd.read_csv(url, sep=';', encoding='latin1', skiprows=5)

# Zeige die Spaltennamen
st.write(df.columns)

# Sicherstellen, dass die Spalte 'MW Solar' vorhanden ist
df = df[['Monat', 'MW Solar']]  # Passe hier den Namen je nach Ausgabe von st.write an
df['Monat'] = pd.to_datetime(df['Monat'], format='%b %Y')
df.set_index('Monat', inplace=True)
df.sort_index(inplace=True)

# Darstellung
st.line_chart(df['MW Solar'])  # Verwende hier die richtige Spalte
