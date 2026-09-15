import { people } from "./data.js";

function averageAge(peopleArray) {
    let ageTotal = 0
    for (let person of people) {
        ageTotal += person["age"];
    }
    console.log(Math.floor(ageTotal / people.length))
}

averageAge(people);