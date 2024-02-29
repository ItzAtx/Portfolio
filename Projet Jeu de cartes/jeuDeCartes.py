import carte
import random

""" FR : SCRIPT CODÉ PAR ANTHONY VAUCHEL

    PROJET SCOLAIRE
    
    (classe pour pouvoir coder miniJeuCartes)
    Ce script permet plusieurs choses :
    - Définit un jeu de cartes
    - Permet de mélanger le paquet,
    - Affiche les cartes du paquet avec leurs caractéristiques
    - Peut distribuer les cartes en deux paquets égaux
    
    EN: SCRIPT CODED BY ANTHONY VAUCHEL
    
    SCHOOL PROJECT

    (Class to be able to code MiniJeuCartes)
    This script allows several things:
    - Defines a deck of cards
    - Enables shuffling the deck
    - Displays the cards in the deck with their characteristics
    - Can distribute the cards into two equal decks """
    
class jeuDeCartes:
    """ Classe définissant un jeu de cartes caractérisé par :
    - son nombre de cartes (32 ou 52)
    - son paquet de cartes (8 ou 13 cartes de chaque couleur) """
    
    def __init__(self, nb): #Notre méthode constructeur        
        """ Constructeur de la classe JeuDeCarte
        Pour créer le paquet de cartes classées par valeur et couleur
        Le paquet n'est pas mélangé """
        
        self.__NbCartes = nb 
        self.__Paquet = []
        if self.__NbCartes == 32:
            numeroDebut = 7
        else:
            numeroDebut = 2
        for coul in ["Pique", "Coeur", "Carreau", "Trèfle"]: 
            for val in range(numeroDebut, 15, 1):  # valeurs de 2 à 14 ou de 7 à 14
                new_carte = carte.Carte(val, coul)  # on crée une instance de Carte
                self.__Paquet.append(new_carte)    # on l'ajoute au paquet
                    
    def GetNbCarte(self):
        """ Retourne le nombre de carte du jeu de cartes """
        return self.__NbCartes
    
    def GetPaquet(self):
        """ Retourne le paquet de cartes"""
        return self.__Paquet
    
    def MelangerPaquet(self):
        """ Mélange aléatoirement le paquet de cartes """
        random.shuffle(self.__Paquet)
        
        
    def AfficherPaquet(self):
        """ Affiche le paquet de cartes avec Valeur Couleur Figure """
        print(" Valeur  Couleur  Figure \n")
        for i in range(len(self.__Paquet)):
            V = self.__Paquet[i].GetValeur()
            C = self.__Paquet[i].GetCouleur()
            F = self.__Paquet[i].GetFigure()
            print(" "*(4-V//10), V, " "*2, C, " "*(7-len(C)), F)
        print()
        
    def distribuer(self):
        """ Distribue les cartes en deux paquets de nombres égaux.
        Retourne deux paquets de cartes """
        random.shuffle(self.GetPaquet())  # Mélanger le paquet de cartes avant de distribuer
        moitie1 = self.GetPaquet()[:len(self.GetPaquet()) // 2]
        moitie2 = self.GetPaquet()[len(self.GetPaquet()) // 2:]
        return moitie1, moitie2