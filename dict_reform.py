# from api import character_JSON_request, user_agent, comicvine_API_KEY
import json 
# from pprint import pprint
import os

directory = 'data/characters'

# dictionary keys include: id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, first_appearance, appearance_count, issue_credit, creator

for char_file in os.listdir(directory):
  # f is a single file
  f = os.path.join(directory, char_file)
  # print('f', f)
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


# prints all key and value pairs in char_results dictionary
# def get_key_attributes(char_results):
#   for attribute, char_info in char_results.items():
#     # print(f'{attribute}:{char_info}')
#     print(f'Key attribute: {attribute}')
#   return


####id####
# comic vine id returns integer
def access_comicvineID(dict_results):
  """Returns character Comic Vine ID."""
  comicvine_ID = dict_results['id']
  return comicvine_ID

####IMAGE####
# get both tiny and medium size picture 12/31/2022
def access_image(dict_results):
  """Returns hyperlink to character profile picture."""
  image = dict_results['image']
  chosen_image = image['medium_url']

  return chosen_image

####NAME####
# returns string
def access_name(dict_results):
  """Returns character's name (not legal name, the nom de guerre)."""
  char_name = dict_results['name']
  return char_name

####REAL NAME####
def access_realName(dict_results):
  """Returns character's real name as string."""
  char_real_name = dict_results['real_name']
  
  return char_real_name

####ACCESS_ALIASES####
# returns string, change to list using "\n" to denote item individuation
def access_alias(dict_results):
  """Returns list of character's aliases by accessing 'aliases' key in character results dictionary. As it returns a string, will be changing into list."""
  aliases = dict_results['aliases']
  alias = list(aliases.split("\r\n"))

  return alias

# print(f'{access_alias(char_results)}')

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

####ACCESS_ORIGIN####
# returns dictionary, access key "name"
def access_origin(dict_results):
  """Access 'name' in origin dictionary to obtain character origin."""
  origin = dict_results['name']

  return origin

#####DECK(biography)#########
#deck: returns string
def access_biography(dict_results):
  """Returns character biography by accessing 'deck' key in character results dictionary."""
  biography = dict_results['deck']
  return biography

####POWERS####
# returns a list of dictionaries. key to power is "name"
def access_power(dict_results):
  """Returns list of character's power."""
  power = dict_results['powers']
  power_list = []
  for power in power:
    char_power = power['name']
    power_list.append(char_power)
    # print(f'char_power {char_power}')
  # print(f'power_list {power_list}')
  return power_list

####ACCESS_FRIENDS####
# returns list of dictionaries. Dictionary access key "name" (possibly need ID?)
def access_friend(dict_results):
  """Returns a list of tuples containing character's friends and respective IDs."""
  friends = dict_results['character_friends']
  friend_list = []
  for friend in friends:
    # print(friend)
    friend_name = friend['name'].strip('\\')
    # print(f'friend_name {friend_name}')
    friend_id = friend['id']
    friend_type = (friend_name, friend_id)
    friend_list.append(friend_type)

  return friend_list

# print(f'{access_friend(char_results)}')

####ACCESS_ENEMY####
# returns list of dictionaries. Dictionary access key "name" (possibly need ID?)
def access_enemy(dict_results):
  """Returns a list of tuples containing character's enemy and respective IDs."""
  enemy = dict_results['character_enemies']
  enemy_list = []
  for enemy in enemy:
    # print(enemy)
    enemy_name = enemy['name']
    enemy_id = enemy['id']
    enemy_char = (enemy_name, enemy_id)
    enemy_list.append(enemy_char)

  return enemy_list

# print(f'{access_enemy(char_results)}')
####ACCESS_TEAMS####
# returns list of dictionaries. Dictionary access key name "name", (possibly need ID?)
def access_team(dict_results):
  """Accesses teams character is associated with and returns tuple pair consisting of team name and team ID."""
  teams = dict_results['teams']
  team_list = []
  for team in teams:
    # print(team)
    team_name = team['name']
    team_id = team['id']
    team_type = (team_name, team_id)
    team_list.append(team_type)

  return team_list

