import json
import requests
makes_minimal = ["mercedes-benz", "mini", "jeep", "kia","hyundai","toyota"] 
i=0 
style_ids = []
  

def getReviews(make,id):
	apiUrl = "https://api.edmunds.com/api/vehiclereviews/v2/styles/"+str(id)+"?fmt=json&api_key=sv3ga54hu77qybtxamykpbdg"
	res = requests.get(apiUrl)
	print res

	if res.status_code == 200:	
		with open(make+'-reviews.json','a') as f:
			f.write("{},\n".format(json.dumps(res.json())))

for make in makes_minimal:
  with open('data/'+make+'.json','r') as json_data:
        objects = json.load(json_data)
        for current_model in objects["models"]:
            for year in current_model["years"]:
                for style in year["styles"]:
                        getReviews(make,style["id"])

