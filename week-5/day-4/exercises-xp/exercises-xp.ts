class Employee {
    private name: string;
    private salary: number;
    public position: string;
    protected department: string;

    constructor (name: string, salary: number, position: string, department: string) {
        this.name = name;
        this.salary = salary;
        this.position = position;
        this.department = department;
    }

    public getEmployeeInfo(): string{
        return `Employee name: ${this.name}\nEmployee position: ${this.position}`
    }
}

const employee1 = new Employee ("Shawn", 750000, "Full Stack Engineer", "R&D");
console.log(employee1.getEmployeeInfo());

// Exercise 2

class Product {
    readonly id: number;
    public name: string;
    public price: number;

    constructor (id: number, name: string, price: number) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    getProductInfo(): string {
        return `Product Name: ${this.name}\nPrice: ${this.price}`
    }
}

const product1 = new Product (12345, "Computer", 1500);
console.log(product1.getProductInfo())
// product1.id = 98765; // raises an error because you are not allowed to modify a readonly property.

// Exercise 3

class Animal {
    public name: string;

    constructor(name: string) {
        this.name = name;
    }

    makeSound() {
        return `${this.name} says I love TypeScript.`
    }
}

class Dog extends Animal {
    makeSound(): string {
        return `${this.name} barks!`
    }
}

const dog1 = new Dog("Steve");
console.log(dog1.makeSound());

// Exercise 4

interface MathOperation {
    (a: number, b: number): number;
}

class Calculator {
    static add: MathOperation = (a, b) => a + b;
    static subtract: MathOperation = (a, b) => a - b;
}

console.log(Calculator.add(1, 9));
console.log(Calculator.subtract(10, 1));

// Exercise 5
// Create an interface User with properties id (readonly), name, and email. 
// Extend the User interface to create a PremiumUser interface with an additional optional property membershipLevel.
//  Create a function printUserDetails that accepts a PremiumUser and logs the details to the console.

interface User {
    readonly id: number;
    name: string;
    email: string;
}
 
interface PremiumUser extends User {
    membershipLevel: string
}

const userPrime: PremiumUser = {
    membershipLevel: "VIP",
    name: "Shawn",
    email: "shawn@123.com",
    id: 1,
}

function printUserDetails(user: PremiumUser): void {
    console.log(user);
}

printUserDetails(userPrime);