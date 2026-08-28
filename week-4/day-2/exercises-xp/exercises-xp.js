// Exercise 1
// const person = {
//     name: 'John Doe',
//     age: 25,
//     location: {
//         country: 'Canada',
//         city: 'Vancouver',
//         coordinates: [49.2827, -123.1207]
//     }
// }

// const { name, location: { country, city, coordinates: [lat, lng] } } = person;

// console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// // I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// //Exercise 2 

// // Using the code above, destructure the parameter inside the function and return a string as the example seen below:
// // //output : 'Your full name is Elie Schoppik'





// function displayStudentInfo(objUser) {
//     const { first, last } = objUser
//     console.log(`Your full name is ${first} ${last}`)
// }

// displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

// Exercise 3
const users = { user1: 18273, user2: 92833, user3: 90315 }
const usersArray = Object.entries(users)
for (let nestedArray of usersArray) {
    nestedArray[1] *= 2;
}
console.log(usersArray)