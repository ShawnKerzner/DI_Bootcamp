const character_name = document.querySelector("#name");
const height = document.querySelector("#height");
const gender = document.querySelector("#gender");
const birthYear = document.querySelector("#birth-year");
const homeWorld = document.querySelector("#home-world");
const loading = document.querySelector("#loading");
const errorDiv = document.querySelector("#error");
const findBtn = document.querySelector("#find-btn");
let previousNum = 0;

async function findSomeone() {
    let randomNum = Math.floor(Math.random() * 83) +1;
    while (randomNum === previousNum) {
        randomNum = Math.floor(Math.random() * 83) +1;
    }
    try {
    loading.hidden = false;
    errorDiv.hidden = true;
    character_name.textContent="";
    height.textContent="";
    gender.textContent="";
    birthYear.textContent="";
    homeWorld.textContent="";

        const data = await getUrl(`https://www.swapi.tech/api/people/${randomNum}`);
        const homeData = await getUrl(data.result.properties.homeworld);
        displayCharacter(data, homeData);
    
    } catch (error) {
        errorDiv.hidden = false;
        console.log(error);
    } finally {
        previousNum = randomNum;
        loading.hidden = true;

    }
}

function displayCharacter(characterData, planetData) {
    character_name.textContent = characterData.result.properties.name;
    height.textContent = `Height: ${characterData.result.properties.height}cm`;
    gender.textContent = `Gender: ${characterData.result.properties.gender}`; 
    birthYear.textContent = `Year of Birth: ${characterData.result.properties.birth_year}`;
    homeWorld.textContent = `Home World:  ${planetData.result.properties.name}`;
}

async function getUrl(url) {
    const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Request Failed');
        }
        const data = await response.json();
        return data;
}

findBtn.addEventListener('click', findSomeone);

