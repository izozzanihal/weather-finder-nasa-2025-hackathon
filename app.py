from flask import Flask, render_template, request
import random
from datetime import datetime

app = Flask(__name__)

# Weather data for 10 cities including Kerala
weather_data = {
    "Kochi, Kerala": [
        {"temp": 30, "wind": 10, "rain": 12, "humidity": 75, "sky": "Cloudy"},
        {"temp": 32, "wind": 8, "rain": 5, "humidity": 70, "sky": "Sunny"},
        {"temp": 28, "wind": 12, "rain": 15, "humidity": 80, "sky": "Rainy"}
    ],
    "Bangalore, India": [
        {"temp": 28, "wind": 10, "rain": 5, "humidity": 65, "sky": "Clear"},
        {"temp": 24, "wind": 15, "rain": 12, "humidity": 70, "sky": "Cloudy"},
        {"temp": 25, "wind": 8, "rain": 0, "humidity": 60, "sky": "Sunny"}
    ],
    "Delhi, India": [
        {"temp": 31, "wind": 12, "rain": 0, "humidity": 40, "sky": "Sunny"},
        {"temp": 32, "wind": 14, "rain": 3, "humidity": 45, "sky": "Clear"},
        {"temp": 29, "wind": 10, "rain": 8, "humidity": 50, "sky": "Cloudy"}
    ],
    "Mumbai, India": [
        {"temp": 31, "wind": 15, "rain": 20, "humidity": 80, "sky": "Rainy"},
        {"temp": 27, "wind": 12, "rain": 10, "humidity": 70, "sky": "Cloudy"},
        {"temp": 30, "wind": 8, "rain": 5, "humidity": 75, "sky": "Sunny"}
    ],
    "Dubai, UAE": [
        {"temp": 32, "wind": 8, "rain": 0, "humidity": 20, "sky": "Sunny"},
        {"temp": 33, "wind": 6, "rain": 0, "humidity": 15, "sky": "Clear"},
        {"temp": 34, "wind": 10, "rain": 0, "humidity": 25, "sky": "Sunny"}
    ],
    "London, UK": [
        {"temp": 11, "wind": 18, "rain": 10, "humidity": 60, "sky": "Cloudy"},
        {"temp": 12, "wind": 20, "rain": 15, "humidity": 65, "sky": "Rainy"},
        {"temp": 18, "wind": 12, "rain": 5, "humidity": 55, "sky": "Clear"}
    ],
    "New York, USA": [
        {"temp": 22, "wind": 12, "rain": 5, "humidity": 50, "sky": "Sunny"},
        {"temp": 18, "wind": 10, "rain": 0, "humidity": 55, "sky": "Clear"},
        {"temp": 25, "wind": 14, "rain": 8, "humidity": 60, "sky": "Cloudy"}
    ],
    "Tokyo, Japan": [
        {"temp": 26, "wind": 10, "rain": 15, "humidity": 65, "sky": "Rainy"},
        {"temp": 29, "wind": 12, "rain": 20, "humidity": 70, "sky": "Cloudy"},
        {"temp": 23, "wind": 8, "rain": 2, "humidity": 60, "sky": "Sunny"}
    ],
    "Sydney, Australia": [
        {"temp": 28, "wind": 25, "rain": 2, "humidity": 55, "sky": "Clear"},
        {"temp": 22, "wind": 18, "rain": 5, "humidity": 60, "sky": "Cloudy"},
        {"temp": 16, "wind": 12, "rain": 8, "humidity": 65, "sky": "Rainy"}
    ],
    "Toronto, Canada": [
        {"temp": 20, "wind": 11, "rain": 3, "humidity": 50, "sky": "Cloudy"},
        {"temp": 6, "wind": 14, "rain": 5, "humidity": 55, "sky": "Snowy"},
        {"temp": 12, "wind": 10, "rain": 0, "humidity": 45, "sky": "Sunny"}
    ],
}

def comfort_level(temp, wind, rain):
    """Determine comfort level and CSS class"""
    if temp > 35:
        return "Very Hot 🔥", "hot"
    elif temp < 10:
        return "Very Cold ❄️", "cold"
    elif wind > 20:
        return "Very Windy 💨", "wind"
    elif rain > 15:
        return "Very Wet 🌧️", "wet"
    elif temp > 30 and rain > 5:
        return "Very Uncomfortable 😓", "hot"
    else:
        return "Comfortable 🙂", "comfort"

@app.route("/", methods=["GET", "POST"])
def index():
    city = None
    data = None
    comfort = None
    comfort_class = None
    summary = None
    date = datetime.now().strftime("%d %b %Y")

    if request.method == "POST":
        city = request.form.get("city")
        if city in weather_data:
            data = random.choice(weather_data[city])
            comfort, comfort_class = comfort_level(data["temp"], data["wind"], data["rain"])
            summary = f"Today in {city}, expect {data['sky'].lower()} skies with temperature around {data['temp']}°C."

    return render_template(
        "index.html",
        cities=weather_data.keys(),
        city=city,
        data=data,
        comfort=comfort,
        comfort_class=comfort_class,
        summary=summary,
        date=date
    )

if __name__ == "__main__":
    app.run(debug=True)
