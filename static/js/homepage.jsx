'use strict';

function Navbar() {
  return(
    <nav>
      <img src="./static/img/logo.png" className="navbar--logo"/>
      <div className="navbar--anchor">
      <span><a className="navbar--hyperlink" href="/about.html">About  </a></span>
      <span><a className="navbar--hyperlink" target="_blank" href="https://github.com/shane-jeon/Into_the_DCUniverse">GitHub  </a></span>
      <span><a className="navbar--hyperlink" href="#">Feedback  </a></span>
      </div>
    </nav>
  )
}

// to-do: created basic searchbar in homepage, working on actual functionality
function SearchBar() {
  // JS logic 
  return(
    <div>
      <form className="search--form">
        <input 
          type="text"
          placeholder="search the 'verse"
          className="search--form_input"
        />

        <button
          className="search--form_button"
          ><img src="static/img/magnifying_glass.png" className="search--magnify" /></button>
      </form>
    </div>
  )
}

// display all character cards on homepage
function CharacterCard(props) {
  return(
    <div className="card">
      <img className="card--img" src={props.image}/>
      <p className="card--name">Name: {props.name} </p>
      <p className="card--alias">Alias: {props.alias} </p>
    </div>
  )
}


function Homepage() {
  // get data from server.py endpoint 'characters/json' to display img, name, and alias in characterCard
  const [characters, setCharacters] = React.useState([]);
  // "edgecases", a couple of cardCharacters are still displaying all aliases. Not overflowing but look into why
  const [aliasLimit, setAliasLimit] = React.useState(7);
  React.useEffect(()=> {
    fetch('/characters.json')
    .then(response => {
      // console.log(response);
      return response.json();})
    .then(data => {
      // console.log(data);
      setCharacters(data.characters);
      })
      .catch(error => {
        console.error(error);
      });
    }, []);

  const characterCards = characters.map((item, index) => {
    // prevent overflowing letter characters in character card
    let limitedAlias = (index < aliasLimit) ? item.alias: item.alias.slice(0, aliasLimit) +'...';
    if (limitedAlias === "none available") limitedAlias = "N/A";
    return(
    <CharacterCard
      key={item.char_id}
      image={item.image}
      name={item.name}
      alias={limitedAlias}
    />
    );
 });
  
 return (
    <div>
      <Navbar />
      <SearchBar />
      <div className="card--grid">
      {characterCards}
      </div>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById("root-homepage")).render(<Homepage />);