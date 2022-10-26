"Drop database/Create database/ Create tables/ Populate database with data, using data from JSON files from data folder."

import os
import json
import crud, model, server

os.system("dropdb characters")
os.system("createdb characters")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/superHeroAPI_DC.json') as f:
  char_data = json.loads(f.read())
  len_test = print('length of list: ', len(char_data))

def create_biography(char_data, char):
  """Create a character's biography summary."""
  
  # putting a pin on this ** 10/26/2022 **
  # char_gender_key = char_data[char]['appearance']['gender'] 
  # genders = {'female': ['she', 'her', 'hers'], 'male': ['he', 'him', 'his'], 'nonbinary': ['they', 'them', 'their']}

  # for gender in genders:
  #   if char_gender_key == gender:

  char_dict = char_data[char]
  char_name = char_dict['name']
  biography_access = char_dict['biography']
  char_stats = char_dict['powerstats']
  char_bio = f'''{char_name}, also known as {biography_access['full-name']} first appeared in {biography_access['first-appearance']} and is originally based in {char_dict['work']['base']}. {char_name}'s professional and personal affiliations include '{char_dict['connections']['group-affiliation']}' and
  '{char_dict['connections']['relatives']}', respectively. {char_name}'s stats are as below:
  
             {char_name}'s POWERSTATS  
  +----------------------------------------------+
    Intelligence: {char_stats['intelligence']}, 
    Strength: {char_stats['strength']},         
    Speed: {char_stats['speed']},               
    Durability: {char_stats['durability']},     
    Power: {char_stats['power']},               
    Combat: {char_stats['combat']}              
  +----------------------------------------------+
  '''
  return char_bio


chars_in_db = []

for char in char_data:
  # print(char_data[char])
  print("char: ", char)
  char_id, name, alignment, biography = (
    char_data[char]['id'], 
    char_data[char]['name'],
    char_data[char]['biography']['alignment'],
    create_biography(char_data, char), 
  )


  db_char = crud.create_char(char_id, name, alignment, biography)
  chars_in_db.append(db_char)


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