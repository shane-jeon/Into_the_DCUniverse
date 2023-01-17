"""APIs and Requests Library."""

# Translates JSON to a python dictionary (and can convert a dictionary to JSON)
import json
import requests
import jsonpickle
import time
import math
# from progressBarTemp import progress_bar, track_remaining_time

# api_key = "YOUR_ACCESS_TOKEN" #Obtain through https://www.superheroapi.com/, requires Facebook account however
superhero_API_KEY = 1075529179813027
comicvine_API_KEY = '6028f8ab23892d424a31b9845b1c36ed4f737523'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'

def comicvine_get_request(your_UA, API_KEY, resource, fields, new_filename):
  """A general get request for comic vine. 
  
  Parameters explained respectively, your user_agent information, your API key, resource: what information you are requesting (character, publisher, etc.), fields: what information you want to get back, new_filename: name of JSON file"""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # required information needed
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : fields
  }

  # URL for API request
  URL = f'https://comicvine.com/api/{resource}/4010-10/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)

def character_JSON_request(your_UA, API_KEY, char_id, new_filename):
  """A general get request for comic vine. 
  
  Parameters explained respectively, your user_agent information, your API key, resource: what information you are requesting (character, publisher, etc.), fields: what information you want to get back, new_filename: name of JSON file"""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # hard coding fields
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : 'id,image,name,real_name,aliases,gender,origin,deck,powers,character_friends,character_enemies,teams,first_appeared_in_issue,count_of_issue_appearances,issue_credits,creators'
  }

  # URL for API request
  URL = f'https://comicvine.com/api/character/4005-{char_id}/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'data/characters/{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)



# fields requested in POSTMAN: real_name,id,deck,description,gender,origin,powers,teams,creators,first_appeared_in_issue,count_of_issue_apperances,issue_credits,volume_credits,issues_died_in,movies,story_arc_credits,api_detail_url

# new field list created because API files did not contain information I needed for CRUD functions and and seed_db: 
  # id, name, gender, deck, description, powers, creators
# char_fields = 'id,name,gender,deck,powers,creators'

