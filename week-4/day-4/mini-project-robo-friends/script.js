// Array of robot friends and all of their info stored in objects
const robots = [
    {
        id: 1,
        name: 'Leanne Graham',
        username: 'Bret',
        email: 'Sincere@april.biz',
        image: 'https://robohash.org/1?200x200'
    },
    {
        id: 2,
        name: 'Ervin Howell',
        username: 'Antonette',
        email: 'Shanna@melissa.tv',
        image: 'https://robohash.org/2?200x200'
    },
    {
        id: 3,
        name: 'Clementine Bauch',
        username: 'Samantha',
        email: 'Nathan@yesenia.net',
        image: 'https://robohash.org/3?200x200'
    },
    {
        id: 4,
        name: 'Patricia Lebsack',
        username: 'Karianne',
        email: 'Julianne.OConner@kory.org',
        image: 'https://robohash.org/4?200x200'
    },
    {
        id: 5,
        name: 'Chelsey Dietrich',
        username: 'Kamren',
        email: 'Lucio_Hettinger@annie.ca',
        image: 'https://robohash.org/5?200x200'
    },
    {
        id: 6,
        name: 'Mrs. Dennis Schulist',
        username: 'Leopoldo_Corkery',
        email: 'Karley_Dach@jasper.info',
        image: 'https://robohash.org/6?200x200'
    },
    {
        id: 7,
        name: 'Kurtis Weissnat',
        username: 'Elwyn.Skiles',
        email: 'Telly.Hoeger@billy.biz',
        image: 'https://robohash.org/7?200x200'
    },
    {
        id: 8,
        name: 'Nicholas Runolfsdottir V',
        username: 'Maxime_Nienow',
        email: 'Sherwood@rosamond.me',
        image: 'https://robohash.org/8?200x200'
    },
    {
        id: 9,
        name: 'Glenna Reichert',
        username: 'Delphine',
        email: 'Chaim_McDermott@dana.io',
        image: 'https://robohash.org/9?200x200'
    },
    {
        id: 10,
        name: 'Clementina DuBuque',
        username: 'Moriah.Stanton',
        email: 'Rey.Padberg@karina.biz',
        image: 'https://robohash.org/10?200x200'
    }
];

// Global variable for the robot-container div in the index.html skeleton to be used in functions
let robotContainerDiv = document.querySelector("#robot-container");

function renderCards(robotArray) {
    for (let robot of robotArray) {
        let robotCardDiv = document.createElement("div");
        robotCardDiv.id = robot["id"];
        let robotImage = document.createElement("img");
        robotImage.src = robot["image"];
        robotImage.classList.add("robot-image")
        robotCardDiv.append(robotImage);
        let robotName = document.createElement("h3");
        robotName.innerText = robot["name"];
        robotCardDiv.append(robotName);
        let robotEmail = document.createElement("p");
        robotEmail.innerText = robot["email"];
        robotCardDiv.append(robotEmail);
        robotContainerDiv.append(robotCardDiv);
    }
}

function searchByName(searhBarInput) {
    let allLowersearhBarInput = searhBarInput.toLowerCase()
    for (let robot of robots) {
        let robotCardDiv = document.querySelector(`#${robot["id"]}`)
        if (robot["name"].includes(allLowersearhBarInput) == false) {
            robotCardDiv.style.display = "none"
        } else {
            robotCardDiv.style.display = "";
        }
    }
}

const searchBar = document.querySelector("#search-bar")
searchBar.addEventListener("input", searchByName)


renderCards(robots);
