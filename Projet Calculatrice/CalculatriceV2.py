import tkinter as tk

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL
    
    PROJET PERSONNEL
    
    Le but de ce projet est d'améliorer au fur et à mesure la calculatrice créée précédemment.
    Dans cette V2, on aura ajouté :
    - L'affichage en temps réel du résultat
    - Une option qui permet de changer le thème de l'application (la couleur des boutons et du fond
    - Une option qui permet de créer un historique des calculs et de leur résultat et de les afficher
    
    EN : PROJECT CODED BY ANTHONY VAUCHEL
    
    PERSONAL PROJECT
    
    The purpose of this project is to progressively enhance the previously created calculator.
    In this V2, the following features will be added:
    - Real-time display of the result
    - An option to change the theme of the application (the color of buttons and the background)
    - An option to create a history of calculations and their results and to display them"""

def evenement(valeurBouton):
    """ Permet de calculer l'expression actuelle, de la réinitialiser ou de la créer """
    texte = texteEntree.get()

    try:
        if valeurBouton == "=":
            resultat = eval(texte)
            texteEntree.set(resultat)
            texteResultat.set("")
            historiqueCalculs.append((texte, resultat))
        else:
            texteEntree.set(texte + valeurBouton)
            texteResultat.set(eval(texte + valeurBouton)) #On calcul pour afficher en temps réel
    except Exception as error:
        texteResultat.set("Error")

    if valeurBouton == "C":
        texteEntree.set("")
        texteResultat.set("")

def changerTheme(nouveau_theme):
    """ Permet de changer la couleur des boutons """
    fenetre.tk_setPalette(background=themes[nouveau_theme])
    
#On définit les différents thèmes    
themes = {
    "1": "white",
    "2": "LightSkyBlue1",
    "3": "darkblue",
    "4": "pink",
    "5": "purple"
}


def afficherHistorique():
    """ Permet d'afficher l'historique des calculs """
    fenetreHistorique = tk.Toplevel(fenetre) #On crée une nouvelle fenêtre
    fenetreHistorique.title("Historique des Calculs")

    texteHistorique = tk.Text(fenetreHistorique, wrap="none", font=('Helvetica', 12), height=20, width=50) #
    texteHistorique.pack()

    for calcul in historiqueCalculs: #Pour le nombre de calcul fait faire 
        texteHistorique.insert(tk.END, f"{calcul[0]} = {calcul[1]}\n") #Ecrire les calculs faits

# Initialisation de l'historique
historiqueCalculs = []

fenetre = tk.Tk() #Crée la fenêtre principale
fenetre.title("Calculatrice")
fenetre.configure(bg= 'white')  #Couleur de fond initiale


texteEntree = tk.StringVar()
texteEntree.set("")

entreeAffichage = tk.Entry(fenetre, textvariable=texteEntree, font=('Helvetica', 18), justify='right') #Crée l'affichage des calculs et du résultat
entreeAffichage.grid(row=0, column=0, columnspan=4)

texteResultat = tk.StringVar()
texteResultat.set("")

labelResultat = tk.Label(fenetre, textvariable=texteResultat, font=('Helvetica', 14), justify='right') #Crée l'affichage du résultat en temps réel
labelResultat.grid(row=1, column=0, columnspan=4) 

boutons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'H'  #Ajout du bouton Historique
]

ligne = 2  
colonne = 0

# Taille fixe pour tous les boutons
largeurBouton = 20
hauteurBouton = 30

for touches in boutons:
    if touches == 'H':
        tk.Button(fenetre, text=touches, padx=largeurBouton, pady=hauteurBouton, font=('Helvetica', 14), command=afficherHistorique).grid(row=ligne, column=colonne, columnspan=1)
    else:
        tk.Button(fenetre, text=touches, padx=largeurBouton, pady=hauteurBouton, font=('Helvetica', 14), command=lambda b=touches: evenement(b)).grid(row=ligne, column=colonne, columnspan=1)

    colonne += 1
    if colonne > 3:
        colonne = 0
        ligne += 1

# Ajouter le bouton de changement de thème en bas à droite
menu_theme = tk.OptionMenu(fenetre, tk.StringVar(), *themes.keys(), command=changerTheme) #On crée le déroulé pour les thèmes
menu_theme.grid(row=ligne, column=3, sticky="se")

fenetre.mainloop()
