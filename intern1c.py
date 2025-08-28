
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set your OpenWeatherMap API key here
API_KEY = 'a2d7435e7b90092f3cb4a51ab901f637'  # Replace with your real API key
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from OpenWeatherMap
response = requests.get(URL)
data = response.json()

# Parse forecast data
timestamps = []
temperatures = []

for entry in data['list']:
    time = datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    timestamps.append(time)
    temperatures.append(temp)

# Create the visualization
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=timestamps, y=temperatures, marker='o')

plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
