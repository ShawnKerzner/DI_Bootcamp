// API - Application Programming Interface

// fetch(("FROM WHERE"))

const myFetch = await fetch("https://api.artic.edu/api/v1/artworks/14572") // returns a promise
const myData = await myFetch.json();
console.log(myData)
// myFetch.then((response) => response.json().then((response) => console.log(response)))

// console.log(myFetch)

