const myObject = {
    name: 'John',
    lastname: 'Doe'
}

console.log(Object.keys(myObject))
console.log(Object.values(myObject))
console.log(Object.entries(myObject))

const MyArray = [
    ['student', 'Joe'],
    ['teacher', 'Rose']
]

console.log(Object.fromEntries(MyArray))

let myObj = {
    name: "john",
    lastNmae: "Doe",
    age: 25,
    friends: ["Mark", "Lucifer", "Ana"]
}

const myObjKeys = Object.keys(myObj);
const myObjValues = Object.values(myObj);

console.log(`We have ${myObjKeys.length} keys and ${myObjValues.length} values`)
console.log(myObjKeys.map((e, i) => 'The ' + (i + 1) + ' key is: ' + e))
