// function calculateSumTS(a: number, b: number): number {
//     return a + b;
// }
// console.log(calculateSumTS(100, 2));
// console.log(calculateSumTS("100", 3))
// console.log(calculateSumTS(100, 4));
// console.log(calculateSumTS(undefined, 1));

// const a: string = "Hello World";
// const b: = a + 1;
// console.log(b);

// const val1: string = "Hello";
// const val2: number = 11.2;
// const val3: boolean = true;

// const example1 = "Hello World";
// example = 56

// function subtraction(a: number, b: number): number {
//     return a - b;
// }

// console.log(subtraction("hello", 56));

// 

// let a = 0;
// let b = 10;
// if (a > 5 || !(b < 20)) {
//     console.log("success")
// } else {
//     console.log("Oh no")
// }

// let  myObject: {
//     name: string,
//     age: number,
//     isStudent: boolean;
// } = {
//     name: "john",
//     age: 25,
//     isStudent: true
// }

// myObject.weight = 60;

// let myObject: {};
// myObject.weight = 60;

// let myArray: (string | number)[] = [];
// myArray.push(3);
// myArray.push("Hello");
// console.log(typeof myArray[0]);

// let myTuple: [string, number] = ["John", 10];

// let point: [number, number, number];
// point = [3,4, 12];
// function distanceFromOrigin([x,y,z]: [number, number, number]): number {
//     return Math.sqrt(x**2 + y**2 + z**2);
// }

// console.log(distanceFromOrigin(point));

// function myFunction(): never {
//     throw new Error("oh no");
// }

// let a: (number | string) [] =  [1, "abc", 3];
// // yes, no maybe
// type myPerfectType = "yes" | "no" | "maybe" | "no chance";
// let b: myPerfectType;
// let c: myPerfectType;
// let d: myPerfectType;
// type myOtherType = number | number | string | true;

// function addNums(a: number, b: number): number {
//     return a + b;
// }

// console.log(addNums(1,2));
// console.log(addNums("2", 1));

class Counter {
    private current: number = 0;
    
    count(): number; //1st option. Input: nothing, output: a number
    count(target: number): number []; // 2nd option. Input a number, Output: an array of numbers
    count(target?: number): number | number [] { // input: nothing or a number. output: a number or an array of numbers
        if (typeof target !== "undefined") {
            let values: number [] = [];
            for (let i = this.current; i <= target; i++) {
                values.push(i)
            }
            this.current = target;
            return values;
        }
        return ++this.current;
    }
}

const myCounter = new Counter();
console.log(myCounter.count(5))