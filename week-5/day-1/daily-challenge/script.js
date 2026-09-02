async function fetchApi(userInput) {
    let apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
    let url = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${userInput}`;
    try {
        let response = await fetch(url);
        let data = await response.json();
        return data.data.images.original.url;
    } catch (error) {console.log(error);}
    
}

const form = document.querySelector("#form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const input = document.querySelector("#input");
    let inputValue = input.value;
    let result = await fetchApi(inputValue);
    let gifContainer = document.createElement("div");
    let actualGif = document.createElement("img");
    actualGif.src = result;
    let deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    gifContainer.append(actualGif, deleteButton);
    let body = document.querySelector("body");
    body.append(gifContainer);
});