####ACCESS_FIRST_APPEARANCE####
# returns dictionary, access key "name", (possibly need "id", and "issue_number"?)
def access_firstAppearance(dict_results):
  """Extracts dictionary key values for 'first_appearance', returns new dictionary consisting of comic issue 'name', 'id', 'issue_number'."""
  first_appearance = dict_results['first_appeared_in_issue']
  first_appearance_data = {}

  # print(first_appearance)

  first_appearance_issue = first_appearance['name'] 
  issue_id = first_appearance['id']
  issue_number = first_appearance['issue_number']

  first_appearance_data['name'] = first_appearance_issue
  first_appearance_data['issue_id'] = issue_id
  first_appearance_data['issue_number'] = issue_number
    

  return first_appearance_data

####ACCESS_APPEARANCE_COUNT####
# returns integer
def access_appearanceCount(dict_results):
  """Returns number of character comic issue appearances."""
  appearance_count = dict_results['count_of_issue_appearances']

  return appearance_count

####ACCESS_ISSUE_CREDITS####
# returns list of dictionaries. Access key "name" (possibly need "id")
def access_comicIssues(dict_results):
  """Returns dictionary containing comic issue information character has been featured in."""
  comic_issues =  dict_results['issue_credits']
  comic_issue_data = []
  for comic_issue in comic_issues:
    # print(comic_issue)
    # comic_issue_dict = {}

    # comic_issue_name = comic_issue['issue_name']
    # comic_issue_id = comic_issue['id']

    # comic_issue_dict['issue_name'] = comic_issue_name
    # comic_issue_dict['issue_id'] = comic_issue_id

    # comic_issue_data.append(comic_issue_dict)
    comic_issue_id = comic_issue['id']
    comic_issue_data.append(comic_issue_id)
  
  return comic_issue_data


def access_creator(dict_results):
  """Extracts a character's creator name(s) and return as a list."""
  creator = dict_results['creators']
  creator_list = []
  for creator in creator:
    creator_name = creator['name']
    creator_list.append(creator_name)
  # print(f'creator: {creator_list}')
  return creator_list

# creators = access_creators(char_results)
# print(creators)

# print('os.listdir(directory)', os.listdir(directory))

char_dicts = []
for char_file in os.listdir(directory):
  # f is a single file
  f = os.path.join(directory, char_file)
  # print(char_file)
  print('f', f)
  if os.path.isfile(f):
    # reads JSON file for character
    json_string = open(f).read()

  # returns JSON file as python dictionary
  json_dict = (json.loads(json_string))

  # accesses 'results' and returns dictionary containing only relevant information
  char_results = json_dict['results']


    
  character_dictionary = {}
  id = access_comicvineID(char_results)
  image = access_image(char_results)
  name = access_name(char_results)
  real_name = access_realName(char_results)
  alias = access_alias(char_results)
  origin = access_origin(char_results)
  gender = access_gender(char_results)
  biography = access_biography(char_results)
  power = access_power(char_results)
  friend = access_friend(char_results)
  enemy = access_enemy(char_results)
  team = access_team(char_results)
  first_appearance = access_firstAppearance(char_results)
  appearance_count = access_appearanceCount(char_results)
  comic_issue = access_comicIssues(char_results)
  creator = access_creator(char_results)

  character_dictionary['id'] = id
  character_dictionary['image'] = image
  character_dictionary['name'] = name
  character_dictionary['real_name'] = real_name
  character_dictionary['alias'] = alias 
  character_dictionary['gender'] = gender
  character_dictionary['origin'] = origin
  character_dictionary['biography'] = biography
  character_dictionary['power'] = power
  character_dictionary['friend'] = friend
  character_dictionary['enemy'] = enemy
  character_dictionary['team'] = team
  character_dictionary['first_appearance'] = first_appearance
  character_dictionary['appearance_count'] = appearance_count
  character_dictionary['comic_issue'] = comic_issue
  character_dictionary['creator'] = creator

  char_dicts.append(character_dictionary)


  with open(f"data/characters_reformatted/{char_file}", "w") as outfile:
    json.dump(character_dictionary, outfile, indent=4)


# for char in char_dicts:
#   print(f'charid: {char["id"]}')


# turn dict into JSON file 