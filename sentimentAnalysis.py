import sys
import json
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob
import time

makes_minimal = ["volkswagen","nissan","mercedes-benz", "mini", "jeep", "kia","hyundai"] 
make_sum = []

#for printing a rotating backslash in console during processing
def printSlash():
	syms = ['\\', '|', '/', '-']
	bs = '\b'
	for _ in range(10):
		for symbol in syms:
			sys.stdout.write("\b%s" % symbol)
			sys.stdout.flush()
			time.sleep(0.5)

#for finding the overall score for each make. make_sum = (sum of all edmund_score / number of Reviews)
def findScoreForMake(scores_array,numberOfReviews):
	sum = 0
	for score in scores_array:
		sum = float(sum + score)
	make_sum.append(float(sum/numberOfReviews))


#for parsing json file (will be changed to rdd or pandas df in next build)
def parseFile(fileUrl,scores_array):
	count = 0
	with open(fileUrl,'r') as jsonFile:
			sent_objects = json.load(jsonFile)
			for wrapper_obj in sent_objects["reviews"]:
				for reviews_array in wrapper_obj["reviews"]:
					count+=1;
					try:
						text_reviews = reviews_array["text"] #getting text and suggested improvement
						sugg_improvements = reviews_array["suggestedImprovements"]
						blob_text = TextBlob(text_reviews)
						blob_improvements = TextBlob(sugg_improvements).sentiment.polarity

						#polarity_score = polarity(text) + polarity(suggested_improvements)
						polarity_score = blob_text.sentiment.polarity + float(blob_improvements)

						#avg_rating given by the user.
						average_rating = reviews_array["averageRating"]

						#obtaining fuel_economy rating
						fuel_economy = reviews_array["ratings"][2]["value"]

						edmunds_score = ((polarity_score) + float(average_rating))*float(fuel_economy)
						scores_array.append(edmunds_score)

					except KeyError:
						#if text params or any specified params are not available. that review is skipped
							continue
	return count
   					



def getSentiments():
	print "Analyzing DataSet. Preparing Edmund's Score for Vehicles. This may take a while . . . .",printSlash()
	for make in makes_minimal:
		fileUrl = make+"-reviews.json"
		scores_array = []

		#returns the no.of reviews.
		numberOfReviews = parseFile(fileUrl,scores_array)

		findScoreForMake(scores_array,numberOfReviews)

def buildGraph():
	print "Preparing graph . . .",printSlash()

	#aligning and centering graph basedd on the number of makes.
	plt.bar(range(len(make_sum)),make_sum,align='center')

	#make_names as x axis legends
	plt.xticks(range(len(make_sum)),makes_minimal,size = 'small')

	#graph rendered
	print 'Graph rendered successfully.'
	plt.show()

#helper methods
getSentiments()
buildGraph()

