import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Funktion zum Extrahieren der Daten von der Energy-Charts Website
def extract_data():
    # URL der Energy-Charts Seite
    url = "https://www.energy-charts.info/charts/market_values/chart.htm?l=de&c=DE&legendItems=0xi0"

    # HTTP-Anfrage an die Webseite
    response = requests.get(url)
    response.raise_for_status()  # Fehlerprüfung

    # BeautifulSoup zum Parsen des HTML-Inhalts
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finden des Tables (tabelle mit Marktwerten)
    table = soup.find('table', {'class': 'chart-table'})

    # Extrahieren der Daten in eine Liste
    rows = table.find_all('tr')
    
    # Initialisieren von Listen für die Daten
    months = []
    spotmarkt_values = []
    solar_values = []
    
    for row in rows[1:]:  # Ignorieren der Header-Zeile
        columns = row.find_all('td')
        if len(columns) > 1:  # Sicherstellen, dass es valide Daten gibt
            months.append(columns[0].text.strip())
            spotmarkt_values.append(columns[1].text.strip().replace(' €','').replace(',','.') if columns[1].text.strip() else None)
            solar_values.append(columns[2].text.strip().replace(' €','').replace(',','.') if columns[2].text.strip() else None)

    # Umwandeln der Daten in ein DataFrame
    data = {
        'Monat': months,
        'Spotmarktwert (€)': spotmarkt_values,
        'Marktwert Solar (€)': solar_values
    }
    df = pd.DataFrame(data)
    
    # Umwandeln der 'Monat'-Spalte in datetime und die Werte in float
    df['Monat'] = pd.to_datetime(df['Monat'], format='%b %Y')
    df['Spotmarktwert (€)'] = pd.to_numeric(df['Spotmarktwert (€)'], errors='coerce')
    df['Marktwert Solar (€)'] = pd.to_numeric(df['Marktwert Solar (€)'], errors='coerce')

    return df

# Streamlit-Setup
st.set_page_config(page_title="Energiedashboard", layout="wide")
st.title("🔆 Marktwert Solar und Spotmarktwert")

# Daten extrahieren
df = extract_data()

# Zeige die ersten paar Zeilen der Daten
st.write(df.head())

# Darstellung von Spotmarktwert und Marktwert Solar in zwei Diagrammen
st.subheader("Spotmarktwert")
st.line_chart(df['Spotmarktwert (€)'])

st.subheader("Marktwert Solar")
st.line_chart(df['Marktwert Solar (€)'])
