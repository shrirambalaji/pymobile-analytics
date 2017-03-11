import json
makes_minimal = ["volkswagen", "nissan", "mercedes-benz", "mini", "jeep", "kia", "toyota", "hyundai"]  # badcars
i=0 
style_ids = []
  
for make in makes_minimal:
  with open('data/'+make+'.json','r') as json_data:
        objects = json.load(json_data)
        for current_model in objects["models"]:
            for year in current_model["years"]:
                for style in year["styles"]:
                    style_ids.append(style["id"])
                
i+=len(style_ids)
print 'Style IDS to parse ie. Number of Requests for all brands = '+str(i)
