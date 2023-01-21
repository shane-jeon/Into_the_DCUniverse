document.querySelector("form").addEventListener("submit", search);

function search(event) {
  event.preventDefault();
  let searchTerm = document.getElementById("search-term").value;
  fetch("/search?name=" + searchTerm)
  .then(response => {
    if(response.status === 200) {
      return response.text();
    } else {
      alert("No Results Found")
    }
  })
  .then(data => {
    let results = document.getElementById("results");
    results.innerHTML = data;
  });
}