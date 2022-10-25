"""APIs and Requests Library."""

# Translates JSON to a python dictionary (and can convert a dictionary to JSON)
import json
import requests

# api_key = "YOUR_ACCESS_TOKEN" #Obtain through https://www.superheroapi.com/, requires Facebook account however
api_key = 1075529179813027

def import_SuperHeroAPI(API_KEY):
  """Gets all available DC Comic characters from SuperHero API."""

  # dictionary for JSON file
  dc_characters = {}

  # loops through all character IDs in SuperHero API
  for i in range(1, 732):
    url = f'https://superheroapi.com/api/{API_KEY}/{i}'
    res = requests.get(url)
    # Displays response success/failure
    print('res:', res)
    # print(res.url)
    superhero_data = res.json()

    # to track progress of API request
    print(f'at superhero ID #{i}')
    # Access returned JSON dictionary with 2 key values to filter out non-DC Comics characters
    if superhero_data['biography']['publisher'] == 'DC Comics':
      # displays as function runs
      name = superhero_data['name']
      print()
      print("*****", name, "*****")
      print()
      if name in dc_characters:
        continue
      else:
        dc_characters[name] = superhero_data

  # gets JSON dictionary
  json_object = json.dumps(dc_characters, indent=4)

  # writes dictionary to JSON file
  with open('example.json', 'w') as outfile:
    outfile.write(json_object)


# import_SuperHeroAPI()

# url = 'https://comicvine.gamespot.com/api/'
# RAPIDAPI


# url = "https://advanced-movie-search.p.rapidapi.com/genre/movie/list"

# headers = {
# 	"X-RapidAPI-Key": "9cac440147mshfad4f28d042e400p18fa5fjsn5fd81cd960d3",
# 	"X-RapidAPI-Host": "advanced-movie-search.p.rapidapi.com"
# }

# res = requests.request("GET", url, headers=headers)

# movie_genres = res.json()

# json_object = json.dumps(movie_genres, indent=4)

# with open('movie_genres.json', 'w') as outfile:
#   outfile.write(json_object)
# print(response.text)


# SUPERHERO SEARCH

url = "https://superhero-search.p.rapidapi.com/api/"

querystring = {"hero":"batman"}

headers = {
	"X-RapidAPI-Key": "9cac440147mshfad4f28d042e400p18fa5fjsn5fd81cd960d3",
	"X-RapidAPI-Host": "superhero-search.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

batman = response.json()
json_object = json.dumps(batman, indent=3)

with open('batman.json', 'w') as outfile:
  outfile.write(json_object)
# print(response.text)

# ComicVine API very confusing to use
# username: milkis420, APIKEY: 6028f8ab23892d424a31b9845b1c36ed4f737523

# https://api.themoviedb.org/3/movie/76341?api_key=<<api_key>>
# api_key: d0c8ed23f9287cc230bd6045c8fb4985

# https://comicvine.gamespot.com/api/search/?api_key= api_key&format=json&limit=1&offset=0&field_list=id,name,deck,volume&sort=name:asc&resources=issue&query=Feynman



# JSON/API Reference Information

# JSON methods
# json.loads() - loads JSON from a given string
# json.dumps(dictionary) - converts a dictionary to a JSON string
  # difference --> "s", stands for "string"
# json.load(open('file.json')) - loads JSON from a file
# json.dump(dictionary, open('file.json', 'w')) - writes a dictionary to a JSON file

# Superhero API
    #  while this API def has all heros (i think), doesn't contain all villians
# https://superheroapi.com/api/access-token


# Personal easy access URL:
  # https://superheroapi.com/api/1075529179813027

# GET methods (available endpoints)
# API Hierarchy
# from '/id' - Search by character id. Returns all info of the character.
  # following returns JSON Array
  # '/id/powerstats'
  # '/id/biography'
  # '/id/apperance'
  # '/id/work'
  # '/id/connections'
  # '/id/image'

# SEARCH character by name, returns character ID
# '/search/name'

# to make a GET request (simple search)

# function that can take in string w/URL request
# --> res = requests.get('https://superheroapi.com/api/1075529179813027/search/{param}')
    # should get <Response [200]>

# res.json is an instance method, will automatically turn JSON into python dictionary
# --> search_results = res.json()

# Requests - creates query string for user
# res.get takes in second argument (params)
# params - should be a dictionary containing key-value pairs user wants to send in request

# for '/search/name' # USING PAYLOAD ADDs "SEARCH" TO THE REQUEST URL
  # api_key = 1075529179813027
  # payload = {'name': 'x'}
  # res = requests.get('https://superheroapi.com/api/1075529179813027', params=payload)
  # print(res.url) --> returns URL w/queries
  # superhero_char = res.json()
  # json.dumps(superhero_char) --> JSON query

# to READ and WRITE JSON file
  # using json.dumps(dictionary, indent), converts dictionary into JSON object
    # takes 2 parameters: 1) name of dictionary to be converted , 2) number of units for indentation
  # using json.dump(dictionary, file pointer) --> directly writes dictionary to a file in the form
    # of JSON without needing to convert into actual JSON object
# *However this method will return dictionary as one long string, no indentation*


