import csv
import json
import os

filename = f"../data/YJ_characters/all_YJ_characters.csv"

def extract_YJchars(filedirectory_name):

  YJ_chars = []
  filename = filedirectory_name
  # print(filename)
  with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      print(''.join(row).rstrip())
      YJ_chars.append(''.join(row).rstrip())
    
  return YJ_chars


YJ = extract_YJchars(filename)


jsonfile = '../data/characters/comicvineAPI_DC.json'



f = open('../data/comicvineAPI_DC.json')

data = json.load(f)

# data_dict = json.loads('comicvineAPI_DC.json')
# print(data_dict[:5])
# for name in YJ:
#   if 

access_results = data['results']
access_characters = access_results['characters']

found = []
not_found = []
count = 0
for i in range(len(YJ)):
  for j in range(len(access_characters)):
    if YJ[i].rstrip() in access_characters[j]['name']:
      found.append((access_characters[j]['name'], access_characters[j]['id']))
    else:
      not_found.append(YJ[i])

  count += 1
  print(count)

print(f"FOUND {found}")
print('*'*200)
print(f"NOT FOUND {set(not_found)}")

 

