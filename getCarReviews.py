import requests
import json


#Getting Editorial Api for Each make name from carMakes.jso
#make nname.model nice name.year = 2017

#Todo
#Feature1 - Compare all the models with their emission index values ( NOX, SOx , CO) 
#Feature2 - Compare each make with previous years models 

makes_minimal = ["volkswagen","nissan","mercedes-benz","mini","jeep","kia","toyota","hyundai"] 
#goodcars - porsche,subaru(1 model), "nissan","mercedes","mini-cooper","jeep","kia","toyota","hyundai"
def getReviews(makes_minimal):
	for make in makes_minimal:
		url = "https://api.edmunds.com/api/vehicle/v2/"+make+"/models?fmt=json&api_key=sv3ga54hu77qybtxamykpbdg"
		res = requests.get(url)
		jsonRes = res.json()
		# print jsonRes
		with open("makes.json","a") as jsonfile:		
			json.dump(jsonRes,jsonfile)
			jsonfile.write("\n")

getReviews(makes_minimal)