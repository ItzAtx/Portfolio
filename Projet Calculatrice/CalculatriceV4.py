import tkinter as tk
from math import log

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL
    
    PROJET PERSONNEL
    
    Le but de ce projet est d'améliorer au fur et à mesure la calculatrice créée précédemment.
    Dans cette V4, on aura ajouté :
    - Le calcul d'exponentielles
    - Le calcul de logarithmes naturels
    - La constante pi
    
    EN : PROJECT CODED BY ANTHONY VAUCHEL
    
    PERSONAL PROJECT
    
    The purpose of this project is to gradually enhance the previously created calculator. In this V4, the following features will have been added:
    - Exponential calculation
    - Natural logarithm calculation
    - The constant pi"""




pi = 3.14159265358979323846

def evaluerExpression(expression):
    """ Évalue l'expression en prenant en charge la puissance et la racine carrée """
    expression = expression.replace("^", "**")
    expression = expression.replace("π", "3.14159265358979323846")
    
    #Fonction de la racine carrée personnalisée
    def sqrt(x):
        return x ** 0.5
    
    #Fonction de l'exponentielle personnalisée
    def exponentielle(x):
        return 2.718281828459045 ** x
    
    #Fonction du logarithme personnalisée
    def ln(x):
        return log(x)     
    
    # Dictionnaire des fonctions personnalisées
    FonctionsPersos = {"sqrt" : sqrt, "exp" : exponentielle, "ln": ln}
    
    # Évaluation de l'expression en utilisant eval, avec les fonctions personnalisées
    try:
        resultat = eval(expression, {}, FonctionsPersos)
        return resultat
    except Exception as error:
        raise ValueError("Erreur d'évaluation")


def evenement(valeurBouton):
    """ Fonction pour gérer les événements des boutons """
    texte = texteEntree.get()

    try:
        if valeurBouton == "=":
            #Évalue l'expression et afficher le résultat
            resultat = evaluerExpression(texte)

            #Formate le résultat en tant qu'entier s'il n'y a pas de décimales
            if isinstance(resultat, float) and resultat.is_integer():
                resultat = int(resultat)

            texteEntree.set(resultat)
            texteResultat.set("")
            historiqueCalculs.append((texte, resultat))
        elif valeurBouton == "DEL":
            #Supprime le dernier caractère
            texteEntree.set(texte[:-1])
            texteResultat.set("")
        elif valeurBouton == "^":
            #Ajoute '^' à l'expression
            texteEntree.set(texte + "^")
        elif valeurBouton == "sqrt":
            #Ajoute 'sqrt(' à l'expression
            texteEntree.set(texte + "sqrt(")
        elif valeurBouton == 'exp':
            # Ajoute 'exp(' à l'expression
            texteEntree.set(texte + "exp(")
        elif valeurBouton == 'ln':
            # Ajoute 'log(' à l'expression
            texteEntree.set(texte + "ln(")
        elif valeurBouton == 'π':
            # Ajoute 'pi' à l'expression
            texteEntree.set(texte + "π")
        else:
            # Ajouter le bouton pressé à l'expression et mettre à jour le résultat en temps réel
            texteEntree.set(texte + valeurBouton)
            if valeurBouton in ['+', '-', '*', '/']:
                texteResultat.set("")
            else:
                texteResultat.set(evaluerExpression(texte + valeurBouton))
    except ValueError as error:
        #Gère les erreurs d'évaluation
        texteResultat.set("Error")

    if valeurBouton == "C":
        #Réinitialise l'expression et le résultat
        texteEntree.set("")
        texteResultat.set("")

def afficherHistorique():
    """ Permet d'afficher l'historique des calculs """
    fenetreHistorique = tk.Toplevel(fenetre)
    fenetreHistorique.title("Historique des Calculs")

    texteHistorique = tk.Text(fenetreHistorique, wrap="none", font=('Helvetica', 12), height=20, width=50)
    texteHistorique.pack()

    for calcul in historiqueCalculs:
        texteHistorique.insert(tk.END, f"{calcul[0]} = {calcul[1]}\n")

