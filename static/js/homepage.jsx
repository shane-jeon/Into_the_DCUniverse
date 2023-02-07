'use strict';

// import { process_params } from "express/lib/router";

// import Navbar from "components/Navbar";

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




function CharacterCard(props) {
  return(
    <div className="card">
      <img className="card--img" src={props.image} />
      <p className="card--name">{props.name} </p>
      <p className="card--alias">{props.alias} </p>
    </div>
  )
}


function Homepage() {
  const [characters, setCharacters] = React.useState([]);
  React.useEffect(()=> {
    fetch('/characters.json')
    .then(response => {
      console.log(response);
      return response.json();})
    .then(data => {
      console.log(data);
      setCharacters(data.characters);
      })
      .catch(error => {
        console.error(error);
      });
    }, []);

  const characterCards = characters.map(item => {
    return(
    <CharacterCard
      key={item.id}
      image={item.image}
      name={item.name}
      alias={item.alias}
    />
    );
 });
  
 return (
    <div>
      <Navbar />
      <div className="card--grid">
      {characterCards}
      </div>
    </div>
  )
}

ReactDOM.createRoot(document.getElementById("root-homepage")).render(<Homepage />);