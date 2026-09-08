// function identity<T>(i: T): T {
//     return i
// }

// console.log(identity("aloha"))

// function makePair<A, B>(first: A, second: B): [A, B] {
//     return [first, second]
// }

// console.log(makePair("hi", true))

// function extendo<T extends {name: string, age: number}>(obj: T): T {
//     console.log(obj);
//     return obj
// }

// extendo({name:"Shawn", age: 28})

// interface Generic<T> {
//     title: string;
//     content: T
// }

// const var1: Generic<string> = {
//     title: "title",
//     content: "A string for content"
// }

// const var2: Generic<{}> = {
//     title: "Another Title",
//     content: {}
// }

// class Holder<T>{
//     private myValue: T;

//     constructor(initialValue: T) {
//         this.myValue = initialValue;
//     }

//     getMyValue(): T {
//         return this.myValue;
//     }
// }

// const myMessage = new Holder<number[]>([1, 2, 3]);
// console.log(myMessage.getMyValue());

// class MyClass<T, F> {
//     private item1: T;
//     private item2: F;

//     constructor(item1: T, item2: F) {
//         this.item1 = item1
//         this.item2 = item2
//     }

//     getMyTypes(): string {
//         return `${typeof this.item1} ${typeof this.item2}`
//     }

// }

// const myMessage = new MyClass<number, string>(5, "Hello");
// console.log(myMessage.getMyTypes()

type User = {
    name: string;
    age: number;
    type: "user";
}

type Product = {
    id: number;
    price: number;
    type: "product"
}

type Order = {
    orderId: string;
    amount: number;
    type: "order";
}

const mixedData: (User | Product | Order) [] = [
    {
        type: "user",
        name: "Joe",
        age: 25
    },
    {
        id: 12345,
        price: 100,
        type: "product"
    },
    {
        orderId: "order12345",
        amount: 2000,
        type: "order"
    }
]

function handleData(dataArray: (User | Product | Order)[]): string {
    for(let obj of dataArray) {
        if(obj["type"] === "user") {
            return `${obj["name"]} is ${obj["age"]} years old`
        } else if (obj["type"] === "product") {
            return `A ${obj["id"]} costs ${obj["price"]}`
        } else if (obj["type"] === "order") {
            return `An order ${obj["orderId"]} has ${obj["amount"]} orders.`
        }
    }
    return ""
}

console.log(handleData(mixedData));