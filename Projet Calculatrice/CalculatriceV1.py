import tkinter as tk

""" FR : PROJET CODÉ PAR ANTHONY VAUCHEL
    
    PROJET PERSONNEL
    
    Le but de ce projet est de créer une calculatrice à l'aide de Tkinter.
    On l'améliorera au fil du temps, ceci étant la V1.
    
    EN : PROJECT CODED BY ANTHONY VAUCHEL
    
    PERSONAL PROJECT

    The aim of this project is to create a calculator using Tkinter.
    It will be enhanced over time, with this being V1."""

historique_calculs = []

def evenement(valeurBouton):
    """ Permet de calculer l'expression actuelle, de la réinitialiser ou de la créer """
    texte = texteEntree.get()

    if valeurBouton == "=":
        try:
            resultat = eval(texte)
            texteResultat.set(resultat)
            historique_calculs.append((texte, resultat))
        except Exception as e:
            texteResultat.set("Error")

    elif valeurBouton == "C": #Si C est activé, réinitialise texteEntree
        texteEntree.set("")
    else:
        texteEntree.set(texte + valeurBouton) #Sinon ajouter la valeur du bouton activé à la fin de l'expression actuelle

#Crée la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")

#Variable pour stocker l'expression
texteEntree = tk.StringVar()

#Affichage de l'expression puis de son résultat
entreeAffichage = tk.Entry(fenetre, textvariable=texteEntree, font=('Helvetica', 18), justify='right')
entreeAffichage.grid(row=0, column=0, columnspan=4)

#Liste des boutons qu'on veut créer
boutons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

ligne = 1
colonne = 0

#Création des boutons
for touches in boutons: #Pour le nombre de boutons faire :
    #Créer les boutons et les placer
    tk.Button(fenetre, text=touches, padx=20, pady=20, font=('Helvetica', 14), command=lambda b=touches: evenement(b)).grid(row=ligne, column=colonne)
    colonne += 1
    if colonne > 3:
        colonne = 0
        ligne += 1

#Lance la boucle principale de l'application
fenetre.mainloop()

