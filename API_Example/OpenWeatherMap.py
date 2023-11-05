# requires: pip install requests
# sign up for api_key here: https://openweathermap.org/appid
# api documentation here: https://openweathermap.org/api
import requests
import os

# Define your API key and the base URL
# Replace with your OpenWeatherMap API key, set up as environment variable locally
api_key = os.getenv('OpenWeather_API_Key')
# Validate your key is loaded with this print statement.
print(api_key)
base_url = 'http://api.openweathermap.org/data/2.5/weather'

# Get the city name from the user
city = input("Enter the city name: ")

# Construct the request parameters
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'  # You can change the units to 'imperial' for Fahrenheit
}

# Send an HTTP GET request to the API
response = requests.get(base_url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()

    # Extract and display the weather information
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    description = data['weather'][0]['description']
    temperature_fahrenheit = (temperature * 9 / 5) + 32
    feels_like_fahrenheit = (feels_like * 9 / 5) + 32
    print(f'Current weather in {city}:')
    print(f'Temperature: {temperature}°C ({temperature_fahrenheit}°F)')
    print(f'It feels like: {feels_like}°C ({feels_like_fahrenheit}°F)')
    print(f'Description: {description.capitalize()}')
    # prints all weather data gathered for the city as a JSON file
    print(data)
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
