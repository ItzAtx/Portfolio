import tkinter as tk

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL

    PROJET PERSONNEL
    
    Le but de ce projet était de créer une v1 de quelque chose qui se rapprochait le plus du jeu Pac-Man en utilisant uniquement Tkinter.
    J'ai réussi à faire le niveau en entier et mettre quelques points de nourritures, je reste content du résultat, le but étant juste d'apprendre Tkinter un maximum.
    Au final j'aurais réussi plusieurs choses avec ce projet :
    - M'améliorer en terme de placement d'objets sur un canevas, surtout avec les rectangles où j'avais du mal
    - Essayer de créer de nouvelles choses tels que les déplacements du fantôme (que je n'ai pas réussi)
    - Tout ce qui est animation
    - Création de mouvements
    - Comment faire des collisions
    J'ai fait cette v1 dans le but de faire une autre version beaucoup plus performante et belle à l'aide de pygames plus tard.
    J'abandonne ce projet à ce point là car il m'as prit plus de temps que je ne le pensais pour un résultat que je trouve pas incroyable.
    Je préfère donc me pencher sur d'autres à la place.
    
    EN: PROJECT CODED BY ANTHONY VAUCHEL
    
    The purpose of this project was to create a v1 of something resembling Pac-Man using Tkinter exclusively. 
    I managed to create the entire level and place a few food points; I am satisfied with the result. The goal was simply to learn Tkinter to the fullest.
    In the end, I achieved several things with this project:
    - Improved my skills in placing objects on a canvas, especially with rectangles where I had difficulty
    - Attempted to create new elements such as ghost movements (which I did not succeed)
    - Animations
    - Implementation of movements
    - Understanding how to handle collisions

    I created this v1 with the intention of developing a much more efficient and aesthetically pleasing version using Pygame later on.
    I am abandoning this project at this point because it took more time than I anticipated for a result that I do not find incredible.
    I prefer to focus on other projects instead. """
    







class Fantome:
    def __init__(self, canvas, pacman, pacmanJeu):
        """ Initialise les propriétés du fantôme """
        self.canvas = canvas
        self.pacman = pacman
        self.pacmanJeu = pacmanJeu
        self.id = canvas.create_oval(295, 225, 315, 245, fill='red') #On crée le fantome
        self.deplacementX = 0
        self.deplacementY = 0

    def versPacman(self):
        """ Déplace le fantôme vers la position actuelle du Pac-Man """
        fantomeX, fantomey, _, _ = self.canvas.coords(self.id) #Permet d'obtenir les coordonnées x du coin supérieur gauche du rectangle englobant du fantôme et du pacman
        pacmanX, pacmanX, _, _ = self.canvas.coords(self.pacman) #Permet d'obtenir les coordonnées y

        distances = { #Le dictionnaire distances stocke les distances calculées
            'Left': abs(fantomeX - pacmanX - 20),  # -20 pour prendre en compte la taille du fantôme
            'Right': abs(fantomeX + 20 - pacmanX),  # 
            'Up': abs(fantomey - pacmanX - 20),  # -20 
            'Down': abs(fantomey + 20 - pacmanX)  # +20 
        }
        
        meilleureDirection = min(distances, key=distances.get) #Calcule les distances entre le fantôme et le pacman dans différentes directions et sélectionne ensuite la direction avec la distance minimale

        deplacementX, deplacementY = 0, 0

        if meilleureDirection == 'Left': #Déduit quelle est donc la meilleure direction où le fantome devrait aller
            deplacementX = -1
        elif meilleureDirection == 'Right':
            deplacementX = 1
        elif meilleureDirection == 'Up':
            deplacementY = -1
        elif meilleureDirection == 'Down':
            deplacementY = 1

        # Vérifier les collisions avec les murs avant de déplacer le fantôme
        if not self.pacmanJeu.verificationCollisionMurs((fantomeX + deplacementX, fantomey + deplacementY,
                                                          fantomeX + deplacementX + 20, fantomey + deplacementY + 20)):
            self.canvas.move(self.id, deplacementX, deplacementY)
            
            

    def poursuivrePacman(self):
        """ Méthode récursive qui appelle versPacman à intervalles réguliers """
        self.versPacman()
        self.canvas.after(10, self.poursuivrePacman)
        
        

class JeuPacman:
    def __init__(self, fenetreJeu):
        """  Initialise le jeu, crée le canevas, le Pac-Man, les murs, les fantômes, etc... """
        self.fenetreJeu = fenetreJeu
        self.fenetreJeu.title("Pac-Man") 
        self.canvas = tk.Canvas(fenetreJeu, width=590, height=700, bg='black')
        self.canvas.pack()
        self.pacman = self.canvas.create_arc(285, 490, 320, 525, start=45, extent=270, fill='yellow')
        self.listeNourritureFantomePositions = [(20, 483), (555, 483)]	
        self.listeNourriturePositions = [(25, 605), (50, 605), (75, 605), (100, 605), (125, 605),(150, 605),(175, 605),(200, 605),(225, 605),(250, 605),(275, 605),(300, 605),(325, 605),(350, 605),(375, 605),(400, 605),(425, 605),(450, 605),(475, 605),(500, 605),(525, 605),(550, 605),(565, 605),
                                          (25, 580), (275, 580), (325, 580),(565, 580),                
                                          (25, 550),(50, 550), (75, 550), (100, 550), (125, 550), (175, 550), (200, 550), (225, 550), (250, 550), (275, 550), (325, 550,), (350, 550), (375, 550), (400, 550), (425, 550), (475, 550),(500, 550),(525, 550),(550, 550),(565, 550),
                                          (60, 520), (125, 520), (175, 520), (415, 520), (475, 520), (525, 520),
                                          (60, 490), (125, 490),(150, 490),(175, 490),(200, 490),(225, 490),(250, 490),(275, 490),(300, 490),(325, 490),(350, 490),(375, 490),(400, 490),(425, 490),(450, 490),(475, 490), (525, 490)]
        
        
        
        
        self.fantome = Fantome(self.canvas, self.pacman, self)
        self.listeNourriture = []
        self.listeNourritureFantome = []
        self.direction = 'Up'
        self.score = 0
        self.fenetreJeu.bind('<KeyPress>', self.choisirTouche)
        self.labelScore = tk.Label(fenetreJeu, text="SCORE : 0")
        self.labelScore.place(x=400, y=670)
        self.boutonQuitter = tk.Button(fenetreJeu, text="QUITTER", command=fenetreJeu.destroy)
        self.boutonQuitter.place(x=200, y=670)
        
        self.creerNiveau()
        self.creerListeNourriture()
        self.creerListeNourritureFantome()
        self.mouvementsPacman()
        self.fantome.poursuivrePacman()
        

    def creerNiveau(self):
        """ Crée les murs et le design du niveau """
        
        #Coté gauche
        self.creerMur(0, 0, 10, 200)
        self.creerMur(100, 190, 10, 200)
        self.creerMur(90, 200, 100, 275)
        self.creerMur(100, 285, 0, 275)
        
        self.creerMur(0, 635, 10, 400)
        self.creerMur(10, 400, 100, 410)       
        self.creerMur(90, 400, 100, 335)
        self.creerMur(0, 325, 100, 335)
        
        #Haut et bas
        self.creerMur(10, 10, 590, 0)
        self.creerMur(10, 625, 590, 635)
        
        #Coté droit
        self.creerMur(580, 0, 591, 200)
        self.creerMur(590, 190, 490, 200)
        self.creerMur(490, 200, 500, 275)
        self.creerMur(490, 275, 602, 285)
        
        self.creerMur(591, 635, 580, 400)
        self.creerMur(490, 400, 590, 410)
        self.creerMur(490, 335, 500, 400)
        self.creerMur(490, 325, 602, 335)
        
        #Petits traits milieux
        self.creerMur(145, 325, 160, 410)
        self.creerMur(455, 325, 440, 410)
        
        #T sous le spawn à fantomes
        self.creerMur(200, 395, 397, 410)
        self.creerMur(295, 395, 310, 473)
        
        #Petits traits sous le T
        self.creerMur(145, 453, 250, 473)
        self.creerMur(355, 453, 455, 473)
        
        #L inversés
        self.creerMur(100, 453, 55, 473)
        self.creerMur(85, 473, 100, 530)
        
        self.creerMur(495, 453, 540, 473)
        self.creerMur(495, 473, 510, 530)
        
        #T déformés à l'envers
        self.creerMur(55, 570, 250, 585)
        self.creerMur(145, 585, 160, 515)
        
        self.creerMur(355, 570, 545, 585)
        self.creerMur(440, 585, 455, 515)
        
        #Traits qui depassent du mur
        self.creerMur(10, 515, 40, 530)
        self.creerMur(550, 515, 580, 530)
        
        #Deuxieme T en bas
        self.creerMur(200, 515, 397, 530)
        self.creerMur(295, 515, 310, 585)
        
        #Petits traits haut
        self.creerMur(50, 135, 100, 150)
        self.creerMur(490, 135, 540, 150)
        
        #Rectangle gauche droite
        self.creerMur(50, 50, 100, 100)
        self.creerMur(490, 50, 540, 100)
        
        #T gauche droite haut
        self.creerMur(145, 285, 160, 135)
        self.creerMur(145, 190, 250, 215)
        
        self.creerMur(440, 285, 455, 135)
        self.creerMur(355, 190, 455, 215)
        
        self.creerMur(205, 135, 400, 150)
        self.creerMur(295, 135, 310, 215) 
        
        #Colonne haut
        self.creerMur(295, 10, 310, 100)
        
        #Cage fantômes
        self.creerMur(200, 355, 397, 315)
        self.creerMur(200, 315, 210, 270)
        self.creerMur(397, 315, 387, 270)
        self.creerMur(200, 270, 397, 255)
        
        #Gros rectangles haut
        self.creerMur(145, 50, 250, 100)
        self.creerMur(355, 50, 460, 100)
        
        
     
    def jeuFini(self):
        """ Vérifie si le joueur a mangé toutes les nourritures """
        if len(self.listeNourriture) == 0 and len(self.listeNourritureFantome) == 0:
            self.fenetreJeu.destroy()
        
    def creerMur(self, x, y, x2, y2):
        """ Crée un mur sur le canevas """
        self.canvas.create_rectangle(x, y, x2, y2, outline='white', fill='blue')

    def creerNourriture(self, position):
        """ Crée le sprite de la nourriture """
        x, y = position
        nourriture = self.canvas.create_oval(x, y, x + 5, y + 5, fill='white')
        return nourriture
    
    def creerNourritureFantome(self, position):
        """ Crée le sprite de la nourriture qui fait fuir les fantômes """
        x, y = position
        nourritureFantome = self.canvas.create_oval(x, y, x + 20, y + 20, fill='white')
        return nourritureFantome
    
    def creerListeNourriture(self):
        """ Crée le nombre de nourriture que contient la liste dédiée"""
        for position in self.listeNourriturePositions:
            nourriture = self.creerNourriture(position)
            self.listeNourriture.append(nourriture)

    def creerListeNourritureFantome(self):
        """ Crée le nombre de nourritureFantome que contient la liste dédiée """
        for position in self.listeNourritureFantomePositions:
            nourritureFantome = self.creerNourritureFantome(position)
            self.listeNourritureFantome.append(nourritureFantome)
            self.animerNourritureFantome(nourritureFantome)

    def mouvementsPacman(self):
        """ Permet de déplacer le pacman et vérifie si le jeu est terminé ou non """
        x1, y1, x2, y2 = self.canvas.coords(self.pacman)

        # Calcul des nouvelles coordonnées après le mouvement
        if self.direction == 'Right': #Si la direction choisie est droite
            nouvellesCoordonnees = [x1 + 10, y1, x2 + 10, y2] #Pacman avance vers la droite
            if x2 > 600: # Vérification si le Pac-Man sort par le tunnel à droite
                nouvellesCoordonnees = [0, y1, 10, y2] #Si il a prit le tunnel de droite il ressort par celui de gauche
        elif self.direction == 'Left':
            nouvellesCoordonnees = [x1 - 10, y1, x2 - 10, y2] #Pacman avance vers la gauche 
            if x1 < 0: #Vérification si le Pac-Man sort par le tunnel à gauche
                nouvellesCoordonnees = [590, y1, 600, y2] #Si il a prit le tunnel de gauche il ressort par celui de droite
        elif self.direction == 'Up':
            nouvellesCoordonnees = [x1, y1 - 10, x2, y2 - 10] #Pacman avance vers le haut
        elif self.direction == 'Down':
            nouvellesCoordonnees = [x1, y1 + 10, x2, y2 + 10] #Pacman avance vers le bas

        # Vérification de la collision avec les murs
        if not self.verificationCollisionMurs(nouvellesCoordonnees): #Si pacman n'est pas contre un mur...
            self.canvas.move(self.pacman, nouvellesCoordonnees[0] - x1, nouvellesCoordonnees[1] - y1) #...On le laisse bouger
            self.animerPacman()#On lance les animations du pacman si il n'est pas contre un mur
            
        #Verification si pacman touche une nourriture   
        for nourriture in self.listeNourriture: #Pour le nombre d'éléments dans listeNourriture
            if self.verificationCollisionNourriture(nourriture): #On verifie si pacman est sur une nourriture
                self.score += 10 #Si oui on augmente les points de 10
                self.canvas.delete(nourriture) #On efface la nourriture qu'il a mangé du canevas...
                self.listeNourriture.remove(nourriture)  #...Et de la liste       
                self.mettreAJourScore() #On met à jour le label
                
        
        #Verification si pacman touche une nourriture   
        for nourritureFantome in self.listeNourritureFantome: #Pour le nombre d'éléments dans listeNourritureFantome
            if self.verificationCollisionNourritureFantome(nourritureFantome): #On verifie si pacman est sur une nourritureFantome
                self.score += 100 #Si oui on augmente les points de 10
                self.canvas.delete(nourritureFantome) #On efface la nourriture qu'il a mangé du canevas...
                self.listeNourritureFantome.remove(nourritureFantome)  #...Et de la liste       
                self.mettreAJourScore() #On met à jour le label
                
        self.jeuFini() #Vérifie si le joueur a mangé toutes les nourritures
        
        # Vérification si le Pac-Man touche un fantôme
        if self.verificationCollisionFantome():
            self.jeuFini()  #Ferme le jeu si le pacman touche un fantôme

            
        
        self.fenetreJeu.after(75, self.mouvementsPacman) #On définit le temps entre chaque déplacement du pacman
        
    def mettreAJourScore(self):
        """ Met à jour le labelScore avec la valeur actuelle du score """
        self.labelScore.config(text="SCORE : {}".format(self.score))
        
    def animerPacman(self):
        """ Anime le Pac-Man en fonction du mouvement """
            
        #Angle de départ et d'extension pour le pacman
        start_angle = 45
        extent_angle = 270

        #Calcul de l'angle en fonction de la direction du mouvement
        if self.direction == 'Right':
            angle = 0
        elif self.direction == 'Left':
            angle = 180
        elif self.direction == 'Up':
            angle = 90
        elif self.direction == 'Down':
            angle = -90       

        #Appeler la fonction récursivement pour une animation continue
        self.fenetreJeu.after(100, self.animerPacman)

        #Animation du Pacman
        self.canvas.itemconfig(self.pacman, start=start_angle + angle, extent=extent_angle)
        
    def animerNourritureFantome(self, nourritureFantome, temps=250):
        """ Fait clignoter la nourriture fantôme """
        self.canvas.itemconfig(nourritureFantome, state=tk.HIDDEN) #On change l'etat de la nourritureFantome à invisible...
        self.fenetreJeu.after(temps, lambda: self.canvas.itemconfig(nourritureFantome, state=tk.NORMAL)) #...Et on la remet visible
        self.fenetreJeu.after(2 * temps, lambda: self.animerNourritureFantome(nourritureFantome, temps)) #On planifie l'execution de la fonction pour créer le clignotement
        

    def verificationCollisionNourriture(self, nourriture):
        """ Vérifie la collision entre le Pac-Man et un élément de nourriture """
        pacmanEmplacement = self.canvas.coords(self.pacman)
        nourritureEmplacement = self.canvas.coords(nourriture)

        return pacmanEmplacement[0] < nourritureEmplacement[2] and pacmanEmplacement[2] > nourritureEmplacement[0] and \
               pacmanEmplacement[1] < nourritureEmplacement[3] and pacmanEmplacement[3] > nourritureEmplacement[1] #Renvoie True si il y a une interaction avec une nourriture
    
    def verificationCollisionNourritureFantome(self, nourritureFantome):
        """ Vérifie la collision entre le Pac-Man et un élément de nourriture """
        pacmanEmplacement = self.canvas.coords(self.pacman)
        nourritureEmplacementFantome = self.canvas.coords(nourritureFantome)

        return pacmanEmplacement[0] < nourritureEmplacementFantome[2] and pacmanEmplacement[2] > nourritureEmplacementFantome[0] and \
               pacmanEmplacement[1] < nourritureEmplacementFantome[3] and pacmanEmplacement[3] > nourritureEmplacementFantome[1] #Renvoie True si il y a une interaction avec une nourriture
    

    def verificationCollisionMurs(self, coords):
        """ Vérifie si les nouvelles coordonnées entrent en collision avec les murs """
        for mur in self.canvas.find_all(): #Pour le nombre de murs dans le canevas
            if self.canvas.itemcget(mur, 'outline') == 'white': #Si la couleur des bords des murs est blanc
                emplacementsMurs = self.canvas.coords(mur)
                if coords[0] < emplacementsMurs[2] and coords[2] > emplacementsMurs[0] and \
                   coords[1] < emplacementsMurs[3] and coords[3] > emplacementsMurs[1]: #Vérifier si le pacman est contre un mur
                    return True  #Si il est contre un mur retourner Vrai
        return False  #Sinon retourner Faux
    
    def verificationCollisionFantome(self):
        """ Vérifie la collision entre le pacman et le fantôme """
        pacmanEmplacement = self.canvas.coords(self.pacman)
        fantomeEmplacement = self.canvas.coords(self.fantome.id)

        return pacmanEmplacement[0] < fantomeEmplacement[2] and pacmanEmplacement[2] > fantomeEmplacement[0] and \
               pacmanEmplacement[1] < fantomeEmplacement[3] and pacmanEmplacement[3] > fantomeEmplacement[1] #Retourne True si pacman touche un fantome



    def choisirTouche(self, event):
        """ Gère les événements de pression des touches """
        if event.keysym in ['Right', 'Left', 'Up', 'Down']:
            self.direction = event.keysym

def main():
    """ La fonction principale """
    fenetreJeu = tk.Tk()
    pacman = JeuPacman(fenetreJeu)
    fenetreJeu.mainloop()

if __name__ == "__main__":
    main()


