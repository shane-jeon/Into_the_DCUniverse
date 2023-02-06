"""APIs and Requests Library."""

import json
import requests
# import jsonpickle
import time
import math
import importlib
from modules.extract_YJ import matching_values


superhero_API_KEY = 1075529179813027
comicvine_API_KEY = '6028f8ab23892d424a31b9845b1c36ed4f737523'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'

def comicvine_get_request(your_UA, API_KEY, resource, fields, new_filename):
  """A general get request for comic vine. 
  
  Parameters explained respectively, your user_agent information, your API key, resource: what information you are requesting (character, publisher, etc.), fields: what information you want to get back, new_filename: name of JSON file"""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # required information needed
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : fields
  }

  # URL for API request
  URL = f'https://comicvine.com/api/{resource}/4010-10/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)

def character_JSON_request(your_UA, API_KEY, char_id, new_filename):
  """A manual get request for comic vine. 
  
  Parameters explained respectively, your user_agent information, your API key, resource: what information you are requesting (character, publisher, etc.), fields: what information you want to get back, new_filename: name of JSON file"""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # hard coding fields
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : 'id,image,name,real_name,aliases,gender,origin,deck,powers,character_friends,character_enemies,teams,first_appeared_in_issue,count_of_issue_appearances,issue_credits,creators'
  }

  # URL for API request
  URL = f'https://comicvine.com/api/character/4005-{char_id}/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'data/characters/{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)


def comic_JSON_request(your_UA, API_KEY, resource, fields, new_filename):
  """Get information of comic issues each character has appeared in."""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # required information needed
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : fields
  }

  # URL for API request
  URL = f'https://comicvine.com/api/{resource}/4010-10/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'data/comics{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)


# comic_JSON_request(user_agent, comicvine_API_KEY, 'comic', 'id,name,person_credits,volume,deck,description,cover_date')


def get_info_from_charID(API_KEY, your_header, matching_values):
  """Gets 99 character IDs from matching_values list to request character data."""
  headers = {'User-Agent': your_header}
  payload = {'api_key': API_KEY,
            'format': 'json',
            'field_list':'id,image,name,real_name,aliases,gender,origin,deck,powers,character_friends,character_enemies,teams,first_appeared_in_issue,count_of_issue_appearances,issue_credits,creators'
  }

  req_count = 0
  hourly_max = 100
  daily_max = 2400

  for value in matching_values:
    char_id = value['id']
    name = value['name']
    print('char_id: ', char_id)
    print('name: ', name)

    req_count += 1

    if req_count % hourly_max== 0:
      current_id = char_id
      print("Paused at: ", current_id)
      time.sleep(3605)
      continue
    if req_count % daily_max == 0:
      current_id = char_id
      print("Paused for 24 hours at: ", current_id)
      time.sleep(86400)
      continue

    URL = f'https://www.comicvine.com/api/character/4005-{char_id}/'

    response = requests.get(URL, params=payload, headers=headers)

    print()
    print('*'*20)
    print()
    print(f"""Current request count at: {req_count},
          At character: {name},
          Character ID: {char_id},
          Response URL: {response.url}""")
    print()
    print('*'*20)
    print()

    json_object = json.dumps(response.json(), indent=3)

    print(name)
    char_name = name.replace(" ", "_").lower()
    print(char_name)
    # writing to json file
    with open(f'data/api_data/{char_name}.json', 'w') as outfile:
      outfile.write(json_object)

get_info_from_charID(comicvine_API_KEY, user_agent, matching_values)


# SUPERHERO API
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


# cleans up postman downloaded JSON file*
# def format_conversion(filename, new_filename):
#   """ Transforms incoherent Postman JSON file to readable JSON file.
#   Use when terminal GET request keeps returning with 403,
#   but Postman GET reqest returns 200 and thus have to download file from Postman."""

#   with open(filename) as data_file:
#     data = json.load(data_file)

#   json_object = json.dumps(data, indent=4)

#   with open(new_filename, 'w') as outfile:
#     outfile.write(json_object)


# format_conversion('data/character_JSON/requires_reformatting/zatanna.json', 'data/character_JSON/zatanna.json')
