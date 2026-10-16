
const canvas=document.getElementById("tetris");
const ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 400;


const cellSize = 25;

function drawBoard(width, height){
    ctx.clearRect(0,0,canvas.width, canvas.height);
    ctx.strokeStyle = "black";
    for(let y=0; y<height; y++){
        for (let x=0; x<width; x++){
            ctx.strokeRect(x*cellSize, y*cellSize, cellSize, cellSize);
        }
    }
}

function drawCell(cells){
    ctx.clearRect(0,0,canvas.width, canvas.height);
    drawBoard(canvas.width,canvas.height)
    ctx.fillStyle = ctx.strokeStyle = figureColor;

    for (let i =0; i<cells.length; i++) {
        let x = cells[i][0];
        let y = cells[i][1];

        ctx.beginPath();
        ctx.rect(x*cellSize, y*cellSize, cellSize, cellSize);
        ctx.fill();
        ctx.stroke();
    }


}


function randomColor(){
    let colorsList = ['#a2ffd8', '#8194f6', '#c6ffc3',
            '#ffb180', '#ffe788', '#e8bcfb'];
    return colorsList[Math.floor(Math.random() * colorsList.length)];
}
let figureColor = randomColor();




fetch("/api/board/")
    .then(response=> response.json())
    .then(data => {

        canvas.width = data.width * cellSize;
        canvas.height = data.height * cellSize;

        drawBoard(data.width, data.height);
        drawCell(data.cells);
    });


function updateRotation() {
    fetch("/api/rotate")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells)
        })
}

function updateLeft() {
    fetch("/api/left")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells)
        })
}

function updateRight() {
    fetch("/api/right")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells)
        })
}

document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowUp") {
        updateRotation();
    }

    if (event.key === "ArrowLeft") {
        updateLeft();
    }

    if (event.key === "ArrowRight") {
        updateRight();
    }
});


