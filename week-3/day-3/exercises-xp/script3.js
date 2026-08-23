// Exercise 3
const allBoldItems = document.querySelectorAll("strong")

const highlight = (event) => {
    event.target.setAttribute("style", "color: blue;")
};

const normal = (event) => {
    event.target.setAttribute("style", "color: black;")
};
for (let node of allBoldItems) {
    node.addEventListener("mouseover", highlight)
    node.addEventListener("mouseout", normal)
};