# JOHN CONSTANTINE
# character_JSON_request(user_agent, comicvine_API_KEY, 3329,'john_constantine')
# HARLEY QUINN
# character_JSON_request(user_agent, comicvine_API_KEY, 1696,'harley_quinn')
# ZATANNA
# character_JSON_request(user_agent, comicvine_API_KEY, 5691, 'zatanna')
# ORPHAN (Cassandra Cain)
# character_JSON_request(user_agent, comicvine_API_KEY, 65230, 'cassandra_cain')
# BLACK CANARY
# character_JSON_request(user_agent, comicvine_API_KEY, 1689, 'black_canary')
# Jackson Hyde (AQUALAD)
# character_JSON_request(user_agent, comicvine_API_KEY, 71494, 'jackson_hyde_aqualad')
# POISON IVY
# character_JSON_request(user_agent, comicvine_API_KEY, 1697, 'poison_ivy')
# RAVEN
# character_JSON_request(user_agent, comicvine_API_KEY, 3584, 'raven')
# NIGHTWING 146057
# character_JSON_request(user_agent, comicvine_API_KEY, 146057, 'nightwing')
# # STARFIRE 62757
# character_JSON_request(user_agent, comicvine_API_KEY, 62757, 'startfire')
# # SPOILER (STEPHANIE BROWN) 6156
# character_JSON_request(user_agent, comicvine_API_KEY, 6156, 'stephanie_brown')
# # BARBARA GORDON (BATGIRL/ORACLE) 5368
# character_JSON_request(user_agent, comicvine_API_KEY, 5368, 'barbara_gordon')
# # PHANTOM STRANGER 116997
# character_JSON_request(user_agent, comicvine_API_KEY, 116997, 'phantom_stranger')
# # KLARION 11976
# character_JSON_request(user_agent, comicvine_API_KEY, 11976, 'klarion')
# # DEATHSTROKE 3588
# character_JSON_request(user_agent, comicvine_API_KEY, 3588, 'deathstroke')
# # ARROWETTE 1685
# character_JSON_request(user_agent, comicvine_API_KEY, 1685, 'arrowette')
# # AMANDA WALLER 4920
# character_JSON_request(user_agent, comicvine_API_KEY, 4920, 'amanda_waller')
# # DEADSHOT 5763
# character_JSON_request(user_agent, comicvine_API_KEY, 5763, 'deadshot')
# # AMAZO 3737
# character_JSON_request(user_agent, comicvine_API_KEY, 3737, 'amazo')
# # PROFESSOR IVO 22015
# character_JSON_request(user_agent, comicvine_API_KEY, 22015, 'professor_ivo')
# # T.O. Morrow 22016
# character_JSON_request(user_agent, comicvine_API_KEY, 22016, 'to_morrow')
# # RED TORNADO 1688
# character_JSON_request(user_agent, comicvine_API_KEY, 1688, 'red_tornado')
# # HUNTRESS 1690
# character_JSON_request(user_agent, comicvine_API_KEY, 1690, 'huntress')
# # JAIME REYES (BLUE BEETLE) 4438
# character_JSON_request(user_agent, comicvine_API_KEY, 4438, 'blue_beetle')
# # LOR-ZOD 42372
# character_JSON_request(user_agent, comicvine_API_KEY, 42372, 'lor_zod')
# # KON-EL (SUPERBOY) 1686
# character_JSON_request(user_agent, comicvine_API_KEY, 1686, 'superboy')
# # JADE 3406 //wrong jade
# CHESHIRE 2537
# character_JSON_request(user_agent, comicvine_API_KEY, 2537, 'cheshire')
# # ROY HARPER 3404
# character_JSON_request(user_agent, comicvine_API_KEY, 3404, 'roy_harper')
# # ROULETTE 19004
# character_JSON_request(user_agent, comicvine_API_KEY, 19004, 'roulette')
# # KITE-MAN 34169
# character_JSON_request(user_agent, comicvine_API_KEY, 34169, 'kite_man')
# # KING SHARK 17772
# character_JSON_request(user_agent, comicvine_API_KEY, 17772, 'king_shark')
# # CLAYFACE (HAGEN) 35188
# character_JSON_request(user_agent, comicvine_API_KEY, 35188, 'clayface_hagen')
# # BLACK ADAM 4916
# character_JSON_request(user_agent, comicvine_API_KEY, 4916, 'black_adam')
# # COUNT VERTIGO 19006
# character_JSON_request(user_agent, comicvine_API_KEY, 19006, 'count_vertigo')
# # BEAST BOY 47265
# character_JSON_request(user_agent, comicvine_API_KEY, 47265, 'beast_boy')
# # WHISPER A'DAIRE 44355
# character_JSON_request(user_agent, comicvine_API_KEY, 44355, 'whisper_adaire')
# # CYBORG 2388
# character_JSON_request(user_agent, comicvine_API_KEY, 2388, 'cyborg')
# # BLACK LIGHTNING 10994
# character_JSON_request(user_agent, comicvine_API_KEY, 10994, 'black_lightning')
# # VANDAL SAVAGE 5722
# character_JSON_request(user_agent, comicvine_API_KEY, 5722, 'vandal_savage')
# # JOHN STEWART 10451
# character_JSON_request(user_agent, comicvine_API_KEY, 10451, 'GL_john_stewart')
# # JESSICA CRUZ 89628
# character_JSON_request(user_agent, comicvine_API_KEY, 89628, 'GL_jessica_cruz')
# # NUBIA 34121
# character_JSON_request(user_agent, comicvine_API_KEY, 34121, 'nubia')
# # SPECTRE 2361
# character_JSON_request(user_agent, comicvine_API_KEY, 2361, 'spectre')
# # LIVEWIRE 4678
# character_JSON_request(user_agent, comicvine_API_KEY, 4678, 'livewire')

#  
def comic_JSON_request(your_UA, API_KEY, resource, fields, new_filename):
  """Get information of comic issues each character has appeared in."""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # required information needed
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : fields
  }

  # URL for API request
  URL = f'https://comicvine.com/api/{resource}/4010-10/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'data/comics{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)


# comic_JSON_request(user_agent, comicvine_API_KEY, 'comic', 'id,name,person_credits,volume,deck,description,cover_date')


