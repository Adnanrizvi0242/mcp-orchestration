import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# ================= LOAD ENV ================= #

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

API_KEY = os.getenv("WEATHERSTACK_API_KEY")

# ================= WEATHER LOGIC ================= #

def get_weather(city: str) -> str:
    """
    Fetch current weather for a given city.

    Args:
        city (str): City name (example: "Delhi")

    Returns:
        str: Human-readable weather report
    """
    if not API_KEY:
        return "Weather API key is not configured."

    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": API_KEY,
        "query": city
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        # Weatherstack API error
        if "error" in data:
            return f"Weather data not found for '{city}'."

        location = data.get("location")
        current = data.get("current")

        if not location or not current:
            return f"Incomplete weather data for '{city}'."

        city_name = location.get("name")
        region = location.get("region")
        country = location.get("country")

        temperature = current.get("temperature")
        feels_like = current.get("feelslike")
        humidity = current.get("humidity")
        description = current.get("weather_descriptions", [""])[0]

        return (
            f"🌍 Weather in {city_name}, {region}, {country}\n"
            f"🌡 Temperature: {temperature}°C (feels like {feels_like}°C)\n"
            f"💧 Humidity: {humidity}%\n"
            f"☁ Condition: {description}"
        )

    except requests.exceptions.RequestException:
        return "Unable to fetch weather data. Please try again later."
    except Exception:
        return "Unexpected error while fetching weather data."
