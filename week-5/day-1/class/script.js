console.log("Starting ...")

const displayArtwork = (art) => {
    const {title, artist_title : artist, artwork_type_title, place_of_origin} = art.data
    const paragraph = document.querySelector("#info-art");
    paragraph.textContent = `The painting is named 
    ${title} by the artist ${artist}. The type of artwork is ${artwork_type_title}. The country of origin is ${place_of_origin}`;
}

const displayError = (error) => {
    const paragraph = document.querySelector("#info-art");
    paragraph.textContent = `We have a problem ${error}`;
}

const getArtwork = () => {
    console.log("Working ...")
    fetch("https://api.artic.edu/api/v1/artworks/14572")
        .then((response) => {
            console.log(response);
            if(response.ok === true){
                return response.json()
            } else {
                throw new Error("Wrong artwork")
            }
        })
        .then((obj) => {
            displayArtwork(obj);
        })
        .catch((error)  => {
            displayError(error);
        });
    console.log("Work Done ...")
}



getArtwork()