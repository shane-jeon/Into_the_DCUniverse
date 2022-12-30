# Goal:

~~I will build a site that allows users to navigate character histories
within the DC Universe. They can see what media appearances characters have,
the different biographies from different eras and earths,
just collecting information that offers all the information a DC fan
would need right at their fingertips in one platform.~~

### 12/27/2022 update, MVP reassessment

A web application that provides "primers" for new and future DC Comics fans to smoothly usher themselves into the complex nature of the DC Universe. Intrigued by Wonder Woman's history after watching Wonder Woman 1984? Well looking up this female crusader's biography isn't as simple as it seems.

Delving into ONE character's history as someone with zero familiarity with the different eras (Golden Age, Silver Age, Bronze Age, Modern Age, New 52, Rebirth) and their publication periods (1938-1956, 1956-1971, 1971-1986, 1986-2011, 2011-2016, 2016-present)--respective dates. During these eras many characters had "reboots" to their origin stories and present timelines (fun fact, one of the few characters whose origin story has remained the same since its inception is Batman. The time old tale of a young boy found in an unfortunate situation in which he witnesses the murders of his mother and father by a petty criminal by the name of Joe Chill).

On top of the chronological changes to keep track of, there is the concept of the DC multiverse. The DC multiverse consists of multiple parallel universes in which some characters will have completely different story lines, relationships, may be deceased or non-existant, etc.

So the PURPOSE of this web application is to allow any user to look up a character of their choosing, get the character's basic biography and personal information, as well as first and all comic appearances, as well as their other appearances in other forms of media (graphic novels, television, film, animation, etc.) Now the curious user can choose where to start their journey with a basic foundational understanding.

This web application was inspired by my own forray into the DC Universe.
My _inspiration_:
As new fan drawn into the DC Universe by their appreciation of the DC Animated Universe, I was thrown into a tizzy when I looked up "Zatanna" and came across the magician's different origin stories and various time and plot lines. I didn't know where to start. Whatever path I chose to venture, I then realized that I needed to look more into the foul-mouthed, chain smoking anti-hero John Constantine. Wait now I need to learn more about Swamp Thing to truly understand John Constantine. Huh Swamp Thing has ties to "the Green", as do Poison Ivy and Floronic Man? My googling journey grew increasingly complex as the number of open tabs were but small slivers on the top of the browser.

~~The site will offer users to either enter a query
OR select from different categories~~

The web application will consist of an alphabetical list of characters, along with a search bar to query for a character. A click to a character link redirects you to a page dedicated to the DC character with the following information: photo, character name, real name, brief biography, gender, origin (if possible) first and all comic appearances, appearances in television/film in chronological order.

## data/APIs

I will need to collect data from different sources as DC does not have an API.

### 12/27/22 update, MVP reassessment:

Most reliable API I have been using so far:

#### CHARACTERS:

[ComicVine API](https://comicvine.gamespot.com/api/documentation)

SUPERHEROS:
~~To get all superhero characters, using the following site to gather a list of all DC
superheros
[superheroAPI](https://www.superheroapi.com/)~~

VILLIANS/ANTIHEROS
There is a github repo containing all DC villians and anti-heros
https://github.com/thatfiredev/dc-villains-api
** 10/25/2022, appears this API is not only just NOT working, but has obviously gathered the same info from SuperHero API
\*\*** attempting to find alternatives, but in the meantime, villians list is not complete

Media Apperances - I will use a variety of resources to collect all the data I will
need to be able to pair comics, movies, tv shows to the proper characters

COMICS: goodReads https://www.goodreads.com/api; Metron (comic book db) https://metron.cloud/ ; shortboxed https://api.shortboxed.com/ ; google books https://developers.google.com/books ; comic vine https://comicvine.gamespot.com/api/
MOVIES: IMDB https://developer.imdb.com/ ; Rotten Tomatoes https://developer.fandango.com/rotten_tomatoes
\*\* TMDB (the movie db), alternative to imdb
TV SHOWS: IMDB https://developer.imdb.com/ ; Rotten Tomatoes https://developer.fandango.com/rotten_tomatoes;

**\*\***10/25/2022 Major Interferences: IMDB is apparently owned by Amazon now! Fee is $150,000 for API access,
goodreads no longer offers public API access; Metron seems to be a viable option, however they have disabled the sign up button,
just e-mailed admin to see if I can sign up.
Earth/Eras:
Possibly Wikipedia? https://www.mediawiki.org/wiki/API:Main_page , https://en.wikipedia.org/api/rest_v1/#/ ;
possibly webscraping?

How to get data ideas:

- somehow get a list of movie titles (dc), iterate through list in one of the movie DBs to obtain
  the info

MVP 1.0

- populate databases
- use db data to create character profiles
- allow for queries that will also catch typos and list any with unfinished
  queries, e.g., "bat" --> batman, batgirl, batwoman, etc.; "green lantern" -->
  john stewart, hal jordan, kyle raynor, etc.
- simple, centered forms, displays, nothing fancy just yet

MVP 2.0

- Have show all option and be able to narrow down results through filters
- have drop down menu to take user to page with only filter they want to see (like characters only, or heros only)
- simple character profile, will have similar stats/details like dossier (see below)

MVP 3.0

- interactive UI/UX
- get real dossier kind of aesthetic
  https://tinadubinsky.com/character/
  also see img file for examples
  - also look into dossier examples from JLU animated universe/young justice/mayyybbe liveaction? (not likely)

MVP 4.0

- add basic DC history in an "about" like page

MVP 3000 (aka after web app is deployed)

- periodicallly check APIs to make sure db data is up to date

General Idea:

A sole character within the DC Comics Universe will have numerous origin stories and dynamic identities. This can be attributed to the "various eras and continuities in the DC Comics Universe", such as Pre and Post Crisis on Infinite Earths or the New 52, to name a few. (Rosenbalm, 2017) In addition to the complicated and often contradictary narratives, there are many different representations of characters outside of DC's super-hero comics. Such appearances include yet another branching of new character origins and backgrounds, specifically in live and animated film and television shows, as well as DC's recent line of YA graphic novels.

So, as one can imagine, finding a thorough character biography can be an arduous task. I know from personal experience, as in the past I have had to navigate through Wikipedia, Fandom Wiki, SubReddit threads, and various articles to get the complete picture of some of my favorite characters, such as Harley Quinn or John Constantine.

The purpose of my web application is to offer users (primarily DC fans like myself), a resource to find all the information they seek neatly packaged into one easily accessible page. Such pages will not only include lengthy details, thorough biographies, and pertinent associations--but also be creatively presented as top-secret dossiers, much like the ones Amanda Waller (the high ranking US Government official, best known as the founder of the infamous "Task Force X" (AKA the Suicide Squad), would have in her arsenal. I intend to create a web application purely dedicated to represent the rich history of the DC Universe.

What is the user flow?

- User will find a search bar at the homepage. Below the search bar will be a few images linking to random characters
- The user can search for a character or additionally can click an option that will show a list of ALL characters.
- After character selection, the user will be redirected to a character's dossier
- There will be a menu bar where the user can return home. Also arrows to return to the prior page
- If the user would like to bookmark a character page, they can select a star (or bookmark, will figure out exact details later on when working on the front end) that will save a character profile to "favorites/save for later"

Where does the user go first in the app? Where do they go second?

- They will first go to the home page with the search bar (at the bare minimium), the second destination will either be to a page displaying search bar results or to a list of all characters.

What does the user see? How do they interact with my app?

- A very simple user interface for now (see above)

Are there forms the user fills out? When?

- Yes, should a user want to create an account. That will be done when a user chooses to register or sign in.

Which data needs to be saved in a database?

- As much data needed to provide the complete profile of a DC character
- Basic user account information (which includes a page containing "starred" pages)

Which data is provided to the users?

- All data relevant to DC characters

What APIs will be used to access what data and how?

- Relying heavily on the Comic Vine API. Not the best API, nor does it have the best documentation. It's been a lengthy process trying to obtain and properly organize the dataset, but everything has been working out okay so far.

What features will I need to build around my dataset?

- A way to display the data set
- Query search

Main Features:

- DC Universe dataset stored in DB
- Web app that will allow users to see a list of characters and individual characters.
- Search for characters by name
- Bookmark character profiles to easily return to in the future

Nice-To-Haves:

- User login (though not necessary to use the web application)
- Interactive UI/UX within a characters' page, ideally designed as a "top-secret" dossier
- Filters to narrow down a search based on factors such as gender, powers, alignment, and species.
- Settings, such as option to open character dossiers in new tabs to continue searching through more characters.
- Spell check, suggesting the correct spelling of a character that the user may have meant to type and showing said character(s)

DATA and APIs
Two types of datasets:

1. Data collected from Comic Vine API (containing all information about DC characters)

- APIs:
  - Successful/Fruitful APIs:
    - SuperHero API (Albeit very limited, ended up only using it to get the hang of API calls)
    - Comic Vine API (A treasure trove of data, but it is limited to 100 requests per hour and has poor documentation)
  - Unsuccessful/Unattainable APIs:
    - GoodReads API (GoodReads no longer offers public API access)
    - Rotten Tomatoes API (Owned by Fandango, similar barrier to access as IMDB)
    - IMDB API (Apparently IMDB is owned by Amazon and charges $150,000 for API access.)
  - In the process of...
    - Metron Comic Book Database API
      - Was unable to sign up on the website. Had to contact moderator bpepple, he said to ping him on Matrix Space and he will create it manually.

2. Data collected from the user in creating an account

- This data will be (obviously) collected from user upon registering

MVP 1.0

- Create database and tables
- Write functions for API requests, collect dataset
  - Currently working on collecting all data before officially structuring my database.
- Basic CRUD operations
- Unit Test
- 3 HTML pages
  1. homepage, search bar
  2. list of all characters
  3. basic character profile (basic info + character profile picture)
- Basic user registration and sign in

MVP 2.0

- Filter options
- Include profile picture thumbnails below search bar for randomly selected characters. Characters should change every time page is refreshed
- Start incorporating REACT

MVP 3.0

- Include "search by" in search bar
- Randomized characters will display with carousel
- Dossier like character profile...though...this may extend to 4.0 +
- Allow user to save/bookmark/star/favorite character profiles, saved onto list
- Selenium testing

MVP 4.0

- Dossier profile continued
- Allow user to save character profiles into different "lists"
- Continue REACT
- Start creating clean CSS/Bootstrap layout (code)

MVP 5.0

- Possible deployment?

MVP ?.? (post-deployment)

- Periodically make API get requests to ensure DB data is up to date

Bibliography:

Rosenbalm, Butch. “FAQ – the Ages of DC Comics .” Www.writeups.org, Writeups.org, 19 June 2017, https://www.writeups.org/ages-dc-comics-primer-guide-crisis/.