def changerTheme():
    """ Change la couleur des boutons tour à tour """
    global indexThemeActuel

    #Incrémente l'index du thème
    indexThemeActuel += 1
    if indexThemeActuel >= len(themes):
        indexThemeActuel = 0

    #Sélectionne le thème en fonction de l'index
    theme = list(themes.keys())[indexThemeActuel]
    couleurTheme = themes[theme]

    #Met à jour les couleurs de l'application
    fenetre.configure(bg=couleurTheme)
    entreeAffichage.configure(bg=couleurTheme)
    for widget in fenetre.winfo_children():
        if isinstance(widget, tk.Button):
            widget.configure(bg=couleurTheme)

#Initialisation de l'historique
historiqueCalculs = []

#Définition des thèmes
themes = {
    "1": "grey85",
    "2": "AntiqueWhite2",
    "3": "LightSkyBlue1",
    "4": "darkolivegreen3",
    "5": "pink",
    "6": "lightslateblue"
}

#Index du thème actuel
indexThemeActuel = 1

#Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.configure(bg='white')  # Couleur de fond initiale

#Variables pour l'affichage
texteEntree = tk.StringVar()
texteEntree.set("")

texteResultat = tk.StringVar()
texteResultat.set("")

#Zone d'affichage des calculs
entreeAffichage = tk.Entry(fenetre, textvariable=texteEntree, font=('Helvetica', 18), justify='center')
entreeAffichage.grid(row=0, column=0, columnspan=4, sticky="ew", ipadx=10)

#Zone d'affichage du résultat en temps réel
labelResultat = tk.Label(fenetre, textvariable=texteResultat, font=('Helvetica', 14), justify='center')
labelResultat.grid(row=1, column=0, columnspan=4, sticky="ew")

#Liste des boutons de la calculatrice
boutons = [
    'exp', 'ln', 'π', '',
    '(', ')', '^', 'sqrt',
    '7', '8', '9', 'DEL',
    '4', '5', '6', '/',
    '1', '2', '3', '*',
    '0', '.', '=', '-',
    'C', 'T', 'H', '+'
]

ligne = 2
colonne = 0

#Taille fixe pour tous les boutons
largeurBouton = 10
hauteurBouton = 2

#Crée les boutons grâce à une boucle
for touches in boutons:
    if touches == 'H':
        tk.Button(fenetre, text=touches, width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=afficherHistorique).grid(row=ligne, column=colonne, columnspan=1)
    elif touches == 'T':
        tk.Button(fenetre, text=touches, width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=changerTheme).grid(row=ligne, column=colonne, columnspan=1)
    elif touches == '^':
        #Ajouter le bouton puissance avec le texte '^'
        tk.Button(fenetre, text='^', width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=lambda b='^': evenement(b)).grid(row=ligne, column=colonne, columnspan=1)
    elif touches == 'sqrt':
        #Ajouter le bouton racine carrée avec le texte '√'
        tk.Button(fenetre, text='√', width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=lambda b='sqrt': evenement(b)).grid(row=ligne, column=colonne, columnspan=1)
    elif touches == 'exp':
        #Ajouter le bouton exponentielle avec le texte 'exp'
        tk.Button(fenetre, text='exp', width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=lambda b='exp': evenement(b)).grid(row=ligne, column=colonne, columnspan=1)
    elif touches == 'ln':
        #Ajouter le bouton logarithme naturel avec le texte 'ln'
        tk.Button(fenetre, text='ln', width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=lambda b='ln': evenement(b)).grid(row=ligne, column=colonne, columnspan=1)
    else:
        tk.Button(fenetre, text=touches, width=largeurBouton, height=hauteurBouton, font=('Helvetica', 14),
                  command=lambda b=touches: evenement(b)).grid(row=ligne, column=colonne, columnspan=1)

    colonne += 1
    if colonne > 3:
        colonne = 0
        ligne += 1

# Démarre la boucle principale de l'application
fenetre.mainloop()




