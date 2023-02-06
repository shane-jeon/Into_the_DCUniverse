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

function CharacterCard() {
  return(
    <div className="card">
      <img className="card--img" src="https://comicvine.gamespot.com/a/uploads/screen_medium/11116/111167641/8074849-cassandra-cain_artgerm-art.jpg" />
      <p className="card--name">Cassandra Cain</p>
      <p className="card--alias">Alias: "Orphan"</p>
    </div>
  )
}

function Homepage() {
  console.log("is this working")
  return (
    <div>
      <Navbar />
      <CharacterCard />
    
    </div>
  )
  
}

ReactDOM.createRoot(document.getElementById("root-homepage")).render(<Homepage />);