# from api import character_JSON_request, user_agent, comicvine_API_KEY
import json 
# from pprint import pprint
import os

directory = 'data/characters'

# dictionary keys include: creators, deck (biography), gender, id, name, powers

# prints all key and value pairs in char_results dictionary
def get_key_attributes(char_results):
  for attribute, char_info in char_results.items():
    # print(f'{attribute}:{char_info}')
    print(f'Key attribute: {attribute}')
  return

def access_creators(dict_results):
  """Extracts a character's creator name(s) and return as a list."""
  creators = dict_results['creators']
  creators_list = []
  for creator in creators:
    creator_name = creator['name']
    creators_list.append(creator_name)
  # print(f'creators: {creators_list}')
  return creators_list

# creators = access_creators(char_results)
# print(creators)


#####DECK(biography)#########
#deck: returns string
def access_biography(dict_results):
  """Returns character biography by accessing 'deck' key in character results dictionary."""
  biography = dict_results['deck']
  return biography
  
####GENDER####
# gender: returns as int, assumptions conclude that 1 = male, and 2 = female *eye roll*
def access_gender(dict_results):
  """Access 'gender' key and depending on int value, will return gender string."""
  gender = ''
  gender_int = dict_results['gender']
  if gender_int == 1:
    gender = "male"
  elif gender_int == 2:
    gender = "female"
  else: 
    gender = "other"
  # print(f'gender: {gender}')
  return gender

####id####
# comic vine id returns integer
def access_comicvineID(dict_results):
  """Returns character Comic Vine ID."""
  comicvine_ID = dict_results['id']
  return comicvine_ID

####NAME####
# returns string
def access_name(dict_results):
  """Returns character's name (not legal name, the nom de guerre)."""
  char_name = dict_results['name']
  return char_name

####POWERS####
# returns a list of dictionaries. key to power is "name"
def access_powers(dict_results):
  """Returns list of character's powers."""
  powers = dict_results['powers']
  powers_list = []
  for power in powers:
    char_power = power['name']
    powers_list.append(char_power)
    # print(f'char_power {char_power}')
  # print(f'powers_list {powers_list}')
  return powers_list

def access_image(dict_results):
  """Returns hyperlink to character profile picture."""
  image = dict_results['image']
  chosen_image = image['medium_url']

  return chosen_image

# print(access_image(char_results))

print('os.listdir(directory)', os.listdir(directory))

char_dicts = []
for char_file in os.listdir(directory):
  # f is a single file
  f = os.path.join(directory, char_file)
  print('f', f)
  if os.path.isfile(f):
    # reads JSON file for character
    json_string = open(f).read()
    # print('json_string', json_string)

  # returns JSON file as python dictionary
  json_dict = json.loads(json_string)
  # print('json_dict', json_dict)

  # accesses 'results' and returns dictionary containing only relevant information
  char_results = json_dict['results']
  # print('char_results', char_results)
    
  character_dictionary = {}

  creators = access_creators(char_results)
  biography = access_biography(char_results)
  gender = access_gender(char_results)
  id = access_comicvineID(char_results)
  name = access_name(char_results)
  powers = access_powers(char_results)
  image = access_image(char_results)

  character_dictionary['id'] = id
  character_dictionary['image'] = image
  character_dictionary['name'] = name
  character_dictionary['gender'] = gender
  character_dictionary['biography'] = biography
  character_dictionary['powers'] = powers
  character_dictionary['creators'] = creators

  char_dicts.append(character_dictionary)
  # print(f'character_dictionary {character_dictionary}')



for char in char_dicts:
  print(f'charid: {char["id"]}')