function makeAllCaps(myArray) {
    let onlyStrings = []
    let allCaps = []
    return new Promise((resolve, reject) => {
        for (let item of myArray) {
            if (typeof(item) === "string") {
                onlyStrings.push(item);
            }
        } if (myArray.length === onlyStrings.length) {
            for (let item of onlyStrings) {
                let itemCaps = item.toUpperCase();
                allCaps.push(itemCaps);
                
            } 
        resolve(allCaps);
        } else {
            reject("Rejected. Not all items in the array were strings")
        }
    })
}

function sortWords(allCapsArray) {
    return new Promise((resolve, reject) => {
        if (allCapsArray.length > 4) {
            resolve(allCapsArray.sort())
        } else {
            reject("Rejected array length was equal to or less than four")
        }
    }) 
}

makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))
