import csv
import json
import os

filename = f"../data/YJ_characters/all_YJ_characters.csv"

def extract_YJchars(filedirectory_name):
  """Appends YJ character names from the CSV file containing them."""

  YJ_chars = []
  filename = filedirectory_name
  # print(filename)
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      # print(''.join(row).rstrip())
      YJ_chars.append(''.join(row).rstrip())
    
  return YJ_chars

YJ = extract_YJchars(filename)
jsonfile = '../data/comicvineAPI_DC.json'

def find_matching_values(list_of_names, json_dict):
  """Iterates over list of YJ names and for each name, will iterate over json_dict and check if dictionary contains a key 'name' with the same value as the current name in the outer loop. If match is found, will append dictionary to 'matching_values' list and if match not found, appends to 'not_matching_values. """

  f = open(json_dict)
  data = json.load(f)
  access_results = data['results']
  access_characters = access_results['characters']
  print(access_characters)

  matching_values = []
  not_matching_values = []

  for name in list_of_names:
    match_found = False
    # print("*"*300)
    # print("name:", name)
    # print("*"*300)
    for dictionary in access_characters:
      # if dictionary['name'] in name: # or name.__contains__(dictionary['name'].strip()): # in name:
      if name in dictionary['name']:
        matching_values.append(dictionary)
        match_found = True
        break

    if not match_found:
      not_matching_values.append(name)

  matching_values = sorted(matching_values, key=lambda x: x['name'].strip())
  not_matching_values = sorted(not_matching_values)



  return [matching_values, not_matching_values]

matching_values, not_matching_values = find_matching_values(YJ, jsonfile)

print(f"Matching values: {matching_values}")
print("*"*100)
print(f"Not matching values: {not_matching_values}")





