"Drop database/Create database/ Create tables/ Populate database with data, using data from JSON files from data folder."

import os
import json
import crud
import model
import server
from dict_reform import *
os.system("dropdb characters")
os.system("createdb characters")

model.connect_to_db(server.app)
model.db.create_all()

directory = 'data/characters'

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

  id = access_comicvineID(char_results)
  print(f'id:::::: {id}')
  image = access_image(char_results)
  name = access_name(char_results)
  # real_name = access_realName(char_results)
  # alias = access_alias(char_results)
  gender = access_gender(char_results)
  # species = access_species(char_results)
  biography = access_biography(char_results)
  # changed power plurality
  power = access_power(char_results)
  friend = access_friend(char_results)
  enemy = access_enemy(char_results)
  # team = access_team(char_results)
  # first_appearance = access_firstAppearance(char_results)
  # appearance_count = access_appearanceCount(char_results)
  # issue_credit = access_issueCredit(char_results)
  # changed creator plurality
  creator = access_creator(char_results)

  print(f'creator: {creator}, id: {id}, name: {name}')
  character_dictionary['id'] = id
  character_dictionary['image'] = image
  character_dictionary['name'] = name
  character_dictionary['real_name'] = real_name
  character_dictionary['alias'] = alias 
  character_dictionary['gender'] = gender
  character_dictionary['species'] = species
  character_dictionary['biography'] = biography
  character_dictionary['power'] = power
  character_dictionary['friend'] = friend
  character_dictionary['enemy'] = enemy
  character_dictionary['team'] = team
  character_dictionary['first_appearance'] = first_appearance
  character_dictionary['appearance_count'] = appearance_count
  character_dictionary['issue_credit'] = issue_credit
  character_dictionary['creator'] = creator

  char_dicts.append(character_dictionary)
  # print(f'character_dictionary {character_dictionary}')

# 12/29/2022 --> will need to create new dictionary to hold results from API request to more easily seed database
characters_in_db = []
# print(f'CHAR DICTS: {char_dicts}')
# for character in char_dict:
for char in char_dicts:
  # print(character)
  print(f"ID: {char['id']}, NAME: {char['name']}")
  id, image, name, real_name, alias, gender, species, biography, power, friend, enemy, team, first_appearance, appearance_count, issue_credit, creator = (
    # character['creator'][1]['name'],
    # character_creator,
    char['id'],
    char['image'],
    char['name'],
    char['real_name'],
    char['alias'],
    char['gender'],
    char['species'],
    char['biography'],
    char['power'],
    char['friend'],
    char['enemy'],
    char['team'],
    char['first_appearance'],
    char['appearance_count'],
    char['issue_credit'],
    char['creator'],
  )

  print(f" NAME CHAR {char['name']}")
  db_character = crud.create_character(id, image, name, real_name, alias, gender, species, biography, power, friend, enemy, team, first_appearance, appearance_count, issue_credit, creator)



  characters_in_db.append(db_character)

# model.db.session.add_all(characters_in_db)
# model.db.session.commit()



# def seed_db_comicvine(char_dict):
#   """Seeding available character data from Comicvine API."""

#   id = char_dict['id']
#   char_name = char_dict['name']


# def create_biography(char_data, char):
#   """Create a character's biography summary."""
  
#   # putting a pin on this ** 10/26/2022 **
#   # char_gender_key = char_data[char]['appearance']['gender'] 
#   # genders = {'female': ['she', 'her', 'hers'], 'male': ['he', 'him', 'his'], 'nonbinary': ['they', 'them', 'their']}

#   # for gender in genders:
#   #   if char_gender_key == gender:

#   char_dict = char_data[char]
#   char_name = char_dict['name']
#   biography_access = char_dict['biography']
#   char_stats = char_dict['powerstats']
#   char_bio = f'''{char_name}, also known as {biography_access['full-name']} first appeared in {biography_access['first-appearance']} and is originally based in {char_dict['work']['base']}. {char_name}'s professional and personal affiliations include '{char_dict['connections']['group-affiliation']}' and
#   '{char_dict['connections']['relatives']}', respectively. {char_name}'s stats are as below:
  
#              {char_name}'s POWERSTATS  
#   +----------------------------------------------+
#     Intelligence: {char_stats['intelligence']}, 
#     Strength: {char_stats['strength']},         
#     Speed: {char_stats['speed']},               
#     Durability: {char_stats['durability']},     
#     Power: {char_stats['power']},               
#     Combat: {char_stats['combat']}              
#   +----------------------------------------------+
#   '''
#   return char_bio


# chars_in_db = []

# for char in char_data:
#   # print(char_data[char])
#   print("char: ", char)
#   char_id, name, alignment, biography = (
#     char_data[char]['id'], 
#     char_data[char]['name'],
#     char_data[char]['biography']['alignment'],
#     create_biography(char_data, char), 
#   )


#   db_char = crud.create_char(char_id, name, alignment, biography)
#   chars_in_db.append(db_char)

# 




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