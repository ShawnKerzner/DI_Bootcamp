// Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];
people.splice(0, 1);
people.splice(2, 3, 'Jason');
people.push("Shawn");
console.log(people.indexOf("Mary"));
const copyPeople = people.slice(1, -1);
console.log(people.indexOf("Foo")); // It returns negative 1 because the item 'Foo' is not an item in the list

for (const item of people) {
    console.log(item)
};

for (const item of people) {
    if (item == "Devon") {
        console.log(item);
        break;
    }
    else {
        console.log(item);
        break;
    }
};

