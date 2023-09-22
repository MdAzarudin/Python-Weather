from flask import Flask, render_template, request
import requests

app = Flask(__name__)

key = "6c6bdb5733f3c458d55b2ddc58723e09"

@app.route('/')
def login():
    return render_template("open.html")

@app.route('/weather', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
        )

        temp = weather_data.json().get("main").get("temp")
        hum = weather_data.json().get("main").get("humidity")
        wind = weather_data.json().get("wind").get("speed")
        sunrise = weather_data.json().get("sys").get("sunrise")
        sunset = weather_data.json().get("sys").get("sunset")
        pressure = weather_data.json().get("main").get("pressure")
        clouds = weather_data.json().get("weather")[0].get("description")
        cityname = weather_data.json().get("name")

        return render_template("index.html",tem=temp,humi=hum,win=wind,sun=sunrise,set=sunset,pres=pressure,clou=clouds,cit=cityname)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)