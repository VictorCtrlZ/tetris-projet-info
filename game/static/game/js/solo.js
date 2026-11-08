
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

function drawCell(cells, board, currentColor){
    drawBoard(board[0].length,board.length)

    //Dessine les pièces déjà posées dans la grille
    for(let y=0; y<board.length; y++){
        for(let x=0; x<board[y].length; x++){
            if(board[y][x] != 0){
                ctx.fillStyle = board[y][x];
                ctx.beginPath();
                ctx.rect(x*cellSize, y*cellSize, cellSize, cellSize);
                ctx.fill();
                ctx.stroke();
            }
        }
    }
    //Dessine la pièce actuelle
    ctx.fillStyle = currentColor;
    for (let i =0; i<cells.length; i++) {
        let x = cells[i][0];
        let y = cells[i][1];

        ctx.beginPath();
        ctx.rect(x*cellSize, y*cellSize, cellSize, cellSize);
        ctx.fill();
        ctx.stroke();
    }
}




function updateBoard(){
    fetch("/board/")
    .then(response=> response.json())
    .then(data => {

        canvas.width = data.width * cellSize;
        canvas.height = data.height * cellSize;

        drawCell(data.cells, data.board, data.currentColor);
    });
}

function updateGame(){
    fetch("/update/")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board, data.currentColor);
            updateScore(data);
        });
}
updateBoard()
setInterval(updateGame,50)

function updateRotation() {
    fetch("/rotate/")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board,data.currentColor)
        })
}

function updateLeft() {
    fetch("/left/")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board,data.currentColor)
        })
}

function updateRight() {
    fetch("/right/")
        .then(response => response.json())
        .then(data => {
            drawCell(data.cells, data.board, data.currentColor)
        })
}


function updateScore(data) {
    document.getElementById("score").textContent=data.score;
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
        fetch("/fastFall/?on=true");
    }

});

document.addEventListener("keyup", (event) => {
    if(event.key === "ArrowDown"){
        fetch("/fastFall/?on=false");
    }
});


