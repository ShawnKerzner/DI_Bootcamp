const h1 = document.querySelector("h1");
console.log(h1);

const paragraphs = document.querySelectorAll("p");
const lastParagraph = paragraphs[paragraphs.length - 1];
lastParagraph.remove();
console.log("last paragraph removed");


const h2 = document.querySelectorAll("h2");
const h2Color = (event) => {
    event.target.setAttribute("style", "background-color: red;")
}
    ;

for (let node of h2) {
    node.addEventListener("click", h2Color)
};

const h3 = document.querySelectorAll("h3");
const h3Disappear = (event) => {
    event.target.setAttribute("style", "display: none")
};

for (let node of h3) {
    node.addEventListener("click", h3Disappear)
};

const button = document.createElement("button");
button.textContent = "Click me";
document.body.appendChild(button);
function textBold() {
    let p = document.querySelectorAll("p");
    for (let item of p) {
        item.setAttribute("style", "font-weight: bold;")
    }
}

button.addEventListener("click", textBold)
