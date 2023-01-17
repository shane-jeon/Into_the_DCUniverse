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

print(YJ)
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
result = [found.append(item['name']) for item in access_characters if item['name'] in YJ]

print(f"found {found}")
print("*"*100)

sorted_found = sorted(found)
# print(sorted_found)


not_found = [item for item in YJ if item not in sorted_found]
print(f'not_found {not_found}')
# no_results = [not_found.append(YJ[i]) for i, item in enumerate(found) if YJ[i] not in found]
# print(no_results)




# for i in range(len(YJ)):
#   for j in range(len(access_characters)):
#     if YJ[i].rstrip() in access_characters[j]['name']:
#       found.append((access_characters[j]['name'], access_characters[j]['id']))
#     else:
#       not_found.append(YJ[i])

  # count += 1
  # print(count)
# found = []
# not_found = []
# count = 0

# for i in range(len(access_characters)):
#   for j in range(len(YJ)):
#     if YJ[j].rstrip() in access_characters[i]['name']:
#       found.append((access_characters[i]['name'], access_characters[i]['id']))
#     else:
#       not_found.append(YJ[i])

#   count += 1
#   print(count)


# print(f"FOUND {found}")
# print('*'*200)
# print(f"NOT FOUND {set(not_found)}")

 