def series_JSON_request(your_UA, API_KEY):
  """Get list of characters from television series YJ."""

  # needed to get response 200 from API request
  headers = { 'User-Agent' : your_UA}

  # required information needed
  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : 'character_credits'
  }

  # URL for API request
  URL = f'https://comicvine.com/api/series/4075-33/'

  # holds information from get request
  response = requests.get(URL, params=payload, headers=headers)

  # converts to JSON dictionary I think
  json_object = json.dumps(response.json(), indent=3)

  with open(f'data/tvseriesYJ.json', 'w') as outfile:
    outfile.write(json_object)

series_JSON_request(user_agent, comicvine_API_KEY)
# iterate through each file
# get characters' comic ids
# limit 100 requests per hour
# fields: cover_date, deck, description, id, name, person_credits, volume

def alphabetize_JSON_dict(filename, new_filename):
  """Retrieves dictionary from JSON file. Alphabetizes data."""

  # story_arcs = []
  story_arcs = {}

  with open(filename) as openfile:
    JSON_dict = json.loads(openfile.read())

  access_arcs = JSON_dict['results']['story_arcs']

  for arc in access_arcs:
    arc_id = arc['id']
    arc_name = arc['name']

    story_arcs[arc_id] = arc_name

    # story_arcs.append(arc_id, arc_name)

    # sort by value
    sort_by_value = dict(sorted(story_arcs.items(), key=lambda item: item[1]))
  # print(story_arcs)
  print(sort_by_value)

  # serialize JSON from dictionary
  json_object = json.dumps(sort_by_value, indent = 4)

  with open(f'{new_filename}.json', 'w') as outfile:
    outfile.write(json_object)

  # create list to store tuples containing concept id and name
  # open JSON file
  # access the list of story arcs
  # itereate through list of story arcs, to store the arc_id and arc_name in the tuple
  # append the tuple to the list created to store them
  # iterate through list of tuples, accessing index 1 of each tuple

  # OR
  # 
# alphabetize_JSON_dict('data/DC_story_arcs.json', 'data/alphabetized_DC_story_arcs.json')
# #####################################################
# #####################################################
# ##################################################### 
# DEVELOPMENT FUNCTIONS, GETS SAMPLE DATA
# #####################################################
# #####################################################
# ##################################################### 


def get_info_from_charID(filename, API_KEY, your_header):
  """Gets 99 character IDs from JSON file generated from API get request to 'publisher' endpoint, retrieving detailed character information.
  
  Currently daily_maximum is set to a low number for development purposes."""

  with open(filename) as openfile:
  # read as dictionary
    char_dict = json.loads(openfile.read())

  # Access character list within 'characters' dictionary
  characters = char_dict['results']['characters']

  # dictionary to hold all key(character id)/value(character name) pairs to iterate through
  char_ids = {}

  # Adding character IDs as key and character names as value
  for i in range(len(characters)):
    char_ids[characters[i]['id']] = characters[i]['name']

  headers = { 'User-Agent' : your_header}
  # headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'}

  payload = { 'api_key' : API_KEY,
              'format' : 'json',
              'field_list' : 'name,real_name,id,deck,description,gender,origin,powers,teams,creators,first_appeared_in_issue,count_of_issue_apperances,issue_credits,volume_credits,issues_died_in,movies,story_arc_credits,api_detail_url'
  }

  # to track number of get requests made
  req_count = 0

  # just need sample data
  hourly_maximum = 5

  # ACTUAL comicvine hourly maximum
  # hourly_maximum = 100

  # for visual tracking (deployment stage, whenever that happens, today: 10/28/2022)
  # daily_maximum = 2400

  for char_id, name in char_ids.items():

    print('char_id: ', char_id)
    print('name: ', name)

    # increment req_count
    req_count += 1

    # will only make MAXIMUM API get requests per hour and 5 seconds (to wait until request limit resets for the hour)
    if req_count % hourly_maximum == 0:
      current_id = char_id
      print("Paused at: ", current_id)
      time.sleep(3605)
      continue

    # check your comicvine Current API Usage:
    # https://comicvine.gamespot.com/api/

    URL = f'https://www.comicvine.com/api/character/4005-{char_id}/'

    response = requests.get(URL, params=payload, headers=headers)

    # visual progress
    print()
    print('*'*20)
    print()
    print(f"""Current request count at: {req_count},
            At character: {name},
            Character ID: {char_id},
            Response URL: {response.url}""")
    print()
    print('*'*20)
    print()

    # serializing json
    json_object = json.dumps(response.json(), indent=3)

    print(name)
    char_name = name.replace(" ", "_").lower()
    print(char_name)
    # writing to json file
    with open(f'{char_name}.json', 'w') as outfile:
      outfile.write(json_object)


