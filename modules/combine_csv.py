import csv

def extract_YJ_characters():
  alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  names = []

  for letter in alph:
    filename = f"../data/YJ_characters/YJcharacters{letter}.csv"
    print(filename)
    with open(filename, 'r') as csvfile:
      csvreader = csv.reader(csvfile)
      fields = next(csvreader)
      
      for row in csvreader:
        names.append([row[1]])
  return names

def create_whole_file(names):
  with open('../data/YJ_characters/all_YJ_characters.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(names)

names = extract_YJ_characters()
create_whole_file(names)

