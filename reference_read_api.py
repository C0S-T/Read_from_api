import requests
import json

data_from_api = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid=3b66f592d458664efde58a8fda5dc3e4")
#print the stauts code of the above api = 100 - Info Msg ; 200 - Success ; 300 - Redirection
# 400 - Client Error ; 500 - Server Error
#print(data_from_api.status_code)

#print the json data  from the response in a pretty format 
# Json = keys : values format
#print(data_from_api.json())

#dt = path of the data
data = data_from_api.json()["list"]
print(data)
print(data[0]['main']['feels_like'])