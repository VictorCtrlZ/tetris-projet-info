const canvas=document.getElementById("tetris");
const ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 400;

fetch("/api/trait/")
    .then(response => response.json())
    .then(traits => {
        dessinerTrait(traits);
    });

function dessinerTrait(traits){
    if (traits.length < 2){
        return;
    }
    ctx.moveTo(traits[0].x, traits[0].y);

    for (let i=1; i<traits.length; i++){
        ctx.lineTo(traits[i].x, traits[i].y);
    }
    ctx.stroke();
}