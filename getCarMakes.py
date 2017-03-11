import requests
import json

# Getting Editorial Api for Each make name from carMakes.jso
# make nname.model nice name.year = 2017

# Tod0
# Feature1 - COmpare all the models with their emission index values ( NOX, SOx , CO)
# Feature2 - Compare each make with previous years models
# Final Feature - Compare each make with each other, find the better ones and ... (tanay will think)

makes_minimal = ["volkswagen", "nissan", "mercedes-benz", "mini", "jeep", "kia", "toyota", "hyundai"]  # badcars


# goodcars - porsche,subaru(1 model), "nissan","mercedes","mini-cooper","jeep","kia","toyota","hyundai"

def getReviews(makes_minimal):
    for make in makes_minimal:
        url = "https://api.edmunds.com/api/vehicle/v2/" + make + "/models?fmt=json&api_key=sv3ga54hu77qybtxamykpbdg"
        res = requests.get(url)
        jsonRes = res.json()
        # print jsonRes
        with open(make+".json", "a") as jsonfile:
            json.dump(jsonRes, jsonfile)
            jsonfile.write("\n")


getReviews(makes_minimal)
