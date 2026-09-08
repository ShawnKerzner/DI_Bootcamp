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

function handleData(dataArray: (User | Product | Order)[]): string[] | string {
    let result: string[] = []
    for(let obj of dataArray) {
        if(obj["type"] === "user") {
            result.push(`${obj["name"]} is ${obj["age"]} years old`)
        } else if (obj["type"] === "product") {
            result.push(`Product ID:${obj["id"]} costs ${obj["price"]}`)
        } else if (obj["type"] === "order") {
            result.push(`Order ID:${obj["orderId"]} has ${obj["amount"]} orders.`)
        }
    }
    if(result.length < 1) {
        return "Error: No relevant data found"
    } else{
        return result
    }
}

console.log(handleData(mixedData));