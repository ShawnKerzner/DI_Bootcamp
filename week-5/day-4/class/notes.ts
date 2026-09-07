// function myFunction(a: boolean): string | number {
//     if (a) {
//         return "Hello"
//     } else {
//         return 1
//     }
// }
// console.log(myFunction(true));
// console.log(myFunction(false));
//  type MyType = (string | number);
//  type myObjectType = {
//     name: string,
//     age: number,
//     isStudent?: boolean
//  };

//  let a: MyType = 5;
//  let b: myObjectType = {name: "Joe", age: 14};

class MyClass {

    private greeting: string;
    public goodbye: string;

    constructor(greeting: string) {
        this.greeting = greeting;
        this.goodbye = "Bye";
    }
    myMethod() {
        console.log(this.greeting);
    }
}

const myClassInstance = new MyClass("Hello");
myClassInstance.myMethod()
console.log(myClassInstance.goodbye)

class Employee {
    readonly name: string;
    readonly lastname: string;
    private salary: number;
    public position: string;

    constructor(name: string, lastname: string, salary: number, position: string) {
        this.name = name;
        this.lastname = lastname;
        this.salary = salary;
        this.position = position;
    }
    public greeting(): void {
        console.log(`I'm ${this.name} ${this.lastname}, my role is ${this.position}`)
    }

    public CompareMySalary
    (theOtherSalary: number): string {
        return this.salary > theOtherSalary ? "I'm happy" : "Give me a raise now!"
    }

}

const myEmployeeInstance = new Employee("John", "Doe", 1000, "developer");
myEmployeeInstance.greeting();
console.log()