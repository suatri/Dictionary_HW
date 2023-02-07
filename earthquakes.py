# the eq_data file is a json file that contains detailed information about
# earthquakes around the world for a period of a month.

# NOTE: No hard-coding allowed except for keys for the dictionaries

# 1) print out the number of earthquakes

import json
from unittest.mock import MagicMixin

infile = open("eq_data.json", "r")
earthq = json.load(infile)

print(len(earthq["features"]))


"""
2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

"""

# Johnny, I'm used to seeing latitude before longitude there fore I grabed the data in the geometry section of the dictioanry from the jason in that order. This explains difference in order to your example.

earthq_info = earthq["features"]
eq_dict = {}
# print(eq_dict)
for i in earthq_info:
    if i["properties"]["mag"] > 6:
        location = i["properties"]["place"]
        magnitude = i["properties"]["mag"]
        longitud = i["geometry"]["coordinates"][1]
        latitude = i["geometry"]["coordinates"][0]
        eq_dict[location] = magnitude, longitud, latitude

# print(eq_dict)


# 3) using the eq_dict dictionary, print out the information as shown below (first three shown):
"""

# This is my version before figuring out that I had to use an observation as the key

earthq_info = earthq["features"]
for i in earthq_info:
    if i["properties"]["mag"] > 6:
        print(f"Location: {i['properties']['place']}")
        print(f"Magnitude: {i['properties']['mag']}")
        print(f"Longitude: {i['geometry']['coordinates'][2]}")
        print(f"Latitude: {i['geometry']['coordinates'][1]}")
        print()
        print()
        eq_dict.append(i)

"""
for i in eq_dict:
    print(f"Location: {i}")
    print(f"Magnitude: {eq_dict[i][0]}")
    print(f"Longitude: {eq_dict[i][1]}")
    print(f"Latitude: {eq_dict[i][2]}")
    print()
    print()

"""
Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

"""
