"""APIs and Requests Library."""

import requests

# Translates JSON to a python dictionary (and can convert a dictionary to JSON)
import json
# JSON methods
# json.loads() - loads JSON from a given string
# json.dumps(dictionary) - converts a dictionary to a JSON string
  # difference --> "s", stands for "string"
# json.load(open('file.json')) - loads JSON from a file
# json.dump(dictionary, open('file.json', 'w')) - writes a dictionary to a JSON file

# Superhero API
    #  while this API def has all heros (i think), doesn't contain all villians
# https://superheroapi.com/api/access-token
# Access Token: 1075529179813027

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
# res = requests.get('https://superheroapi.com/api/1075529179813027/search/{param}')
    # --> should get <Response [200]>

# Response.json is an instance method, will automatically turn JSON into python dictionary
# search_results = res.json()

# Requests - creates query string for user
# requests.get takes in second argument (params)
# params - should be a dictionary containing key-value pairs user wants to send in request

# for search NAME
  # api_key = 1075529179813027
  # payload = {'name': 'x'}
  # res = requests.get('https://superheroapi.com/api/1075529179813027/search', params=payload)
  # print(res.url) --> returns URL w/queries
  # superhero_char = res.json()
  # json.dumps(superhero_char) --> JSON query

# to READ and WRITE JSON file
  # using json.dumps(dictionary, indent), converts dictionary into JSON object
    # takes 2 parameters: 1) name of dictionary to be converted , 2) number of units for indentation
  # using json.dump(dictionary, file pointer) --> directly writes dictionary to a file in the form
    # of JSON without needing to convert into actual JSON object
# *However this method will return dictionary as one long string, no indentation*

# I want to get all characters affiliated with DC comics ONLY 
# the dictionary keys to use will be as follows
  # superhero_char['results'][i]['biography']['publisher']

# can't seem to get all characters....going to have to loop through char IDs (max num: 731)

# creating variable to allow others to insert their own api key (avoid hard coding)
# apikey = 1075529179813027

# for i in range(732):

  # payload = {'id': i} # character-id  
  # PAYLOAD DOES NOT WORK IN THIS SITUATION, BY USING THIS IT WILL ADD "SEARCH" TO THE REQUEST
  # url = f'https://superheroapi.com/api/{apikey}/{id}/biography'
  # res = requests.get(url, params=payload)
  # superheroAPI_data = res.json()

  # if ''

# working in terminal




# dictionary for JSON file
dc_characters = {}

for i in range(1, 732):

  url = f'https://superheroapi.com/api/1075529179813027/{i}'
  res = requests.get(url)
  # print(res.url)
  superhero_data = res.json()
  # print(char)

  print(f'at superhero #{i}')
  if superhero_data['biography']['publisher'] == 'DC Comics':
    name = superhero_data['name']
    if name in dc_characters:
      print(name)
      continue
    else:
      dc_characters[name] = superhero_data

# print(dc_characters)
json_object = json.dumps(dc_characters, indent=4)

with open('superHeroAPI_DC.json', 'w') as outfile:
  outfile.write(json_object)





  # for search NAME
  # api_key = 1075529179813027
  # payload = {'id': 10}
  # res = requests.get('https://superheroapi.com/api/1075529179813027', params=payload)
  # print(res.url) --> returns URL w/queries
  # superhero_char = res.json()
  # json.dumps(superhero_char) --> JSON query