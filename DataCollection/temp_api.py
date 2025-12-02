import requests
import pandas as pd

# Bhubaneswar coordinates
lat = 20.2961
lon = 85.8245

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

r = requests.get(url)
data = r.json()

df = pd.DataFrame([data["current_weather"]])
df.to_csv("weather_data.csv", index=False)

print("Weather data saved!")
print(df.head())
