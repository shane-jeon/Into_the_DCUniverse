"Drop database/Create database/ Create tables/ Populate database with data, using data from JSON files from data folder."

import os
import json
import crud
import model
# import server
import run
# from dict_reform import *

# from modules.dict_reform import *
os.system("dropdb characters")
os.system("createdb characters")

model.connect_to_db(run.app)
model.db.create_all()

directory = 'data/characters'

char_dicts = []

for char_file in os.listdir(directory):
  # f is a single file
  f = os.path.join(directory, char_file)
  # print('f', f)
  if os.path.isfile(f):
    # reads JSON file for character
    json_string = open(f).read()
    # print('json_string', json_string)

  # returns JSON file as python dictionary
  char_results = json.loads(json_string)
  # json_dict = json.loads(json_string)
  # print('json_dict', json_dict)

  # accesses 'results' and returns dictionary containing only relevant information
  # char_results = json_dict['results']
  # print('char_results', char_results)
    
  character_dictionary = {}

  id = char_results['id']
  # print(f'id:::::: {id}')
  image = char_results['image']
  # image = access_image(char_results)
  name = char_results['name']
  # name = access_name(char_results)
  real_name = char_results['real_name']
  # real_name = access_realName(char_results)
  alias = char_results['alias']
  # alias = access_alias(char_results)
  gender = char_results['gender']
  # gender = access_gender(char_results)
  origin = char_results['origin']
  # origin = access_origin(char_results)
  biography = char_results['biography']
  # biography = access_biography(char_results)
  power = char_results['power']
  # # changed power plurality
  # power = access_power(char_results)
  friend = char_results['friend']
  # friend = access_friend(char_results)
  enemy = char_results['enemy']
  # enemy = access_enemy(char_results)
  team = char_results['team']
  # team = access_team(char_results)
  # first_appearance = char_results['first_appearance']
  # first_appearance = access_firstAppearance(char_results)
  appearance_count = char_results['appearance_count']
  # appearance_count = access_appearanceCount(char_results)
  comic_issue = char_results['comic_issue']
  # comic_issue = access_comicIssues(char_results)
  creator = char_results['creator']
  # # changed creator plurality
  # creator = access_creator(char_results)


  # print(f'creator: {creator}, id: {id}, name: {name}')
  # print("*"*30)
  # print(f'comic issue {comic_issue}')
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
  # character_dictionary['first_appearance'] = first_appearance
  character_dictionary['appearance_count'] = appearance_count
  character_dictionary['comic_issue'] = comic_issue
  character_dictionary['creator'] = creator

  
  char_dicts.append(character_dictionary)
  # print(f'character_dictionary {character_dictionary}')

# 12/29/2022 --> will need to create new dictionary to hold results from API request to more easily seed database
characters_in_db = []


for char in char_dicts:

  id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, appearance_count, comic_issue, creator = (
    # character_creator,
    char['id'],
    char['image'],
    char['name'],
    char['real_name'],
    char['alias'],
    char['gender'],
    char['origin'],
    char['biography'],
    char['power'],
    char['friend'],
    char['enemy'],
    char['team'],
    # char['first_appearance'],
    char['appearance_count'],
    char['comic_issue'],
    char['creator'],
  )
  # print('*'* 800)
  # print(id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, first_appearance, appearance_count, comic_issue, creator)
  # db_character = crud.create_character(id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, first_appearance, appearance_count, comic_issue, creator)
  db_character = crud.create_character(id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, appearance_count, comic_issue, creator)

  characters_in_db.append(db_character)





# TROUBLESHOOTING 10/25/2022
  # iterate through all values in json file 
  # assign variables to dictionary access contents

  # getting error 'can't dapt type 'dict''
    # blocker resolved: it's because biography is a dictionary,
    # look into this later'
  # error with 'name' column not in relation with something
    # just dropdb and createdb
  # look into why calling crud function just returns <function> i forgot
      # have to be in the database to use said functions (remember to store calls in variables)