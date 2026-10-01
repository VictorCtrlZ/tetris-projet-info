const canvas=document.getElementById("tetris");
const ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 400;

fetch("/api/trait/")
    .then(response => response.json())
    .then(traits => {
        dessinerTrait(traits);
    });

fetch("/api/grid/")
    .then(response=> response.json())
    .then(data => {
        console.log(data);

        const largeur = data.width;
        const hauteur = data.height;

        canvas.width = largeur * tailleCase;
        canvas.height = hauteur * tailleCase;

        dessinerGrille(largeur, hauteur);
    })
    .catch(error => {
        console.error("Erreur : ", error);
        }
    );


 const tailleCase = 25;

function dessinerGrille(largeur, hauteur){
    ctx.clearRect(0,0,canvas.width, canvas.height);

    for(let y=0; y<hauteur; y++){
        for (let x=0; x<largeur; x++){
            ctx.strokeRect(x*tailleCase, y*tailleCase, tailleCase, tailleCase);
        }
    }
}
dessinerGrille();