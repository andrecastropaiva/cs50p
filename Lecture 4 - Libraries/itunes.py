# Demonstrates requests package
import json # this library comes already with python
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

# signs the result of requests.get() to the variable response
#response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # here we are cutting the name of the band so we can write any band name in the terminal when we run python itunes.py writebandname... 50 means the number of songs for the searched band

# json as upon check apple uses json format to store the data
print(json.dumps(response.json(), indent = 2)) # using another function json.dumps() to format the json data to be more readable... indent = 2 means to indent the json response to be indented to a max of 2 lines per code

# NOTE: the json file has basically a dictionary, a combination of key value pairs... sometimes even a dictionary inside a dictionary



# Upon checking the JSON file of itunes for the above song we know there is a key named "results" that contain objects such as "trackName"
# so we create a variable named object and store the json response and use a for loop to iterate through the dictionary

object = response.json()
for result in object["results"]: # here we know already the name of the key which is results as we checked the file earlier
    print(result["trackName"]) # will print the name of the songs for the band weezer and in the url API above we limit to 50...so 50 songnames