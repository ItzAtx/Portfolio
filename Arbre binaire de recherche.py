import tkinter as tk
from tkinter import messagebox

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL

    PROJET SCOLAIRE 
    
    Le but de ce projet est de créer une application qui permettra de dessiner un arbre binaire de recherche à partir de valeurs que l'utilisateur aura entrées.
    L'application sera séparée en 3 parties :
    - La partie de saisie des valeurs
    - La partie des boutons
    - La partie du dessin de l'arbre
    On utilisera les valeurs saisies pour construire un arbre binaire de recherche.
    Les valeurs ne doivent pas êtres inférieures à 1 ou supérieures à 999.
    La hauteur de l'arbre ne doit pas dépasser 3.
    Les différents boutons auront plusieurs fonctionnalités :
    - Quitter l'application
    - Créer une fenêtre Pop-Up qui donnera des informations sur l'application
    - Dessiner l'arbre 
    - Réinitialiser les valeurs saisies ainsi que l'arbre dessiné
    
    EN : PROJECT CODED BY ANTHONY VAUCHEL

    SCHOOL PROJECT 

    The goal of this project is to create an application that will allow the user to draw a binary search tree based on values they input.
    The application will be divided into 3 parts:
    - The input values section
    - The buttons section
    - The tree drawing section
    We will use the entered values to construct a binary search tree.
    Values should not be less than 1 or greater than 999.
    The height pf the tree should not exceed 3.
    - Various buttons will have multiple functionalities:
    - Exit the application
    - Create a Pop-Up window providing information about the application
    - Draw the tree
    Reset the entered values and the drawn tree"""

#---------------------------------------------------------------CLASSE DE L'ARBRE------------------------------------------------------------

class ArbreBinaireRecherche:
    def __init__(self, val):
        self.valeur = val
        self.sag = None
        self.sad = None
 
 
    def __str__(self):
        """ permet d'afficher la valeur de la racine de l'arbre """
        return str(self.valeur)
    
    
    def ajoute(self, cle):
        """ ajoute une clé à l'arbre binaire de recherche """
        if cle < self.valeur:
            if self.sag is None:
                self.sag = ArbreBinaireRecherche(cle)
            else:
                self.sag.ajoute(cle)
        elif cle > self.valeur:
            if self.sad is None:
                self.sad = ArbreBinaireRecherche(cle)
            else:
                self.sad.ajoute(cle)
                

    def taille(self):
        """ permet de renvoyer la taille de l'arbre """
        if self.sag == None:
            tSAG = 0
        else:
            tSAG = self.sag.taille()
        if self.sad == None:
            tSAD = 0
        else:
            tSAD = self.sad.taille()
        return 1+tSAG+tSAD
    
    
    def hauteur(self):
        """ permet de renvoyer la hauteur de l'arbre """
        if self.sag == None:
            hSAG = -1
        else:
            hSAG = self.sag.hauteur()
        if self.sad == None:
            hSAD = -1
        else:
            hSAD = self.sad.hauteur()
        return 1 + max(hSAG, hSAD)
    
    
    def afficheArbre(self, profondeur = 0):
        """ Permet l'affichage de l'arbre dans la console avec un décalage des noeuds propotionnel à la profondeur du noeud.
            L'affichage de l'arbre est horizontal (Droite en haut et Gauche en bas) """
        if self.sad:
            self.sad.afficheArbre(profondeur + 1)
        print(f"{profondeur * 6 * ' '}{self.valeur}")
        if self.sag:
            self.sag.afficheArbre(profondeur + 1)

#------------------------------------------------------------CLASSE DE L'APPLICATION---------------------------------------------------------



