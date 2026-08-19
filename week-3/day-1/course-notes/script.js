let addressNumber = 55;
let addressStreet = "av Bosquet";
let country = "Paris"

let globalAddress = "I live in" + " " + addressNumber + " " + addressStreet + " " + country;

console.log(globalAddress);
document.getElementById("addressDisplay").textContent = globalAddress