# get_info_from_charID('data/comicvineAPI_DC.json', comicvine_API_KEY, my_header)

# #####################################################
# #####################################################
# ##################################################### 
# DEVELOPMENT FUNCTIONS, GETS SAMPLE DATA
# #####################################################
# #####################################################
# ##################################################### 

# ***** ROOM FOR IMPROVEMENT HERE, CAN MAKE IT MORE GENERALIZED AND MORE BROADLY APPLICABLE
# ***** get to after I get all data needed in 8 days (today is 10/28/2022)
# ********* Just realized I really don't need 19709 worth of character information if I'm still creating the project and only need some test data...
# also learned as of 4:00pm that my request isn't returning a proper JSON file!!!! wait do I need to create a new json file for each character....???? (its 4:18PM right now)
def get_comicvine_API(filename, API_KEY, your_header, new_filename):
  """Uses data from JSON file obtained from 'format_conversion()' function to make individual API get requests to comicvine API.
  HOWEVER, comicvine has request limit of 100 per hour. So a timer has been included to cycle through 100 requests per hour. Total time should take 8 days to retrieve all information."""

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

  headers = { 'User-Agent' : your_header}
  # headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'}

  # to track number of get requests made
  req_count = 0
  hourly_maximum = 100
  daily_maximum = 2400
  num_ids = len(char_ids)
  # results = []

  for i, char_id in enumerate(char_ids):
    # URL = f'https://www.comicvine.com/api/character/4005-1699/?api_key=6028f8ab23892d424a31b9845b1c36ed4f737523&format=json&field_list=name,real_name,deck,description,powers,movies,issue_credits,issues_died_in,id,volume_credits'

    # increment req_count
    req_count += 1

    # will only make 100 API get requests per hour and 5 seconds (to wait until request limit resets for the hour)
    if req_count % hourly_maximum == 0:
      current_id = char_id
      time.sleep(3605)
      print("Paused at: ", current_id)
      continue

    # check your comicvine Current API Usage:
    # https://comicvine.gamespot.com/api/

    URL = f'https://www.comicvine.com/api/character/4005-{char_id}/?api_key={API_KEY}&format=json&field_list=name,real_name,deck,description,powers,movies,issue_credits,issues_died_in,id,volume_credits'

    response = requests.get(URL, headers=headers)

    # visual progress
    print()
    print('*'*20)
    print()
    print(f"""Current request count at: {req_count},
            At character: {character},
            Character ID: {char_id},
            Response URL: {response.url},
            Days remaining: {num_ids // daily_maximum}""")
    print()
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

# API_KEYS
comicvine_API_KEY = '6028f8ab23892d424a31b9845b1c36ed4f737523'

# other parameter variables
my_header = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0'
#  ****************************************************************
# API FUNCTION CALLS
# import_SuperHeroAPI(superheroAPI_KEY)
# format_conversion('postman/data/POSTMAN_comicvine.json', 'data/comicvineAPI_DC.json')
# get_comicvine_API('data/comicvineAPI_DC.json', comicvine_API_KEY, my_header, 'comicvine_characters.json')
# #  ****************************************************************







# ***** 10/26/2022 HAD TO SCRAP THIS API CODE....FOR SOME REASON I KEPT GETTING BACK RESPONSE 403 BUT WHEN I RAN THE GET REQUEST ON POSTMAN IT WORKED JUST FINE. JUST CLEANED UP DOWNLOADED JSON FILE FROM POSTMAN AND LEAVING IT AT THAT.


# comicvine_API_KEY = '6028f8ab23892d424a31b9845b1c36ed4f737523'

# def get_publisher_characters(API_KEY):
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


# SUPERHERO API
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


# format_conversion('data/character_JSON/requires_reformatting/zatanna.json', 'data/character_JSON/zatanna.json')
