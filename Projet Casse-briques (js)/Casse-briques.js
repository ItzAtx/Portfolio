//On sélectionne le canva et on le défini
const canvas = document.getElementById("jeu");
const ctx = canvas.getContext("2d");

//Variables des paramètres du jeu
const hauteurRaquette = 10; //Hauteur de la raquette
const largeurRaquette = 75; //Largeur de la raquette
let positionRaquette = (canvas.width - largeurRaquette) / 2; //Position initiale de la raquette
const lignesBriques = 5; //Nombre de lignes de briques
const colonnesBriques = 5; //Nombre de colonnes de briques
const largeurBriques = 75; //Largeur des briques
const hauteurBriques = 20; //Hauteur des briques
const espaceBriques = 10; //Espace entre les briques
const margeSupBriques = 30; //Marge supérieure des briques
const margeGBriques = 30; //Marge gauche des briques
let perdu = false; //Variable qui indique si le jeu est terminé

//Variables pour la création des briques
let briques = [];
let valeurBriques = 10; //Valeur initiale des briques pour le score
reinitialiserBriques(); //On appelle la fonction pour initialiser les briques

//Variables des paramètres de la balle
const rayonBalle = 10; //Rayon de la balle
let x = canvas.width / 2; //Position horizontale initiale de la balle
let y = canvas.height - 30; //Position verticale initiale de la balle
let dx = 2; //Déplacement horizontal de la balle
let dy = -2; //Déplacement vertical de la balle
let mouvementsBalle = true; // Variable qui indique si la balle est en mouvement ou non

//Variables des contrôles
let droitActivé = false; //Indique si la touche de droite est enfoncée
let gaucheActivé = false; //Indique si la touche de gauche est enfoncée

//Variables pour la gestion des points et des vies
let score = 0; //Score du joueur
let vies = 3; //Nombre de vies du joueur
let scoreVies = 1500; //Nombre de points nécessaires pour gagner une vie supplémentaire

//Fonction pour afficher les points
function dessinerScore() {
    ctx.font = "16px Arial";
    ctx.fillStyle = "#0095DD";
    ctx.fillText("Score: " + score, 8, 20); //On affiche le score en haut à gauche du canvas
}

//Fonction pour afficher les vies
function dessinerVies() {
    ctx.font = "16px Arial";
    ctx.fillStyle = "#0095DD";
    ctx.fillText("vies: " + vies, canvas.width - 65, 20); //On affiche du le nombre vies en haut à droite du canvas
}

//Fonction de réinitialisation des briques
function reinitialiserBriques() {
    briques = [];
    for (let c = 0; c < colonnesBriques; c++) {
        briques[c] = [];
        for (let r = 0; r < lignesBriques; r++) {
            briques[c][r] = { x: 0, y: 0, status: 1 }; //On initialise une brique 
        }
    }
}

//Fonction pour déterminer si toutes les briques ont été cassées
function toutesCasses() {
    for (let c = 0; c < colonnesBriques; c++) {
        for (let r = 0; r < lignesBriques; r++) {
            if (briques[c][r].status === 1) {
                return false; //Renvoyer False si il reste des briques 
            }
        }
    }
    return true; //Renvoyer True si toutes les briques sont cassées
}

