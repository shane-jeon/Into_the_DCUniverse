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
    <div className="card--char">
      <img src="" />
      <h3>*insert char_name*</h3>
    </div>
  )
}

function Homepage() {
  console.log("is this working")
  return (
    // <h1>homepage</h1>
    <div>
    {/* <h1>Homepage goes here</h1> */}
    <Navbar />
    {/* <Characters /> */}
    </div>
  )
  
}

ReactDOM.createRoot(document.getElementById("root-homepage")).render(<Homepage />);