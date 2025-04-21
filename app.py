from selenium import webdriver
from bs4 import BeautifulSoup
import time

def extract_data():
    # SafariDriver starten (kein Pfad nötig)
    driver = webdriver.Safari()

    url = "https://www.energy-charts.info/charts/market_values/chart.htm?l=de&c=DE&legendItems=0xi0"
    driver.get(url)

    # Warten, bis die Daten geladen sind
    time.sleep(5)

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', {'class': 'chart-table'})

    if table is None:
        raise ValueError("❌ Tabelle wurde nicht gefunden – evtl. hat sich die Seite geändert.")

    rows = table.find_all('tr')
    months, spotmarkt, solar = [], [], []

    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) >= 3:
            months.append(cols[0].text.strip())
            spotmarkt.append(cols[1].text.strip().replace(" €", "").replace(",", "."))
            solar.append(cols[2].text.strip().replace(" €", "").replace(",", "."))

    import pandas as pd
    df = pd.DataFrame({
        'Monat': months,
        'Spotmarktwert (€)': pd.to_numeric(spotmarkt, errors='coerce'),
        'Marktwert Solar (€)': pd.to_numeric(solar, errors='coerce')
    })

    df['Monat'] = pd.to_datetime(df['Monat'], format='%b %Y')
    df.set_index('Monat', inplace=True)
    return df
