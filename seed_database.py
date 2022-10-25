"Drop database/Create database/ Create tables/ Populate database with data, using data from JSON files from data folder."

import os
import json
import crud, model, server

os.system("dropdb dc_chars")
os.system("createdb dc_chars")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/superHeroAPI_DC.json') as f:
  char_data = json.loads(f.read())
  len_test = print('length of list: ', len(char_data))

chars_in_db = []

for char in char_data:
  # print(char_data[char])
  print("char: ", char)
  char_id, name, alignment = (
    char_data[char]['id'], 
    char_data[char]['name'],
    char_data[char]['biography']['alignment'],
  )


  db_char = crud.create_char(char_id, name, alignment)
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