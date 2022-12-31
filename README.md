# Into the DCUniverse

**Please see txt_files/MVP.md**

_Into the DCUniverse_, a web application that aims to provide an accessible and organized way for users to learn about characters in the DC Comics multiverse by offering recommendations for which comic series to start reading. The application includes a list of all characters, with basic information and a list of apperances in various media, as well as a quiz to help users find recommendations based on their interests.

The project was created to address the difficulty and time-consuming nature of researching the DC Universe and provide a solution for those who may be intimidated by the complexities of the various multiverses, publication eras, and anthologies.

How this project came to be? I was drawn into the DC Franchise through the DC Animated Universe. Soon the animated television shows drew me to animated film, live action film, and finally the comics themselves. However, as a new DC Comics fan, I was incredibly confused with all the multiverses, "Pre & Post" Crisis, different Earths, the reboots that came from new ages...I eventually was able to piece everything together albeit through an arduous process of investigation through wikipedia, fandom wiki, and my own personal media consumption. How wonderful would it have been to go to one website and to have a primer guiding my reading journey of the thousands of comic book series published by DC.

My initial vision was to pack as much information into each character's profile, including the many plotlines belonging to different multiverse versions of a DC character. However, as I began my research and found an API (Comic Vine's API) that provided all the information I needed, I quickly realized that I'd merely be replicating Comic Vine's web application. This vast vision also would prevent me from creating a MVP for quite some time. So I decided to shift focus and reassess the goals of what I wanted to get out of my project. I went back to the roots of my vision and decided I'd create a web application to help those who may be thrown off by the complexities of the DC Universe.

Stay tuned!

model.py

To create the tables needed for my postgreSQL relational database, I required the use of 3 libraries:

- psycopg2 : allows Python to connect with DB
- SQLAlchemy : Needed to work with DB using Python
- Flask-SQLAlchemy : Makes it easier to use SQLAlchemy w/Flask

Working with comicvine API:

- [comicvine API documentation](https://comicvine.gamespot.com/api/documentation)

Need to create an account with [comicvine](https://comicvine.gamespot.com/api/) to get an API key

Making GET Requests:

Start URL with:

"https://comicvine.com/api/"

Endpoints can be found in documentation under 'Resources'.

According to comicvine API developer forum, endpoint "characters" can't be filtered by publisher, so instead you will need to get a list of characters from a publisher.

Important factors in the URL request include:

- Your API key
- Your User-Agent
- Filters, specifically 'format' and 'field_list'
- Endpoints
- IDs

STEP 1: Get a List of Characters by Publisher

We will be using the endpoint 'publisher', so the URL to get all DC Comics characters will be as follows:
"https://comicvine.com/api/publisher/4010-10/?api_key={YOUR_API_KEY}&format=json&field_list=characters,aliases,description"

- URL Breakdown:

  - Endpoint(s): Because this project works with DC Comics characters only, the required endpoint will be '_publisher_' not '_publisher_**_s_**'.[^bignote]
  - DC Comics' publisher ID is **4010-10**
  - To reduce response payload size, I personally selected 'characters', 'aliases', and 'description'.[^1]
  - I recommend using POSTMAN first to check that your GET request queries are functioning. See footnote 1.
  - In order to get a 200 response (this is not necessary if using POSTMAN, as POSTMAN will send the user-agent automatically), you will need to also include your 'User-Agent' as a headers parameter in requests.get(). So your code will look like the following:
    ````
    payload = { ... }
    headers = { 'User-Agent' : YOUR_HEADER }
    {response = requests.get(URL, headers=headers, params=payload)}```
    - To find your header, go to [whatsmybrowser](https://www.whatsmiybrowser.org) . `ctrl + f` 'user agent' if you can't find your User-Agent (it looks something like this:
    'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion')
    ````
  - I personally did not include `payload = { ... }` in my code (see `api.py`) because I was having issues with the commas in 'field_list'. Looking back now, if I just removed the spaces it should be ok--but it's not necessary unless you're drastically changing my code as all the necessary fields are returned.

  - It took me a while to figure out why my get requests in VScode kept returning with the response 403, I resorted to downloading the JSON file from POSTMAN. The format was weird though, so I created the function `format_conversion(filename, new_filename)` to re-format retrieved data for readability.
    - THEREFORE, I will need to return to the initial get characters from publisher request from comicvineAPI when I get to that in a later point (most likely after or during the 8 day request cycle period).
      **\*** I will return to this once I re-do the function
      (IGNORE) - Once you fulfill the parameters for `get_publisher_characters(API_KEY)` (IGNORE)

  [^bignote]: Should you want to look for other publishers, I recommend using the 'publishers' endpoint. The reason being you can't merely put in the publisher name in the URL, Comic Vine has assigned IDs to each publisher. So by using the 'publishers' endpoint, see example below, you will get a list of publishers with all of their respective fields. You can specifically select what field you want returned for a reduced size of the response payload.

  `{https://comicvine.com/api/publishers/?api_key={YOUR_API_KEY}&format=json}`

  [^1] My API requests would only return the first field in my field list, which proved very, very, very annoying. Because I was using POSTMAN to ensure I was receiving the information I was requesting, in the Query Params, for the key 'field_list' the value I put in included 'characters, aliases, description'. My requests kept returning only 'characters' (which was OKAY because it included the character id--the most important detail I needed from the publisher GET request), but again, very inconvenient. Solution: I realized I was including spaces in the field_list values, so the value needed to be changed to 'characters,aliases,description'.

STEP 2: Get Character Information by Character ID

- The function `get_comicvine_API` will open the JSON file created from getting all characters by publisher. It will glean all character IDs and append them to a list. The funciton will then loop through each character id to make individual API get requests for every respective characters' information.[^2]
- It will take about 8 days to retrieve all character information, as comic vine as a request limit of 100 per hour.

[^2] (\*note from 10/28/2022, I was currently planning on collecting all data from comic vine but as I was creating this README.md file I realized I don't need all that data until my project is complete so I will need to create another function to just get 99 characters to test my db with)

URL = "https://comicvine.com/api/character/4005-1699/?api_key=6028f8ab23892d424a31b9845b1c36ed4f737523&format=json&field_list=name,real_name,deck,powers,movies,issues_died_in

https://comicvine.com/api/character/4005-1699/?api_key=6028f8ab23892d424a31b9845b1c36ed4f737523&format=json&field_list=name,real_name,deck,powers,movies,issues_died_in
