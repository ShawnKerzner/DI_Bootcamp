// Exercise 1
const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const { name, location: { country, city, coordinates: [lat, lng] } } = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// //Exercise 2

function displayStudentInfo(objUser) {
    const { first, last } = objUser
    console.log(`Your full name is ${first} ${last}`)
}

displayStudentInfo({ first: 'Elie', last: 'Schoppik' });

// Exercise 3
const users = { user1: 18273, user2: 92833, user3: 90315 }
const usersArray = Object.entries(users)
for (let nestedArray of usersArray) {
    nestedArray[1] *= 2;
}
console.log(usersArray)

// Exercise 4
class Person {
    constructor(name) {
        this.name = name;
    }
}

const member = new Person('John');
console.log(typeof member);
// so this code will return the data type object because typeof only looks at what type the variable member
// is and because member is an instance of the person class it is an object with access to all of person class atrributes and methods

// Exercise 5
class Dog {
    constructor(name) {
        this.name = name;
    }
};

// 1
class Labrador extends Dog {
    constructor(name, size) {
        this.size = size;
    }
};
// Cant be this one because it doesnt use the super keyword to call the super class constructor
// 2
class Labrador extends Dog {
    constructor(name, size) {
        super(name);
        this.size = size;
    }
    // It's this one because name is initialized in the constructr and has a defined value and also uses the super keyword to call the super class constructor
};
// 3
class Labrador extends Dog {
    constructor(size) {
        super(name);
        this.size = size;
    }
    // Can't be this one because name isnt initialized as a variable with a value here so its just undefined
};
// 4
class Labrador extends Dog {
    constructor(name, size) {
        this.name = name;
        this.size = size;
    }
};
// Can't be this one becuase it doesn't use the super keyword to call the super class constructor

//Exercise 6
//1.
//[2] === [2])
//{} === {}
// Both of these are false because === compares the reference point not the value

// 2.
const object1 = { number: 5 }; // value is 5 because the value of the key number is defined as 5
const object2 = object1; // value is 5 because its being set with the value of object1 where the value of key number is 5
const object3 = object2; // value is 5 because it following previous pattern and its set at the value of object 2 where the value of the key number is 5
const object4 = { number: 5 }; // value is 5 because the value of the key number is defined as 5
//const object1 = object4 // synatx error because the indentifier "object1" has as already declared

console.log(object1, object2, object3, object4)

class Animal {
    constructor(name, type, color) {
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mammal extends Animal {
    constructor(name, type, color, noise) {
        super(name, type, color);
        this.noise = noise;
    }
    sound() {
        console.log(`${this.noise} I'm a ${this.type} named ${this.name} and I'm ${this.color}`);
    }
}

let farmerCow = new Mammal("Bart", "cow", "black", "Sup Broskie");
farmerCow.sound();
console.log(farmerCow.name);
console.log(farmerCow.type);
console.log(farmerCow.color);
console.log(farmerCow.noise)

