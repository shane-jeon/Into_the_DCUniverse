# Into the DCUniverse

"Dive into the DC Universe, a web application for fans of the DC Animated Universe who want to learn more about their favorite characters. The app currently features characters from _Young Justice_, but will soon expand to include _Justice League_, _Justice League Unlimited_, and _Harley Quinn_. The homepage will display a list of character cards (containing img, name, and aliases), each leading to a profile with basic information and a comprehensive list of comic book issues organized by publication era. The DC Universe can be overwhelming for new fans, and that's why this project was created- to offer a "primer" and simplify the research process. The creator of this project fell in love with the DC Animated Universe and eventually moved on to comics, but found the complexity of the multiverses and different publication eras intimidating. They wanted to create a one-stop-shop for new fans to ease their journey into the DC Universe, avoiding the time-consuming process of piecing information together from various sources."

# TABLE OF CONTENTS
* [Tech Stack](#tech-stack)
* [Challenges](#challenges)
* [Future Plans](#future)
* [Links](#links)

## <a name="tech-stack"></a> Project Description (Tech Stack, Challenges, Ideas for Future Feature Implementations)

For the backend of this application, I have utilized the Python programming language, in conjunction with SQLAlchemy and PostgreSQL, for database management. The frontend is composed of HTML, CSS, JavaScript, and React for dynamic rendering. I chose to use this tech stack as it allowed me to build upon the skills and knowledge I acquired during my time at Hackbright Academy, where I created my first project. Specifically, I aim to expand my proficiency in JavaScript and React, which I did not have the opportunity to fully explore in my previous project. To gather information on the characters featured in the app, I utilized the Comic Vine API as a valuable resource, and for obtaining a list of characters introduced in the Young Justice television series, I employed web scraping techniques using Beautiful Soup library on the Young Justice Fandom Wiki page. By cross-referencing this list of character names with a dictionary of all characters within the DC Universe, I was able to selectively gather information on the desired characters.
It's important to note that, as the Comic Vine API is a community-built and supported resource, there are certain limitations to the number of requests that can be made in a given time frame. To adhere to these restrictions, I have created a function that enforces a delay of 1 hour after 100 requests, ensuring compliance with the API's rules while still efficiently retrieving the necessary data. 


## <a name="challenges"></a> Challenges

I aimed to expand my proficiency in JavaScript and React, which I did not have the
opportunity to fully explore in my coding bootcamp capstone project. This time around, I
did not have the support of my instructors or peers to troubleshoot blockers or
bugs in my code. This required in the conduction of extensive
research and self-study to piece together solutions and hone my skillsets. Has greatly improved debugging skills in both frontend and backend.

One of the challenges I faced was my limited experience with REST APIs. Especially as DC Comics does not have an API (for the time being), I had to find resources through my own means. The reliable and wonderful resources I did find included Comicvine's API, whiched helped me in improving my interpretation of API documentation. Though challenging at first, learning from my mistakes eventually allowed me to familiarze myself with API GET requests (especially when it came to understanding the constraints of REST architecture), response handling, and creating functions to incorporate data from JSON files/web scraping to my database.

Due to time limitations (with my capstone project), I wasn't able to include as many interactive features as I would have liked. In this project, my primary focus is towards establishing a better understanding of frontend development. My goal is to create a product with better styling and dynamic features. Currently working on increasing familiarity with JavaScript as well as React. 

To fully comprehend my code, I revisited my notes and lectures on JavaScript and DOM manipulation from Hackbright Academy. For concepts I couldn't understand, I turned to books and documentation. For example, I felt I needed to break React down to its fundamental building blocks, thus I went back to square one and started studying React using React's beginner-friendly documentation and online scrimba course. This experience is greatly helping me in understanding components, props, state, hooks, rendering, and the integration of React into my web application's frontend. Because I am able to pace myself this time around me, I can actually incorporate all lessons from HB in developing MVP.

I am very much enjoying front-end development and am developing best study practices to increase quality of learning.

## <a name="future"></a> Future Features

_Into the DC Universe_ is a project very near and dear to my heart, with the goal to introduce new generations of DC fans trickling in from viewerships of the DC animated universe to the fuller extent of the DC universe.

I hope to add new features along my journey as a software engineer, implementing the knowledge and experience I will have gained through my professional career. Some features that I look forward to adding include character appearances in other forms of media (film, television, graphic novels), user accounts (so users may bookmark characters or comics they would want to return to later), and an extremely interactive and complicated map that I can't even find the words for to explain. I hope to deploy it once the day comes. This project will always be a work in progress and hopefully I can feel confident sharing my project with the users of the DC subreddit (their very critical nature is definitely a component in my motivation).

### <a name="links"></a> Links
- [Figma File](https://www.figma.com/file/oxz3PnOxaJLdreVew8hwNX/Untitled?node-id=0%3A1&t=g1zQbWfZfS9IwPJl-1)
<!-- **under construction, explanation of how to work with comicvine REST API. For future users and/or my future self**

### Working with comicvine API:

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

https://comicvine.com/api/character/4005-1699/?api_key=6028f8ab23892d424a31b9845b1c36ed4f737523&format=json&field_list=name,real_name,deck,powers,movies,issues_died_in -->
