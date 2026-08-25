const coloringBoard = document.querySelector("#coloring-board");
const swatches = document.querySelectorAll(".color-swatch");
const colorPallete = document.querySelector("#color-pallete");
let selectedColor = "whitesmoke";
let mouseDown = false

function generateBoard() {
    let coloringBoardWidth = coloringBoard.offsetWidth;
    let coloringBoardHeight = coloringBoard.offsetHeight;
    const cellSize = 30;
    const numColumns = Math.floor(coloringBoardWidth / cellSize);
    const numRows = Math.floor(coloringBoardHeight / cellSize);
    const totalCells = numRows * numColumns;
    coloringBoard.style.gridTemplateColumns = `repeat(${numColumns},30px)`;
    coloringBoard.style.gridTemplateRows = `repeat(${numRows}, 30px)`;
    for (let i = 0; i < totalCells; i++) {
        let div = document.createElement("div");
        div.classList.add(("indv-cells"));
        coloringBoard.appendChild(div);
    }
}

function giveColorToSwatch() {
    for (let swatch of swatches) {
        swatch.style.backgroundColor = swatch.dataset.color;
    }
}

function selectColor(event) {
    console.log(event.target);
    if (event.target.classList.contains("color-swatch")) {
        selectedColor = event.target.dataset.color;
    }
}

function paintSquare(element) {
    element.style.backgroundColor = selectedColor;
}

function handleMouseDown(event) {
    event.preventDefault();
    mouseDown = true;
    if (event.target.classList.contains("indv-cells")) {
        paintSquare(event.target);
    }
}

function handleMouseOver(event) {
    if (mouseDown) {
        if (event.target.classList.contains("indv-cells")) {
            paintSquare(event.target)
        }
    }
}

colorPallete.addEventListener("click", selectColor);
coloringBoard.addEventListener("mousedown", handleMouseDown);
coloringBoard.addEventListener("mouseover", handleMouseOver);
coloringBoard.addEventListener("mouseup", handleMouseUp)

generateBoard();
giveColorToSwatch();
