const planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"];
const colors = ["red", "orange", "green", "blue", "yellow", "purple", "pink", "white"];
let styleRules = []
let planetSection = document.querySelector(".listPlanets");

for (let i = 0; i < planets.length; i++) {
    let newPlanet = document.createElement("div");
    newPlanet.classList.add("planet");
    newPlanet.classList.add(planets[i]);
    let styleRule = `.${planets[i]}{background-color: ${colors[i]};}`;
    styleRules.push(styleRule);
    planetSection.append(newPlanet)
};

let styleTag = document.createElement("style");
styleTag.textContent = styleRules.join("\n");
document.head.append(styleTag);
