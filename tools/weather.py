import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# ---- FORCE LOAD .env FROM PROJECT ROOT ----
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)

API_KEY = os.getenv("WEATHERSTACK_API_KEY")

def get_weather(city: str) -> str:
    if not API_KEY:
        return "Weather API key not configured."

    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": API_KEY,
        "query": city
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        # Weatherstack error handling
        if "error" in data:
            return f"Weather data not found for '{city}'. Please try another city."

        location = data.get("location")
        current = data.get("current")

        if not location or not current:
            return f"Incomplete weather data for '{city}'."

        city_name = location.get("name")
        region = location.get("region")
        country = location.get("country")

        temperature = current.get("temperature")
        humidity = current.get("humidity")
        description = current.get("weather_descriptions", [""])[0]
        feels_like = current.get("feelslike")

        return (
            f"🌍 Weather in {city_name}, {region}, {country}\n"
            f"🌡 Temperature: {temperature}°C (feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁ Condition: {description}"
        )

    except Exception as e:
        return "Error fetching weather data."



