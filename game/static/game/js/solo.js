const canvas=document.getElementById("tetris");
const ctx = canvas.getContext("2d");

const nexPieceCanvas=document.getElementById("next-piece");
const nextPieceCtx=nexPieceCanvas.getContext("2d");

canvas.width = 400;
canvas.height = 400;


const cellSize = 25;
const nextPieceCellSize=20;

let gameEnded = false;
let gameInterval;

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

function drawNextPiece(nextPiece, nextColor){
    nextPieceCtx.clearRect(0,0,nexPieceCanvas.width, nexPieceCanvas.height);

    if(!nextPiece||nextPiece.length === 0){
        return;
    }

    let minX=nextPiece[0][0];
    let minY=nextPiece[0][1];

    for(let i=0;i<nextPiece.length;i++){
        if(nextPiece[i][0]<minX){
            minX=nextPiece[i][0];
        }
        if(nextPiece[i][1]<minY){
            minY=nextPiece[i][1];
        }
    }
    nextPieceCtx.fillStyle=nextColor;
    nextPieceCtx.strokeStyle="black";

    for(let i=0;i<nextPiece.length;i++){
        let x = nextPiece[i][0]-minX;
        let y=nextPiece[i][1]-minY;

        nextPieceCtx.beginPath();
        nextPieceCtx.rect(x*nextPieceCellSize, y*nextPieceCellSize, nextPieceCellSize, nextPieceCellSize);
        nextPieceCtx.fill();
        nextPieceCtx.stroke();

    }
}


function updateBoard(){
    fetch("/board/")
    .then(response=> response.json())
    .then(data => {

        canvas.width = data.width * cellSize;
        canvas.height = data.height * cellSize;

        drawCell(data.cells, data.board, data.currentColor);
        drawNextPiece(data.nextPiece, data.nextColor);
    });
}

function updateGame(){
    fetch("/update/")
        .then(response => response.json())
        .then(data => {

            updateScore(data);

            if(data.gameOver){
                gameEnded = true;
                document.getElementById("game-over").style.display = "flex";
                clearInterval(gameInterval);
                return;
            }

            drawCell(data.cells, data.board, data.currentColor);
            drawNextPiece(data.nextPiece, data.nextColor);
        });
}
updateBoard()
gameInterval=setInterval(updateGame,50)

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


document.getElementById("restart").addEventListener("click",() => {
    fetch("/restart/")
        .then(response => response.json())
        .then(data => {
            gameEnded = false;
            document.getElementById("game-over").style.display="none";
            drawCell(data.cells, data.board, data.currentColor);
            drawNextPiece(data.nextPiece, data.nextColor);
            updateScore(data);
            gameInterval=setInterval(updateGame,50)
        })
})

