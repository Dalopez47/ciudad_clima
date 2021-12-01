import json
import urllib.request

url = "http://api.openweathermap.org/data/2.5/weather?q=Bogota,co&appid=1508a9a4840a5574c822d70ca2132032"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data)
