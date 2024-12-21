/*FR : PROJET CODÉ PAR ANTHONY VAUCHEL

PROJET PERSONNEL

Règles du jeu :

Ce jeu se base sur la simulation d'une petite ville dans un contexte de survie. On commence avec une population de 10 habitants et on doit gérer différentes ressources : le bois, l'or et la nourriture dans le but de faire croître sa population. On peut construire des bâtiments comme des fermes, des scieries, des maisons et des mines qui produisent des ressources chaque tour. Il y a aussi des risques, comme des catastrophes naturelles qui peuvent détruire des bâtiments ou une mauvaise gestion de la nourriture qui peut tuer une partie des habitants.

Le but du jeu est d'atteindre un certain niveau de développement (minimum de 50 habitants, 5 scieries, 5 fermes et 2 mines) tout en maintenant sa population en vie et nourrie. Si la population atteint 0, la partie est perdue, on doit donc intelligemment gérer les ressources, nourrir ses habitants, et prendre des décisions de construction pour atteindre l'objectif.

Ce projet a été développé dans le but de m'exercer sur les bases du langage C :
- Gestion des variables
- Utilisation des fonctions
- Boucles
- Structures conditionnelles

J'ai également appris à manipuler les générateurs de nombres aléatoires.
Je modifierais probablement le jeu au fur et à mesure pour ajouter des choses, si j'en ai le temps et l'envie. (peut-être "optimiser" le code en utilisant des tableaux) 



PROJECT CODED BY ANTHONY VAUCHEL

PERSONAL PROJECT

Game Rules:

This game is based on the simulation of a small town in a survival context. You start with a population of 10 inhabitants and must manage various resources: wood, gold, and food in order to grow your population. You can build buildings such as farms, sawmills, houses, and mines that produce resources each turn. There are also risks, such as natural disasters that can destroy buildings or poor food management that may kill part of the population.

The goal of the game is to reach a certain level of development (at least 50 inhabitants, 5 sawmills, 5 farms, and 2 mines) while keeping the population alive and fed. If the population reaches 0, the game is lost, so you must wisely manage resources, feed your inhabitants, and make construction decisions to reach the goal.

This project was developed to practice the basics of the C language:

- Variable management
- Function usage
- Loops
- Conditional structures
I also learned how to manipulate random number generators.
I will likely modify the game over time to add features, if I have the time and motivation. (Maybe "optimize" the code using arrays)*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//Fonction qui vérifie si les conditions de victoire sont remplies
int aGagne(int habitants, int scieries, int mines, int fermes) {
    if (habitants >= 50 && scieries >= 5 && fermes >= 5 && mines >= 2) {
        printf("\n🌟 Félicitations ! Vous avez gagné ! 🌟\n\n");
        return 1;
    }
    return 0;
}

//Fonction qui vérifie si les conditions pour perdre sont remplies
int aPerdu(int habitants) {
    if (habitants == 0) {
        printf("\n💀 Tous vos habitants sont morts... Vous avez perdu. 💀\n\n");
        return 1;
    }
    return 0;
}

//Fonction qui affiche les ressources actuelles
void afficherRessources(int monnaie, int nourriture, int bois) {
    printf("\n=== RESSOURCES ===\n");
    printf("  💰 Or          : %d\n", monnaie);
    printf("  🍎 Nourriture  : %d\n", nourriture);
    printf("  🪵 Bois        : %d\n", bois);
}

//Fonction qui affiche les bâtiments actuels
void afficherBatiments(int scieries, int fermes, int maisons, int mines) {
    printf("\n=== BÂTIMENTS ===\n");
    printf("  🪚 Scieries    : %d\n", scieries);
    printf("  🌾 Fermes      : %d\n", fermes);
    printf("  🏠 Maisons     : %d\n", maisons);
    printf("  ⛏️ Mines       : %d\n", mines);
}

//Fonction qui affiche le statut des habitants
void afficherStatutHab(int nbHabs, int statutNourris, int morts, int nes) {
    printf("\n=== STATUT DES HABITANTS ===\n");
    printf("  👥 Habitants actuels : %d\n", nbHabs);
    if (statutNourris == 2) {
        printf("  🍽️ Vos habitants sont nourris.\n");
    } else if (statutNourris == 1) {
        printf("  🍽️ Vos habitants ont faim !\n");
    } else {
        printf("  🚨 Vos habitants sont terriblement affamés !\n");
    }
    printf("  💀 Total morts : %d\n", morts);
    printf("  👶 Total nes   : %d\n", nes);
}

//Fonction pour "nourrir" les habitants
int nourrirHabitants(int nbHabitants, int qtNourriture, int sontNourris) {
    if (qtNourriture < nbHabitants) {
        printf("\n⚠️ Pas assez de nourriture pour nourrir vos habitants.\n");
        return sontNourris;
    } else if (sontNourris == 2) {
        printf("\n✅ Vos habitants sont déjà nourris.\n");
        return -1;
    } else {
        printf("\n✅ Vos habitants ont été nourris !\n");
        return 2;
    }
}

//Fonction qui retourne le nb de morts de vieillesse
int mortHabitants(int compteur, int habitants) {
    int morts = rand() % 6 + 1;
    if (compteur % 10 == 0) {
        morts += 1;
    }
    return morts > habitants ? habitants : morts;
}

//Fonction qui retourne le nb de naissances
int naissanceHabitants(int monnaie, int habitants, int maisons) {
    int maxVal = monnaie / 10;
    int naissances = rand() % (maxVal + 1);
    int capaciteMax = maisons * 2;
    int placesLibres = capaciteMax - habitants;

    if (placesLibres <= 0) {
        return 0;
    }

    if (naissances > placesLibres) {
        return placesLibres;
    }

    return naissances;
}

//Fonction qui affiche l'annonce principale
void annonces(int mortsF, int morts, int naissances, int sontNourris, int perteBat[], int maisons, int habitants) {
    printf("\n=== ANNONCES ===\n");
    printf("  💀 %d habitants sont morts.\n", morts);
    printf("  🚨 %d habitants sont morts de faim.\n", mortsF);
    printf("  👶 %d nouveaux habitants sont nés.\n", naissances);
    if (sontNourris == 1){
        printf("  🍽 Vos habitants ont faim.\n");
    } else if (sontNourris == 0){
        printf("  🚨 Vos habitants sont affamés !\n");
    }

    if (perteBat[0] > 0){
        printf("  Vous avez perdu %d scierie(s).\n", perteBat[0]);
    }
    if (perteBat[1] > 0){ 
        printf("  Vous avez perdu %d mine(s).\n", perteBat[1]);
    }
    if (perteBat[2] > 0){ 
        printf("  Vous avez perdu %d ferme(s).\n", perteBat[2]);
    }

    if (habitants >= maisons){
        printf("  ATTENTION ! Vous avez atteint la limite d'habitants possible avec vos maisons !\n");
    }
}

int construireFerme(int bois) {
    int qt = 0;
    printf("\n🌾 Une ferme coûte 10 bois.\n");
    printf("Combien de fermes voulez-vous construire ? (Vous avez %d bois)\n> ", bois);
    scanf("%d", &qt);
    if (10 * qt <= bois) {
        return qt;
    } else {
        printf("\n❌ Pas assez de ressources.\n");
        return 0;
    }
}

int construireScierie(int bois, int monnaie) {
    int qt = 0;
    printf("\n🪚 Une scierie coûte 10 bois et 5 or.\n");
    printf("Combien de scieries voulez-vous construire ? (Vous avez %d bois et %d or)\n> ", bois, monnaie);
    scanf("%d", &qt);
    if ((10 * qt <= bois) && (5 * qt <= monnaie)) {
        return qt;
    } else {
        printf("\n❌ Pas assez de ressources.\n");
        return 0;
    }
}

int construireMaison(int bois, int monnaie) {
    int qt = 0;
    printf("\n🏠 Une maison coûte 10 bois et 4 or.\n");
    printf("Combien de maisons voulez-vous construire ? (Vous avez %d bois et %d or)\n> ", bois, monnaie);
    scanf("%d", &qt);
    if ((10 * qt <= bois) && (4 * qt <= monnaie)) {
        return qt;
    } else {
        printf("\n❌ Pas assez de ressources.\n");
        return 0;
    }
}

int construireMine(int bois, int monnaie, int nourriture) {
    int qt = 0;
    printf("\n⛏️ Une mine coûte 15 bois, 10 or et 3 nourriture.\n");
    printf("Combien de mines voulez-vous construire ? (Vous avez %d bois, %d or et %d nourriture)\n> ", bois, monnaie, nourriture);
    scanf("%d", &qt);
    if ((15 * qt <= bois) && (10 * qt <= monnaie) && (3 * qt <= nourriture)) {
        return qt;
    } else {
        printf("\n❌ Pas assez de ressources.\n");
        return 0;
    }
}

int cataS(int scieries) {
    int pertes, alé;
    if (scieries >= 4) {
        alé = rand() % 100;
        if (alé < 4) {
            return rand() % 3;
        }
    }
    return 0;
}

int cataM(int mines) {
    int pertes, alé;
    if (mines >= 3) {
        alé = rand() % 100;
        if (alé < 4) {
            return rand() % 2;
        }
    }
    return 0;
}

int cataF(int fermes) {
    int pertes, alé;
    if (fermes >= 3) {
        alé = rand() % 100;
        if (alé < 4) {
            return rand() % 3;
        }
    }
    return 0;
}

int distribuerBois(int qtSci) { return qtSci * 5; }
int distribuerOr(int qtMin) { return qtMin * 5; }
int distribuerNourriture(int qtFer) { return qtFer * 5; }

int main() {
    int habitants = 10, morts = 0, nes = 0, pertes = 0, nouveaux = 0;
    int monnaie = 20, nourriture = 20, bois = 20;
    int fermes = 1, maisons = 5, scieries = 1, mines = 0, save = 0;
    int sontNourris = 0, etatNourriture, pertesF;
    int decision = -1, compteur = 1, deciBat = -1;
    int perteBat[3];

    srand(time(NULL));

    while (!aGagne(habitants, scieries, mines, fermes) && !aPerdu(habitants)) {
        printf("\n========== 🌟 TOUR %d 🌟 ==========\n", compteur);

        printf("\nQue souhaitez-vous faire ?\n");
        printf("  1️⃣ - Consulter vos ressources\n");
        printf("  2️⃣ - Consulter vos bâtiments\n");
        printf("  3️⃣ - Consulter le statut de vos habitants\n");
        printf("  4️⃣ - Nourrir les habitants\n");
        printf("  5️⃣ - Construire un batiment\n");
        printf("  6️⃣ - Passer au tour suivant\n");
        printf("  7️⃣ - Quitter le jeu\n> ");
        scanf("%d", &decision);

        if (decision == 1) {
            
            afficherRessources(monnaie, nourriture, bois);
            
        } else if (decision == 2) {
            
            afficherBatiments(scieries, fermes, maisons, mines);
            
        } else if (decision == 3) {
            afficherStatutHab(habitants, sontNourris, morts, nes);
            
        } else if (decision == 4) {
            
            etatNourriture = nourrirHabitants(habitants, nourriture, sontNourris);
            if (etatNourriture == 2) {
                nourriture -= habitants;
                sontNourris = etatNourriture;
            }
            
        
        } else if (decision == 5) {
            while (deciBat != 5) {
                printf("\nQuel bâtiment voulez-vous construire ?\n");
                printf("  1️⃣ - Ferme\n");
                printf("  2️⃣ - Scierie\n");
                printf("  3️⃣ - Maison\n");
                printf("  4️⃣ - Mine\n");
                printf("  5️⃣ - Quitter ce menu\n> ");
                scanf("%d", &deciBat);
                if (deciBat == 1) {
                    save = construireFerme(bois);
                    bois -= 10 * save;
                    fermes += save;
                } else if (deciBat == 2) {
                    save = construireScierie(bois, monnaie);
                    bois -= 10 * save;
                    monnaie -= 5 * save;
                    scieries += save;
                } else if (deciBat == 3) {
                    save = construireMaison(bois, monnaie);
                    bois -= 10 * save;
                    monnaie -= 4 * save;
                    maisons += save;
                } else if (deciBat == 4) {
                    save = construireMine(bois, monnaie, nourriture);
                    bois -= 15 * save;
                    monnaie -= 10 * save;
                    nourriture -= 3 * save;
                    mines += save;
                }
            }
            deciBat = -1;
            
        } else if (decision == 6) {
            compteur++;
            bois += distribuerBois(scieries);
            nourriture += distribuerNourriture(fermes);
            monnaie += distribuerOr(mines);

            pertes = mortHabitants(compteur, habitants);
            morts += pertes;
            habitants -= pertes;
            if (habitants < 0) { habitants = 0; }

            sontNourris -= 1;
            if (sontNourris < 0) {
                pertesF = habitants * 40 / 100;
                if (pertesF < 1 && habitants > 0) { pertesF = 1; }
                morts += pertesF;
                habitants -= pertesF;
                sontNourris = 0;
            }

            nouveaux = naissanceHabitants(monnaie, habitants, maisons);
            nes += nouveaux;
            habitants += nouveaux;

            perteBat[0] = cataS(scieries);
            perteBat[1] = cataM(mines);
            perteBat[2] = cataF(fermes);

            scieries -= perteBat[0];
            mines -= perteBat[1];
            fermes -= perteBat[2];

            annonces(pertesF, pertes, nouveaux, sontNourris, perteBat, maisons, habitants);
            
        } else if (decision == 7) {
            printf("\nMerci d'avoir joué ! À bientôt. 👋\n");
            break;
            
        } else {
            printf("\n❓ Commande inconnue. Veuillez saisir une option valide.\n");
        }
    }

    return 0;
}