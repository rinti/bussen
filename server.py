import os
import datetime

from dotenv import load_dotenv
import httpx
import pprint

load_dotenv()

API_KEY = os.environ["TRAFIKLAB_API_KEY"]
URL = "https://api.resrobot.se/v2/trip.json?key={}&originId={}&destId={}&passlist=0&date={}&time={}&products=128"

# 740046158 = Rosenlundsgatan
# 740021705 = Gullmars
# 740053057 = Årsta torg

PAIRS = (("740046158", "740021705"), ("740053057", "740021705"))

stops = []

for pair in PAIRS:
    now = datetime.datetime.now()
    today = str(now.date())
    time = "{}:{:02d}".format(now.hour, now.minute)

    origin, destination = pair
    url = URL.format(API_KEY, origin, destination, today, time)
    req = httpx.get(url)
    json = req.json()

    name = req.json()["Trip"][0]["LegList"]["Leg"][0]["Origin"]["name"]
    times = []

    for trip in json["Trip"]:
        times.append(
            {
                "from": trip["LegList"]["Leg"][0]["Origin"]["name"],
                "with": trip["LegList"]["Leg"][0]["Product"]["name"],
                "to": trip["LegList"]["Leg"][0]["Destination"]["name"],
                "time": trip["LegList"]["Leg"][0]["Origin"]["time"],
            }
        )

    stops.append({"name": name, "times": times})

pprint.pprint(stops)
