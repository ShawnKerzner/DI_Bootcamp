import fs from "fs";



// export const reading = fs.readFile("./files/file-data.txt", "utf-8", (err, data) => {
//     console.log(data);
// })

export function reading(fileName) {
    fs.readFile(fileName, "utf-8", (err, data) => {
        console.log(data);
})};

