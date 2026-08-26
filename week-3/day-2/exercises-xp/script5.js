const div = document.querySelector("#container");
console.log(div);

const liNodeList = document.querySelectorAll("li");
for (node of liNodeList) {
    if (node.innerText == "Pete") {
        node.innerText = "Richard"
    }
}

const ulNodeList = document.querySelectorAll("ul");
const ulTwo = ulNodeList[1];
const liTagsinUlTwo = ulTwo.children;
const secondLiinUlTwo = liTagsinUlTwo[1];
secondLiinUlTwo.remove();

for (node of ulNodeList) {
    node.children[0].innerText = "Shawn";
}

for (node of ulNodeList) {
    node.classList.add("student_list")
}
const ulOne = ulNodeList[0];
ulOne.classList.add("university");
ulOne.classList.add("attendance");

div.style.backgroundColor = "lightblue"
for (node of liNodeList) {
    if (node.innerText == "Dan") {
        node.remove()
    }
}

for (node of liNodeList) {
    if (node.innerText == "Richard") {
        node.style.border = "solid black 2px"
    }
}

const body = document.querySelector("body");
body.style.fontSize = "32px";