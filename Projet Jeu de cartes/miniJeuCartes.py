from jeuDeCartes import *
import carte
import time

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL

    PROJET SCOLAIRE
    
    Le but de ce projet est de créer un jeu de 32 cartes, le partager en 4 paquets de taille identique et les assimiler à 4 joueurs.
    On additionnera les valeurs des cartes de chacun des deux paquets, le joueur qui gagne est celui qui a la valeur la plus élevée.
    ON UTILISERA LES CLASSES carte ET jeuDeCartes CODÉES PRÉCÉDEMMENT.
    
    EN : PROJECT CODED BY ANTHONY VAUCHEL

    SCHOOL PROJECT
    
    The goal of this project is to create a card game with 32 cards, divide them into 4 equally-sized decks, and associate them with 4 players.
    The values of the cards in each player's deck will be added up, and the player with the highest total value wins.
    
    WE WILL BE USING THE PREVIOUSLY CODED CLASSES carte AND jeuDeCartes FOR THIS PROJECT. """
    

def ValeurPaquet(paquet,joueur):
    """ cette fonction prend un paquet de cartes et le joueur associé 
        retourne la valeur totale du paquet des joueurs
        retourne la liste des valeurs des cartes du paquet du joueur
        la fonction parcourt chaque carte du paquet, récupère sa valeur et sa couleur, puis les ajoute à la liste ListeValeurs
        la valeur totale du paquet est également calculée """
    
    coul = "\x1B[0m"
    ValeurP = 0
    ListeValeurs = "\x1B[32m" + "Jeu du joueur " + joueur + " : " + "\x1B[0m"
    for carte in paquet:
        valeur = str(carte.GetValeur())
        if carte.GetCouleur() == 'Pique':
            coul = "\x1B[30m" + chr(0x2660) + "\x1B[0m"
        elif carte.GetCouleur() == 'Coeur':
            coul = "\x1B[31m" + chr(0x2665) + "\x1B[0m"
        elif carte.GetCouleur() == 'Carreau':
            coul = "\x1B[31m" + chr(0x2666) + "\x1B[0m"
        elif carte.GetCouleur() == 'Trèfle':
            coul = "\x1B[30m" + chr(0x2663) + "\x1B[0m"
        if valeur == '14':
            valeur = 'A'
        if valeur == '13':
            valeur = 'R'
        if valeur == '12':
            valeur = 'D'
        if valeur == '11':
            valeur = 'V'
        ListeValeurs = ListeValeurs + valeur + coul +" " + "\x1B[0m"
        ValeurP = ValeurP + carte.GetValeur()
    return ValeurP,ListeValeurs


#Création d'un paquet de 32 cartes mélangées
MonPaquet = jeuDeCartes(32)
MonPaquet.MelangerPaquet()
ScoreMax = 0
NombresParties = 0


#Initialisation des joueurs
JoueurA = "A"
JoueurB = "B"
JoueurC = "C"
JoueurD = "D"
#Initialisation des paquets des joueurs   
PaquetA = [MonPaquet.GetPaquet()[4*i] for i in range(8)]
PaquetB = [MonPaquet.GetPaquet()[4*i+1] for i in range(8)]
PaquetC = [MonPaquet.GetPaquet()[4*i+2] for i in range(8)]
PaquetD = [MonPaquet.GetPaquet()[4*i+3] for i in range(8)]

#Calcul des valeurs des paquets
ValeurPaquetA,ListeValeursA = ValeurPaquet(PaquetA, JoueurA)
ValeurPaquetB,ListeValeursB = ValeurPaquet(PaquetB, JoueurB)
ValeurPaquetC,ListeValeursC = ValeurPaquet(PaquetC, JoueurC)
ValeurPaquetD,ListeValeursD = ValeurPaquet(PaquetD, JoueurD)
 
#Détermination du gagnant
ScoreMax = max(ValeurPaquetA,ValeurPaquetB,ValeurPaquetC,ValeurPaquetD)

#Affichage des paquets et de leurs valeurs
print("\n",ListeValeursA)
print("\x1B[32m" + "Valeur du Paquet A :" + "\x1B[0m",ValeurPaquetA)
print("\n",ListeValeursB)
print("\x1B[32m" + "Valeur du Paquet B :" + "\x1B[0m",ValeurPaquetB)
print("\n",ListeValeursC)
print("\x1B[32m" + "Valeur du Paquet C :" + "\x1B[0m",ValeurPaquetC)
print("\n",ListeValeursD)
print("\x1B[32m" + "Valeur du Paquet D :" + "\x1B[0m",ValeurPaquetD)
    



if ValeurPaquetA == ScoreMax:
    print("\x1B[31m" + "\nLe joueur A gagne avec un total de", ValeurPaquetA)
elif ValeurPaquetB == ScoreMax:
    print("\x1B[31m" + "\nLe joueur B gagne avec un total de", ValeurPaquetB)
elif ValeurPaquetC == ScoreMax:
    print("\x1B[31m" + "\nLe joueur C gagne avec un total de", ValeurPaquetC)
elif ValeurPaquetD == ScoreMax:
    print("\x1B[31m" + "\nLe joueur D gagne avec un total de", ValeurPaquetD)
    
