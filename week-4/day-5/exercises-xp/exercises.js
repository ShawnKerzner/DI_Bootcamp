// // Exercises 1
// function compareToTen(num) {
//     return new Promise ((resolve, reject) => {
//         if(num <= 10) {
//             resolve(`Success: ${num} is less than or equal to 10`);
//         } else {
//             reject(`Error: ${num} is greater than 10`);
//         }
//     });   
// }

// compareToTen(12)
//    .then(result => console.log(result))
//    .catch(error => console.log(error));

// compareToTen(8)
//     .then(result => console.log(result))
//    .catch(error => console.log(error));

// Exercises 2

function fourSecondTimer() {
    return new Promise((resolve, reject) => {
        setTimeout(() => { resolve("Success") }, 4000)
    })
}

fourSecondTimer().then(result => console.log(result));