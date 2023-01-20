// Empty search bar, takes in user input
// capture user input, handle it to start finding what user is searching for
// find and render data to user, store data being searched (characters)

// get search bar element
const searchInput = document.getElementById("searchInput")

// store character elements in array-like object
const charactersFromDOM = document.getElementsByClassName("character-name")

// event listener
searchInput.addEventListener("keypress", (event) => {
  if (event.key === 'Enter'){

    const { value } = event.target;
    
    // get user search input converted to lowercase
    const searchQuery = value.toLowerCase();
    
    for (const characterElement of charactersFromDOM) {
      // store name text and convert to lowercase
      let character = characterElement.textContent.toLowerCase();
      
      // compare current character to search input
      if (character.includes(searchQuery)) {
        // found name matching search, display
        characterElement.style.display = "block";
      } else {
        // no match
        characterElement.style.display = 'none';
      }
    }
  }
  });

