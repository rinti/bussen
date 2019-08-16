import os

from dotenv import load_dotenv
import httpx
import pprint

load_dotenv()

API_KEY = os.environ["TRAFIKLAB_API_KEY"]
URL = (
    "http://api.sl.se/api2/realtimedeparturesv4.json"
    "?key={}&siteid={}&timewindow=60&metro=false&train=false&tram=false&ship=false"
)


PAIRS = (("740046158", "740021705"), ("740053057", "740021705"))

in_data = {1367: {"name": "Rosenlundsgatan"}, 1500: {"name": "Årsta torg"}}

data = []

for x in in_data.keys():
    req = httpx.get(URL.format(API_KEY, x))
    json = req.json()

    trips = list(
        filter(
            lambda x: x["Destination"] == "Gullmarsplan", json["ResponseData"]["Buses"]
        )
    )
    data.append({"name": in_data[x]["name"], "trips": trips})

pprint.pprint(data)
