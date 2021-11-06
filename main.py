import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.metoffice.gov.uk/weather/forecast/gcqdt4b2x")
soup = BeautifulSoup(page.content, "html.parser")
week = soup.find(id="dayNav")

#image = week.find_all("alt")
items = week.find_all(class_="forecast-tab")

#print(items[0].find(class_="sticky-header").get_text())
#print(items[0].find(class_="step-time").get_text("|", strip=True))
#print(items[0].find(class_="step-pop").get_text("|", strip=True))
#print(items[0].find(class_="step-temp").get_text())

dayNames = [item.find(class_="tab-day").get_text(" ", strip=True) for item in items]
#description= [image for img in items]
temperatureHigh = [item.find(class_="tab-temp-high").get_text("|", strip=True) for item in items]
temperatureLow = [item.find(class_="tab-temp-low").get_text("|", strip=True) for item in items]
#time = [item.find(class_="step-time").get_text("|", strip=True) for item in items]
#precipitation = [item.find(class_="step-pop").get_text("|", strip=True) for item in items]


#print (dayNames)
#print (time)
#print (precipitation)
#print (temperature)

weather_stuff = pd.DataFrame(
	{
		"day": dayNames,
		"temperatureHigh": temperatureHigh,
		"temperatureLow": temperatureLow,
	})

print (weather_stuff)

weather_stuff.to_csv("weather.csv")