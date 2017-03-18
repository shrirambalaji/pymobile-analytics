#!/bin/bash  
mongoimport --db reviews --collection hyundai-reviews --file hyundai-reviews-reviews.json
mongoimport --db reviews --collection kia-reviews --file kia-reviews.json
mongoimport --db reviews --collection volkswagen-reviews --file volkswagen-reviews.json
mongoimport --db reviews --collection nissan-reviews --file nissan-reviews-reviews.json
mongoimport --db reviews --collection mini-reviews --file mini-reviews.json
mongoimport --db reviews --collection mercedes-benz-reviews --file mercedes-benz-reviews.json
mongoimport --db reviews --collection jeep-reviews --file jeep-reviews.json
