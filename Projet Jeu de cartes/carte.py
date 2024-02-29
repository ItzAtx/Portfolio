""" FR : SCRIPT CODÉ PAR ANTHONY VAUCHEL

    PROJET SCOLAIRE
    
    (classe pour pouvoir coder jeuDeCartes)
    Ce script permet de créer une carte avec ses caractéristiques
    Elle permettra finalement de pouvoir créer miniJeuCartes
    
    
    EN: SCRIPT CODED BY ANTHONY VAUCHEL
    
    SCHOOL PROJECT

    (Class to be able to code jeuDeCartes)
    This script allows creating a card with its characteristics.
    Ultimately, it will be used to create miniJeuCartes. """
    



class Carte :
    """ Classe définissant une carte caractérisée par :
    - sa valeur
    - sa couleur
    - sa figure """
    
    def __init__(self, val, coul): # Notre méthode constructeur
        """ Constructeur de la classe carte """
        self.__valeur = val
        self.__couleur = coul
        if val == 11:
            self.__figure = "Valet"
        elif val == 12 :
            self.__figure = "Dame"
        elif val == 13:
            self.__figure = "Roi"
        elif val == 14:
            self.__figure = "As"
        else:
            self.__figure = "Aucune"
            
    def GetValeur(self):
        """ Retourne la valeur d'une carte """
        return self.__valeur
        
    def GetCouleur(self):
        """ Retourne la couleur d'une carte """
        return self.__couleur
        
    def GetFigure(self):
        """ Retourne la figure d'une carte """
        return self.__figure
        
    def __SetFigure(self, val):
        """ Méthode privée pour changer la figure en fonction de la nouvelle valeur val """
        if val == 11:
            self.__figure = "Valet"
        elif val == 12 :
            self.__figure = "Dame"
        elif val == 13:
            self.__figure = "Roi"
        elif val == 14:
            self.__figure = "As"
        else:
            self.__figure = "Aucune"
                
    def SetValeur(self, val):
        """ Retourne Vrai si la valeur de la carte a été changé par val
            Retourne Faux sinon (valeur non comprise dans l'intervalle [2; 14]) """
        if 2 <= val <= 14:
            self.__valeur = val
            self.__SetFigure(val)
            return True
        else:
            return False
            
    def SetCouleur(self, coul):
        """ Retourne Vrai si la couleur de la carte a été changé par coul
            Retourne Faux sinon (valeur non comprise dans l'intervalle [2; 14]) """
        lst_couleur = ["Carreaux", "Coeur", "Pique", "Trèfle"]
        if coul in lst_couleur:
            self.__couleur = coul
            return True
        else:
            return False

    def GetIcon(self):
        """ envoie un symbole Unicode correspondant au symbole de la carte """
        if self.GetCouleur() == "Pique":
            return chr(0x2660)
        elif self.GetCouleur() == "Coeur":
            return "\x1B[31m" + chr(0x2665) + "\x1B[0m"
        elif self.GetCouleur() == "Carreau":
            return "\x1B[31m" + chr(0x2666) + "\x1B[0m"
        else :
            return chr(0x2663)
        
    def GetGrade(self):
        """ retourne une représentation symbolique de la valeur de la carte """
        if self.GetValeur() == 11:
            return "V"
        elif self.GetValeur() == 12:
            return "D"
        elif self.GetValeur() == 13:
            return "R"
        elif self.GetValeur() == 14:
            return "A"
        else:
            return self.GetValeur()

