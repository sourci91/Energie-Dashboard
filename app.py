import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# Funktion zum Extrahieren der Daten über Safari (macOS only)
def extract_data():
    # SafariDriver starten (muss mit "safaridriver --enable" freigegeben sein)
    driver = webdriver.Safari()

    url = "https://www.energy-charts.info/charts/market_values/chart.htm?l=de&c=DE&legendItems=0xi0"
    driver.get(url)

    # Warten, bis die Seite komplett geladen ist
    time.sleep(5)

    # HTML-Inhalt holen
    html = driver.page_source
    driver.quit()

    # HTML mit BeautifulSoup parsen
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'chart-table'})

    if table is None:
        raise ValueError("❌ Tabelle nicht gefunden. Struktur der Seite hat sich evtl. geändert.")

    # Daten auslesen
    rows = table.find_all('tr')
    months, spotmarkt, solar = [], [], []

    for row in rows[1:]:
