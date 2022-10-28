"""APIs and Requests Library."""

# Translates JSON to a python dictionary (and can convert a dictionary to JSON)
import json
import requests
import jsonpickle

# api_key = "YOUR_ACCESS_TOKEN" #Obtain through https://www.superheroapi.com/, requires Facebook account however
superhero_API_KEY = 1075529179813027

def import_SuperHeroAPI(API_KEY):
  """Gets all available DC Comic characters from SuperHero API."""

  # dictionary for JSON file
  dc_characters = {}

  # loops through all character IDs in SuperHero API
  for i in range(1, 732):
    url = f'https://superheroapi.com/api/{API_KEY}/{i}'
    res = requests.get(url)
    # Displays response success/failure
    print('res:', res)
    # print(res.url)
    superhero_data = res.json()

    # to track progress of API request
    print(f'at superhero ID #{i}')
    # Access returned JSON dictionary with 2 key values to filter out non-DC Comics characters
    if superhero_data['biography']['publisher'] == 'DC Comics':
      # displays as function runs
      name = superhero_data['name']
      print()
      print("*****", name, "*****")
      print()
      if name in dc_characters:
        continue
      else:
        dc_characters[name] = superhero_data

  # gets JSON dictionary
  json_object = json.dumps(dc_characters, indent=4)

  # writes dictionary to JSON file
  with open('example.json', 'w') as outfile:
    outfile.write(json_object)

# cleans up postman downloaded JSON file*
def format_conversion(filename, new_filename):
  """ Transforms incoherent Postman JSON file to readable JSON file.
  Use when terminal GET request keeps returning with 403,
  but Postman GET reqest returns 200 and thus have to download file from Postman."""

  with open(filename) as data_file:
    data = json.load(data_file)

  json_object = json.dumps(data, indent=4)

  with open(new_filename, 'w') as outfile:
    outfile.write(json_object)



def get_comicvine_API(filename, API_KEY, your_header, new_filename):
  """Uses data from JSON file obtained from 'format_conversion()' function to make individual API get requests to comicvine API.
  HOWEVER, comicvine has request limit of 100 per hour. ****need to add code to alleviate/automate that."""

  with open(filename) as openfile:
  # with open('data/comicvineAPI_DC.json') as openfile:
  # read as dictionary
    char_dict = json.loads(openfile.read())
  
  # Access character list within 'characters' dictionary
  characters = char_dict['results']['characters']

  # list to hold all character ids that will eventually iterate through
  char_ids = []

  # extract 'id' from every character in comicvineAPI_DC.json and append to char_ids list
  for i, character in enumerate(characters):
    char_ids.append(characters[i]['id'])

  headers = {your_header}
  # headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'}

  # to track number of get requests made
  counter = 0

  for char_id in char_ids:
    # URL = f'https://www.comicvine.com/api/character/4005-1699/?api_key=6028f8ab23892d424a31b9845b1c36ed4f737523&format=json&field_list=name,real_name,deck,description,powers,movies,issue_credits,issues_died_in,id,volume_credits'

    URL = f'https://www.comicvine.com/api/character/4005-{char_id}/?api_key={API_KEY}&format=json&field_list=name,real_name,deck,description,powers,movies,issue_credits,issues_died_in,id,volume_credits'

    response = requests.get(URL, headers=headers)

    # increment counter
    counter += 1

    # visual progress
    print()
    print('*'*20)
    print("at counter: ", counter)
    # ensure url has correct char_id
    print(response.url)
    print('*'*20)
    print()

    # encodes object so response can be serialized
    json_pickle = jsonpickle.encode(response)
    
    # creates dictionary
    json_object = json.dumps(json_pickle, indent=4)
    # # json_object = json.loads(response.json)
    # # json_object = response.json()

    # create JSON file to store all imported data
    with open(new_filename, 'w') as outfile:
    # with open('comicvineChar_API.json', 'w') as outfile:
      outfile.write(json_object)



# * please note that while the code below is logically functional, it keeps returning response 403. For some reason POSTMAN GET requests work just fine. Should you run into this error, comment out the following function (as of 10/26/2022 I have not completed the function, will return to it later. ) and use def format_conversion instead. Will make a how-to follow up in how a user can get access to said file.

# ******FIGURED OUT API REQUEST ISSUE W/BROWSER V. POSTMAN 10/27/2022, FIX CODE LATER
# *****RETURN TO THIS (had enough of API and coding stuff for today. )


#  ****************************************************************
# API FUNCTION CALLS
# import_SuperHeroAPI(superheroAPI_KEY)
# format_conversion('postman/data/POSTMAN_comicvine.json', 'data/comicvineAPI_DC.json')
#  ****************************************************************







# ***** 10/26/2022 HAD TO SCRAP THIS API CODE....FOR SOME REASON I KEPT GETTING BACK RESPONSE 403 BUT WHEN I RAN THE GET REQUEST ON POSTMAN IT WORKED JUST FINE. JUST CLEANED UP DOWNLOADED JSON FILE FROM POSTMAN AND LEAVING IT AT THAT.


# comicvine_API_KEY = '6028f8ab23892d424a31b9845b1c36ed4f737523'

# def import_comicvineAPI(API_KEY):
#   """Retrieve all comic book issues/volumes from publisher DC Comics. Also getting characters not listed in SuperHeroAPI. """
#   #  the issue with trying to import both.....is I might get duplicates....so should I just use comic vine API?? In the mean time, I'll just make the REST API call to create the JSON file and will review and decide from there


#   payload = { 'api_key': API_KEY,
#               'format': 'json',
#               'field_list': 'characters'}

#   # URL for publisher
#   pub_URL = 'https://comicvine.gamespot.com/api/publisher/4010-10/'

#   # API GET request
#   res = requests.get(pub_URL, params=payload)
#   print()
#   print('************************')
#   print('res.url',res.url)
#   print('************************')
#   print()


#   # dc_characters = {}

#   # for i in range(len(character_list)):
#   #   print(f'at character num {i}')


#   #   # gets results into json()
#   #   PUB_data = res.json()

#   #   print(f'at superhero #{i}')

#   #   name = dc_characters['name'] 

#   #   print()
#   #   print("*****", name, "*****")
#   #   print()

#   #   # gets JSON dictionary
#   #   json_object = json.dumps(dc_characters, indent=4)

#   # writes dictionary to JSON file
#   with open('comicvineAPI_DC.json', 'w') as outfile:
#     outfile.write(json_object)

# import_comicvineAPI(comicvine_API_KEY)








#  *************************************************************************  #
                            # API FUNCTION CALLS
# import_SuperHeroAPI(superheroAPI_KEY)

#  *************************************************************************  #



# JSON/API Reference Information

# JSON methods
# json.loads() - loads JSON from a given string
# json.dumps(dictionary) - converts a dictionary to a JSON string
  # difference --> "s", stands for "string"
# json.load(open('file.json')) - loads JSON from a file
# json.dump(dictionary, open('file.json', 'w')) - writes a dictionary to a JSON file

# Superhero API
    #  while this API def has all heros (i think), doesn't contain all villians
# https://superheroapi.com/api/access-token


# Personal easy access URL:
  # https://superheroapi.com/api/1075529179813027

# GET methods (available endpoints)
# API Hierarchy
# from '/id' - Search by character id. Returns all info of the character.
  # following returns JSON Array
  # '/id/powerstats'
  # '/id/biography'
  # '/id/apperance'
  # '/id/work'
  # '/id/connections'
  # '/id/image'

# SEARCH character by name, returns character ID
# '/search/name'

# to make a GET request (simple search)

# function that can take in string w/URL request
# --> res = requests.get('https://superheroapi.com/api/1075529179813027/search/{param}')
    # should get <Response [200]>

# res.json is an instance method, will automatically turn JSON into python dictionary
# --> search_results = res.json()

# Requests - creates query string for user
# res.get takes in second argument (params)
# params - should be a dictionary containing key-value pairs user wants to send in request

# for '/search/name' # USING PAYLOAD ADDs "SEARCH" TO THE REQUEST URL
  # api_key = 1075529179813027
  # payload = {'name': 'x'}
  # res = requests.get('https://superheroapi.com/api/1075529179813027', params=payload)
  # print(res.url) --> returns URL w/queries
  # superhero_char = res.json()
  # json.dumps(superhero_char) --> JSON query

# to READ and WRITE JSON file
  # using json.dumps(dictionary, indent), converts dictionary into JSON object
    # takes 2 parameters: 1) name of dictionary to be converted , 2) number of units for indentation
  # using json.dump(dictionary, file pointer) --> directly writes dictionary to a file in the form
    # of JSON without needing to convert into actual JSON object
# *However this method will return dictionary as one long string, no indentation*


