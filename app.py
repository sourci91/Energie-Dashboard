Python 3.13.3 (v3.13.3:6280bb54784, Apr  8 2025, 10:47:54) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import streamlit as st
... import pandas as pd
... 
... st.set_page_config(page_title="Energiedashboard", layout="wide")
... 
... st.title("🔆 Marktwert Solar (Monatlich, 2024)")
... 
... # CSV von Netztransparenz.de laden
... url = "https://www.netztransparenz.de/portals/1/Content/Markttransparenz/Marktwerte/Monatliche_Marktwerte_2024.csv"
... df = pd.read_csv(url, sep=';', encoding='latin1', skiprows=5)
... 
... # Nur Solar und relevante Spalten filtern
... df = df[['Monat', 'Marktwert Solar [ct/kWh]']]
... df['Monat'] = pd.to_datetime(df['Monat'], format='%b %Y')
... df.set_index('Monat', inplace=True)
... df.sort_index(inplace=True)
... 
... # Darstellung
... st.line_chart(df['Marktwert Solar [ct/kWh]'])
