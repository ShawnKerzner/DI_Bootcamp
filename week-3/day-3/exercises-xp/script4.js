// Exercise 4
// V = (4 / 3) × π × r³, 

const radius = document.querySelector("#radius");
const volume = document.querySelector("#volume")
const form = document.querySelector("form")


let findVolume = (radius) => {
    return (4 / 3) * 3.14 * radius ** 3
};

function formSubmit(event) {
    event.preventDefault();
    const radiusValue = radius.value;
    if (radiusValue === "") {
        alert("Insert a radius");
        return
    }
    let volumeFound = findVolume(radiusValue)
    volume.value = volumeFound
}

form.addEventListener("submit", formSubmit)