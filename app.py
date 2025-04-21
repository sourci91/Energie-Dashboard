
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Energiedashboard", layout="wide")
 
st.title("🔆 Marktwert Solar (Monatlich, 2024)")
 
# CSV von Netztransparenz.de laden
url = "https://www.netztransparenz.de/portals/1/Content/Markttransparenz/Marktwerte/Monatliche_Marktwerte_2024.csv"
df = pd.read_csv(url, sep=';', encoding='latin1', skiprows=5)

# Nur Solar und relevante Spalten filtern
df = df[['Monat', 'Marktwert Solar [ct/kWh]']]
df['Monat'] = pd.to_datetime(df['Monat'], format='%b %Y')
df.set_index('Monat', inplace=True)
df.sort_index(inplace=True)

# Darstellung
st.line_chart(df['Marktwert Solar [ct/kWh]'])
