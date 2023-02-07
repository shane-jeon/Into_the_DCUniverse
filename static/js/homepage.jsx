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
  // let characterData = []


  // fetch('/characters.json')
  // .then((response) => response.json())
  // .then((data) => (characterData.push(data)));

  // const innerArray = characterData[0]
  // console.log(characterData)
  // console.log(typeof characterData)
  // console.log(characterData[0])
  // const charData = characterData
  // console.log(charData);


    
  return(
    <div className="card">
      <img className="card--img" src={props.image} />
      <p className="card--name">{props.name} </p>
      <p className="card--alias">{props.alias} </p>
      {/* <img className="card--img" src="https://comicvine.gamespot.com/a/uploads/screen_medium/11116/111167641/8074849-cassandra-cain_artgerm-art.jpg" />
      <p className="card--name">Cassandra Cain</p>
      <p className="card--alias">Alias: "Orphan"</p> */}
    </div>
  )
}



// function CharacterCard() {
//   return(
//     <div className="card">
//       <img className="card--img" src="https://comicvine.gamespot.com/a/uploads/screen_medium/11116/111167641/8074849-cassandra-cain_artgerm-art.jpg" />
//       <p className="card--name">Cassandra Cain</p>
//       <p className="card--alias">Alias: "Orphan"</p>
//     </div>
//   )
// }

function Homepage() {
  let characterData;


  fetch('/characters.json')
  .then((response) => response.json())
  .then((data) => {
    characterData = data;
    console.log(characterData);
  });

  const [characters, setCharacters] = React.useState([]);
  React.useEffect(()=> {
    try {fetch('/characters.json')
    .then((response) => response.json())
    .then((data) => {
      setCharacters(data)
      });
    } catch (error) {
      console.error(error);
    }
  }, []);

  if (!characters || !Array.isArray(characters)) {
    return <div>Loading...</div>;
  }

  const characterCards = characters.map(item => {
    return(
    <CharacterCard
      image={item.image}
      name={item.name}
      alias={item.alias}
    />
    );
 });
  
 return (
    <div>
      <Navbar />
      {characterCards}
    </div>
  )
}

ReactDOM.createRoot(document.getElementById("root-homepage")).render(<Homepage />);