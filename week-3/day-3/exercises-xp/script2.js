// Exercise 2
const form = document.querySelector("form");
console.log(form);

const fname = document.querySelector("#fname");
const lname = document.querySelector("#lname");
console.log(fname, lname);

const inputByNameFname = document.getElementsByName("firstname");
const inputByNameLname = document.getElementsByName("lastname");
console.log(inputByNameFname);
console.log(inputByNameLname);

function formSubmission(event) {
    event.preventDefault();
    const lnameValue = lname.value;
    const fnameValue = fname.value;
    if (fnameValue === "" || lnameValue === "") {
        alert("Both inputs need to be filled in");
        return
    }
    let liFname = document.createElement("li")
    let liLname = document.createElement("li")
    liFname.innerText = fnameValue
    liLname.innerText = lnameValue
    const userAnswer = document.querySelector(".usersAnswer")
    userAnswer.append(liFname, liLname)
}

form.addEventListener("submit", formSubmission);