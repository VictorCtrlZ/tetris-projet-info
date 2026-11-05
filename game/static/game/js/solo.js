
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

function drawCell(cells, board){
    drawBoard(canvas.width,canvas.height)

    //Dessine les pièces déjà posées dans la grille
    for(let y=0; y<board.length; y++){
        for(let x=0; x<board[y].length; x++){
            if(board[y][x] != 0){
                ctx.beginPath();
                ctx.rect(x*cellSize, y*cellSize, cellSize, cellSize);
                ctx.fill();
                ctx.stroke();
            }
        }
    }
    //Dessine la pièce actuelle
    ctx.fillStyle = figureColor;
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



function updateBoard(){
    fetch("/api/board/")
    .then(response=> response.json())
    .then(data => {

        canvas.width = data.width * cellSize;
        canvas.height = data.height * cellSize;

        drawBoard(data.width, data.height);
        drawCell(data.cells, data.board);
    });
}

function updateGame(){
    fetch("/api/update/")
        .then(response => response.json())
        .then(data => {
            drawBoard(data.width, data.height);
            drawCell(data.cells, data.board);
        });
}
updateBoard()
setInterval(updateGame,50)

function updateRotation() {
    fetch("/api/rotate")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board)
        })
}

function updateLeft() {
    fetch("/api/left")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board)
        })
}

function updateRight() {
    fetch("/api/right")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board)
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

    if(event.key === "ArrowDown"){
        fetch("/api/fastFall/?on=true");
    }

});

document.addEventListener("keyup", (event) => {
    if(event.key === "ArrowDown"){
        fetch("/api/fastFall/?on=false");
    }
});