class Application:
        
    def __init__(self):
        
        #Création du canevas
        fenetre = tk.Tk()
        fenetre.title("Arbre Binaire de Recherche")
        self.canevas = tk.Canvas(fenetre, width = 1200, height = 700)
        self.canevas.create_line(700, 0, 700, 700)
        self.canevas.create_line(700, 450, 1200, 450)
        self.canevas.pack()
        
        #Création des widgets
        self.labelInc = tk.Label(fenetre, text = "propriété de Vauchel Inc®, ne pas copier sous peine d'emprisonnement")
        self.labelTaille = tk.Label(fenetre, fg="red", text="Taille :")
        self.labelTailleVar = tk.Label(fenetre, text=" ")
        self.labelHauteur = tk.Label(fenetre, fg="green", text="Hauteur :")
        self.labelHauteurVar = tk.Label(fenetre, text=" ")
        self.labelBoutons = tk.Label(fenetre, text="Zone des boutons utilitaires")
        self.labelArbre = tk.Label(fenetre, text="Zone du schéma de l'arbre")
        self.labelCles = tk.Label(fenetre, text="Zone de saisie des clés")
        self.labelRacine = tk.Label(fenetre, text="Entrez la racine voulue ici :")
        self.labelPositionCles = tk.Label(fenetre, text = "Entrez les valeurs des clés ci-dessous :")
        self.labelTailleVar = tk.Label(fenetre, text= ' ')

        self.boutonDessiner = tk.Button(fenetre, text = "Dessiner l'arbre", fg="green", command = self.recupererValeurs)
        self.boutonRéinitialiser = tk.Button(fenetre, text = "Réinitialiser l'arbre", fg="gray", command = self.reinitialiser)
        self.boutonAPropos = tk.Button(fenetre, text = "A propos", fg="blue", command=self.aPropos)
        self.boutonQuitter = tk.Button(fenetre, text = "Quitter le programme", command = fenetre.destroy)

        self.entréeRacine = tk.Entry(fenetre, width=5)
        self.entrée2 = tk.Entry(fenetre, width=5)
        self.entrée3 = tk.Entry(fenetre, width=5)
        self.entrée4 = tk.Entry(fenetre, width=5)
        self.entrée5 = tk.Entry(fenetre, width=5)
        self.entrée6 = tk.Entry(fenetre, width=5)
        self.entrée7 = tk.Entry(fenetre, width=5)
        self.entrée8 = tk.Entry(fenetre, width=5)
        self.entrée9 = tk.Entry(fenetre, width=5)
        self.entrée10 = tk.Entry(fenetre, width=5)
        self.entrée11 = tk.Entry(fenetre, width=5)
        self.entrée12 = tk.Entry(fenetre, width=5)
        self.entrée13 = tk.Entry(fenetre, width=5)
        self.entrée14 = tk.Entry(fenetre, width=5)
        self.entrée15 = tk.Entry(fenetre, width=5)

        #Positions des widgets
        self.boutonDessiner.place(x=820, y=520)
        self.boutonRéinitialiser.place(x=820, y=600)
        self.boutonAPropos.place(x=1000, y=525)
        self.boutonQuitter.place(x=1000, y=600)
        
        self.labelInc.place(x=820, y=685)
        self.labelHauteur.place(x= 850, y=425)
        self.labelHauteurVar.place(x= 910, y = 425)
        self.labelTaille.place(x=750, y=425)
        self.labelTailleVar.place(x= 790, y=425)
        self.labelCles.place(x= 875, y= 25)
        self.labelArbre.place(x= 275, y= 25)
        self.labelBoutons.place(x= 885, y= 470)
        self.labelRacine.place(x= 775, y=75)
        self.labelPositionCles.place(x=775, y=125)

        self.entréeRacine.place(x= 920, y= 75)
        self.entrée2.place(x=850, y=165)
        self.entrée3.place(x=900, y=165)
        self.entrée4.place(x=950, y=165)
        self.entrée5.place(x=850, y=195)
        self.entrée6.place(x=900, y=195)
        self.entrée7.place(x=950, y=195)
        self.entrée8.place(x=850, y=225)
        self.entrée9.place(x=900, y=225)
        self.entrée10.place(x=950, y=225)
        self.entrée11.place(x=850, y=255)
        self.entrée12.place(x=900, y=255)
        self.entrée13.place(x=950, y=255)
        self.entrée14.place(x=875, y=285)
        self.entrée15.place(x=925, y=285)
        
        
        #Fin du programme
        fenetre.mainloop()
        print("Programme terminé")

        
    def reinitialiser(self):
        """ Permet de réinitialiser totalement l'entièreté des variables pour construire un nouvel arbre """
        #Efface les valeurs dans les entrées
        self.entréeRacine.delete(0, tk.END)
        self.entrée2.delete(0, tk.END)
        self.entrée3.delete(0, tk.END)
        self.entrée4.delete(0, tk.END)
        self.entrée5.delete(0, tk.END)
        self.entrée6.delete(0, tk.END)
        self.entrée7.delete(0, tk.END)
        self.entrée8.delete(0, tk.END)
        self.entrée9.delete(0, tk.END)
        self.entrée10.delete(0, tk.END)
        self.entrée11.delete(0, tk.END)
        self.entrée12.delete(0, tk.END)
        self.entrée13.delete(0, tk.END)
        self.entrée14.delete(0, tk.END)
        self.entrée15.delete(0, tk.END)

        #Réinitialise la liste de valeurs
        self.valeurs = [''] * 15
        
        #Efface le contenu du canevas
        self.canevas.delete("all")
        
        #Redessine les lignes qui délimitent les trois parties effacées initialement
        self.canevas.create_line(700, 0, 700, 700)
        self.canevas.create_line(700, 450, 1200, 450)
        
        
    def aPropos(self):
        """ Permet d'ouvrir une fenêtre Pop Up qui expliquera comment utiliser l'application """
        #Création d'un nouveau canevas pour afficher les informations
        porte = tk.Tk()
        porte.title("Comment marche l'application ?")
        canevapa = tk.Canvas(porte, width= 640, height=180)
        canevapa.pack()
        
        #Les informations
        tk.Label(porte, fg="green", text="Cliquer sur le bouton Dessiner permet aux valeurs saisies d'apparaître dans l'arbre.").place(x=0, y=0)
        tk.Label(porte, fg="gray", text="Cliquer sur le bouton Réinitialiser effacera toutes les valeurs saisies ainsi que l'arbre.").place(x=0, y=20)
        tk.Label(porte, text="Cliquer sur le bouton Quitter permet de fermer l'application.").place(x= 0, y=40)
        tk.Label(porte, fg="lightblue", text="Vous devez saisirs les valeurs à mettre dans l'arbre binaire de recherche.").place(x=0, y=60)
        tk.Label(porte, fg="red", text="ATTENTION : La hauteur maximale de l'arbre que vous voulez dessiner ne doit pas dépasser 4.").place(x=0, y=80)
        tk.Label(porte, fg="red", text="ATTENTION : Les valeurs entrées ne doivent pas être inférieure à 1 ou supérieure à 999, et ce sont forcément des entiers.").place(x=0, y=100)
        tk.Label(porte, fg="red", text="ATTENTION : Vous ne pouvez pas rentrer deux fois la même valeur (en tout cas à ça crééra un arbre erroné.").place(x=0, y=120)
        tk.Label(porte, fg="red", text="REMARQUE : Si vous n'avez pas saisi de racine, la première valeur rentrée deviendra la racine.").place(x=0, y=140)
        tk.Label(porte, fg="blue", text="INFORMATION : Modifier une valeur saisie modifiera l'arbre en remplacant l'ancienne valeur par la nouvelle entrée.").place(x=0, y=160)

        
    def recupererValeurs(self):
        """ Récupère les valeurs entrées et vérifie si ce sont bien des entiers compris entre 1 et 999 et qu'il n'y ai pas de doublons """
        self.listeValeurs = [self.entréeRacine.get(), self.entrée2.get(), self.entrée3.get(), self.entrée4.get(),
                   self.entrée5.get(), self.entrée6.get(), self.entrée7.get(), self.entrée8.get(), self.entrée9.get(),
                   self.entrée10.get(), self.entrée11.get(), self.entrée12.get(),self.entrée13.get(), self.entrée14.get(),
                   self.entrée15.get()] #Récupère les valeurs entrées
        

        
        valeursInt = set()  #On utilise un ensemble pour vérifier les doublons

        for v in self.listeValeurs:
            if v:  #Si v existe (la valeur est autre chose que '')
                if not isinstance(v, (int, str)):
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")

                try:
                    valeurInt = int(v)
                except ValueError: #Si la valeur entrée est autre chose qu'un nombre entier, renvoyer une erreur
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "Les valeurs doivent uniquement être des entiers (réinitialisez pour recommencer).")
                    return

                if not (1 <= valeurInt <= 999):  #Si la valeur n'est pas comprise entre 1 et 999, renvoyer une erreur
                    tk.messagebox.showerror("Erreur", "Les valeurs doivent être des entiers entre 1 et 999 (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", "La valeur doit être un entier entre 1 et 999 (réinitialisez pour recommencer).")
                    return

                if valeurInt in valeursInt:  #Si la valeur est déjà dans la liste, renvoyer une erreur
                    tk.messagebox.showerror("Erreur", f"La valeur {valeurInt} a été saisie plus d'une fois (réinitialisez pour recommencer).")
                    raise ValueError("Erreur", f"La valeur {valeurInt} a été saisie plus d'une fois (réinitialisez pour recommencer).")
                    return

                valeursInt.add(valeurInt)  #Ajouter la valeur à l'ensemble
        
        self.creationArbre() #Si il n'y a aucune erreur, on commence à créer l'arbre
                        
        
    def creationArbre(self):
        """ Crée l'arbre avec les valeurs correctement saisies, vérifie si la liste n'est pas vide et que la hauteur maximale n'est pas dépassée
            et met à jour l'arbre si une valeur est remplacé par une autre """
        valeursInt = [int(v) if v else None for v in self.listeValeurs]  #Convertit en int seulement si la valeur n'est pas vide
        valeursInt = list(filter(None, valeursInt))  #Supprime les valeurs None

        if valeursInt == []: #Si la liste est vide, renvoyer une erreur
            tk.messagebox.showerror("Erreur", "Veuillez entrer au moins une valeur pour construire un arbre.")
            raise ValueError("Erreur:", "Veuillez entrer au moins une valeur pour construire un arbre.")

        #Crée un arbre avec les valeurs actuelles/nouvelles
        AB1 = ArbreBinaireRecherche(valeursInt[0])
        for valeur in valeursInt[1:]:
            AB1.ajoute(valeur)

        self.taille = AB1.taille()
        self.labelTailleVar.config(text=self.taille)  #Renvoie la taille
        self.hauteur = AB1.hauteur()
        self.labelHauteurVar.config(text=self.hauteur)  #Renvoie la hauteur
        if self.hauteur > 4:  #Test si la hauteur maximale n'est pas dépassée
            tk.messagebox.showerror("Erreur", "La hauteur maximale de l'arbre doit être de 4.")
            raise ValueError("Erreur", "La hauteur maximale de l'arbre doit être de 4.")

        #Efface le contenu du canevas
        self.canevas.delete("all")

        #Redessine les lignes qui délimitent les trois parties effacées initialement
        self.canevas.create_line(700, 0, 700, 700)
        self.canevas.create_line(700, 450, 1200, 450)
        
        self.dessinerArbre(AB1, 375, 150, 3)
        
 
    
    def dessinerArbre(self, arbre, x, y, niveau, largeur=700, espacementHorizontal=150, espaceVertical = 100):
        """ Dessine l'arbre sur le canevas avec les valeurs entrées triées pour créer un arbre binaire de recherche """
        rayon = 20  #Rayon du cercle représentant un nœud

        if arbre:
            #Dessiner le nœud
            self.canevas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill="lightblue")
            self.canevas.create_text(x, y, text=str(arbre.valeur))

            #Dessiner la branche gauche
            if arbre.sag:
                xGauche = x - espacementHorizontal
                yGauche = y + espaceVertical
                self.canevas.create_line(x, y + rayon, xGauche, yGauche - rayon, width=2, fill="black")
                self.dessinerArbre(arbre.sag, xGauche, yGauche, niveau - 1, largeur / 2, espacementHorizontal / 2)

            #Dessiner la branche droite
            if arbre.sad:
                xDroite = x + espacementHorizontal
                yDroite = y + espaceVertical
                self.canevas.create_line(x, y + rayon, xDroite, yDroite - rayon, width=2, fill="black")
                self.dessinerArbre(arbre.sad, xDroite, yDroite, niveau - 1, largeur / 2, espacementHorizontal / 2)
 
 
application = Application()
