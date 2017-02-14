import requests
import json
apikey = "sv3ga54hu77qybtxamykpbdg"
url = "https://api.edmunds.com/api/vehicle/v2/makes?state=new&year=2017&view=basic&fmt=json&api_key="+apikey


jsonResponse = requests.get(url)
json_data = jsonResponse.json()

with open('carMakes.json','wb') as outputFile:
	json.dump(json_data,outputFile)