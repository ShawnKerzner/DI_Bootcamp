// // Exercise 1 
// async function fetchGiphInfo() {
//     try {
//         const response = await fetch("https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My");
//         if (response.ok) {
//            const data = await response.json();
//             console.log(data)
//         } else {
//             throw new Error(response.status)
            
//         }
//     } catch(e){
//        console.log(e)
//     }
// }

// fetchGiphInfo()

// // Exercise 2 
// async function fetchTenSunGiphs() {
//     try {
//         const response = await fetch("https://api.giphy.com/v1/gifs/search?q=sun&rating=g&limit=10&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My");
//         if (response.ok) {
//             const data = await response.json();
//             console.log(data);
//         } else {
//             throw new Error(response.status);
//         }
//     } catch(e) {
//         console.log(e)
//     }
// }

// fetchTenSunGiphs()

// // Exercise 3
// async function newImproved() {
//     try {
//         const response = await fetch("https://www.swapi.tech/api/starships/9/");
//         if (response.ok) {
//             const data = await response.json();
//             console.log(data);
//         } else {
//             throw new Error(response.status);
//         }
//     } catch (e) {
//         console.log(e);
//     }
// };

// Exercise 4 
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();
// First it will console.log "calling"
// Then 2 seconds will go by
// Then it will console.log "Resolved"