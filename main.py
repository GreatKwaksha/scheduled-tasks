import requests
from twilio.http.http_client import TwilioHttpClient
import os
import json
from twilio.rest import Client

api_key=os.environ.get("API_KEY")
token=os.environ.get("TWILIO_TOKEN")
sid=os.environ.get("TWILIO_SID")
my_lat=28.4546
my_long=117.9436
parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "cnt": 4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data=response.json()
for d in weather_data["list"]:
    for i in d["weather"]:
        if i["id"]<700:
            raining=True
if raining==True:
    proxy_client=TwilioHttpClient()
    proxy_client.session.proxies={'https': os.environ['https_proxy']}
    client=Client(sid,token,http_client=proxy_client)
    message=client.messages \
    .create(body="Чакаецца дождж у бліжэйшыя гадзіны. Мо і ракетны сыпане.",from_="whatsapp:+14155238886",to="whatsapp:+972533714240")
    print(message.status)