//Fonction pour la gestion de la raquette
function dessinerRaquette() {
    ctx.beginPath();
    ctx.rect(positionRaquette, canvas.height - hauteurRaquette - 10, largeurRaquette, hauteurRaquette); //On crée la raquette
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

//Fonction pour la gestion de la balle
function dessinerBalle() {
    ctx.beginPath();
    ctx.arc(x, y, rayonBalle, 0, Math.PI * 2); //On crée la balle
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

//Fonction pour la gestion des briques
function dessinerBriques() {
    for (let c = 0; c < colonnesBriques; c++) {
        for (let r = 0; r < lignesBriques; r++) {
            if (briques[c][r].status === 1) {
                const briqueX = (c * (largeurBriques + espaceBriques)) + margeGBriques; //Position horizontale de la brique
                const briqueY = (r * (hauteurBriques + espaceBriques)) + margeSupBriques; //Position verticale de la brique
                briques[c][r].x = briqueX; //Stockage de la position horizontale de la brique
                briques[c][r].y = briqueY; //Stockage de la position verticale de la brique
                ctx.beginPath();
                ctx.rect(briqueX, briqueY, largeurBriques, hauteurBriques); //On crée la brique dans le jeu
                ctx.fillStyle = "#0095DD";
                ctx.fill();
                ctx.closePath();
            }
        }
    }
}

//Fonction pour la gestion des collisions
function detectionCollisions() {
    //On vérifie les collisions avec les briques
    for (let c = 0; c < colonnesBriques; c++) {
        for (let r = 0; r < lignesBriques; r++) {
            const brique = briques[c][r];
            if (brique.status === 1) {
                if (
                    x + rayonBalle > brique.x &&
                    x - rayonBalle < brique.x + largeurBriques &&
                    y + rayonBalle > brique.y &&
                    y - rayonBalle < brique.y + hauteurBriques
                ) {
                    dy = -dy; //On inverse la direction verticale de la balle
                    brique.status = 0; //La brique touchée change son statut : elle n'existe plus
                    score += valeurBriques; //Si la balle a touché une brique on augmente le score
                    if (toutesCasses()) { //On vérifie si toutes les briques sont cassées, et si elles le sont :
                        reinitialiserBriques(); //On réinitialise les briques
                        valeurBriques += 10; //On augmente la valeur des briques pour le score
                        reinitialiserBalle(); //On réinitialise la position de la balle
                        mouvementsBalle = false; //On arrete la balle 
                        setTimeout(() => {
                            mouvementsBalle = true; //On laisse la balle bouger de nouveau après 1 seconde
                        }, 1000);
                        voirPourVieSupp(); //On vérifie si le joueur a gagné une vie supplémentaire (a accumulé 1500 pts ou +)
                    }
                }
            }
        }
    }

    //On vérifie les collisions avec la raquette
    const hautRaquette = canvas.height - hauteurRaquette - 10; //Position verticale haute de la raquette
    const basRaquette = canvas.height; //Position verticale basse de la raquette
    const gaucheRaquette = positionRaquette; //Position horizontale gauche de la raquette
    const droiteRaquette = positionRaquette + largeurRaquette; //Position horizontale droite de la raquette

    if (
        x + rayonBalle > gaucheRaquette &&
        x - rayonBalle < droiteRaquette &&
        y + rayonBalle > hautRaquette &&
        y - rayonBalle < basRaquette
    ) {
        dy = -dy; //On inverse la direction verticale de la balle
    }

    //On vérifie les collisions avec les murs gauche et droit
    if (x + dx > canvas.width - rayonBalle || x + dx < rayonBalle) {
        dx = -dx; //On inverse la direction horizontale de la balle
    }

    //On vérifie les collisions avec le mur du haut
    if (y + dy < rayonBalle) {
        dy = -dy; //On inverse la direction verticale de la balle
    }

    //Gestion de la perte de vie
    if (y + dy > canvas.height - rayonBalle) {
        if (x > positionRaquette && x < positionRaquette + largeurRaquette) {
            dy = -dy; //Inversion de la direction verticale de la balle
        } else {
            vies--; //On enlève une vie au joueur
            if (vies === 0) { //Si le joueur n'a plus de vies, fin du jeu
                perdu = true;
                alert("Vous avez perdu !! Votre score est de : " + score + " points");
                document.location.reload();
            } else { //Sinon, réinitialisation de la balle
                reinitialiserBalle();
                mouvementsBalle = false; //On arrête les mouvements de la balle
                setTimeout(() => {
                    mouvementsBalle = true; //On laisse la balle rebouger après 1 seconde
                }, 1000);
            }
        }
    }
}

//Fonction pour vérifier si le joueur a gagné une vie supplémentaire
function voirPourVieSupp() {
    if (score >= scoreVies) {
        vies++; //On ajoute une vie supplémentaire
        scoreVies += 1500; //On augmente le score nécessaire pour gagner une vie supplémentaire
    }
}

//Fonction pour la réinitialisation de la position de la balle, le maintiens de sa vitesse ou son augmentation si nécessaire
function reinitialiserBalle() {
    x = canvas.width / 2; //Position horizontale initiale de la balle
    y = canvas.height - 30; //Position verticale initiale de la balle

    //On augmente la vitesse de la balle si elle est inférieure à 5
    if (Math.abs(dx) < 5 && Math.abs(dy) < 5) {
        if (dx > 0) {
            dx += 0.5;
        } else if (dx < 0) {
            dx -= 0.5;
        }
        if (dy > 0) {
            dy += 0.5;
        } else if (dy < 0) {
            dy -= 0.5;
        }
    }
}

//Fonction pour le dessin principal
function draw() {
    if (!perdu) { //On vérifie si le jeu est terminé
        ctx.clearRect(0, 0, canvas.width, canvas.height); //On efface le canvas
        dessinerBriques(); //Dessin des briques
        dessinerBalle(); //Dessin de la balle
        dessinerRaquette(); //Dessin de la raquette
        dessinerScore(); //Affichage du score
        dessinerVies(); //Affichage du nombre de vies
        detectionCollisions(); //On itinialise la gestion des collisions

        //Déplacement de la raquette
        if (droitActivé && positionRaquette < canvas.width - largeurRaquette) {
            positionRaquette += 7; //Déplacement vers la droite
        } else if (gaucheActivé && positionRaquette > 0) {
            positionRaquette -= 7; //Déplacement vers la gauche
        }

        //Mouvement de la balle si elle est en mouvement
        if (mouvementsBalle) {
            x += dx; //Déplacement horizontal de la balle
            y += dy; //Déplacement vertical de la balle
        }

        requestAnimationFrame(draw); //Appel récursif pour continuer à dessiner
    }
}

//Gestion des touches
document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

//Fonction appelée lorsqu'une touche est enfoncée
function keyDownHandler(e) {
    if (e.key === "Right" || e.key === "ArrowRight") {
        droitActivé = true; //Marque la touche de droite comme enfoncée
    } else if (e.key === "Left" || e.key === "ArrowLeft") {
        gaucheActivé = true; //Marque la touche de gauche comme enfoncée
    }
}

//Fonction appelée lorsqu'une touche est relâchée
function keyUpHandler(e) {
    if (e.key === "Right" || e.key === "ArrowRight") {
        droitActivé = false; //Marque la touche de droite comme relâchée
    } else if (e.key === "Left" || e.key === "ArrowLeft") {
        gaucheActivé = false; //Marque la touche de gauche comme relâchée
    }
}

//Lance le jeu
draw(); //Appel de la fonction pour démarrer le jeu
