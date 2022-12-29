from bs4 import BeautifulSoup
import requests

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=43.2073&lon=-71.5366")

if page.status_code == 200:
    con = page.content
else:
    print(page.status_code)

soup = BeautifulSoup(con,'html.parser')

seven_day = soup.find(id="seven-day-forcast")

forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forcast_items[0]
print(tonight.prettify())
