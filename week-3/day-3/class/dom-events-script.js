let counter = 1

const insertRow = () => {
    const myTable = document.querySelector("#sampleTable");
    const myNewRow = document.createElement("tr");

    for (let i = 1; i < 6; i++) {
        const myNewCell = document.createElement("td");
        myNewCell.innerText = "Row" + counter + " cell" + i;
        myNewRow.append(myNewCell);

    }
    myTable.appendChild(myNewRow);
    counter++;
}

const myStrangeAlert = () => {
    alert("Rows on row on rows my g")
}

const listeners = () => {
    insertRow();
    myStrangeAlert();
}

document.querySelector("#button1").onclick = listeners;
