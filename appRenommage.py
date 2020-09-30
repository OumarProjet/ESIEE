#!/usr/bin/python3

import os
import re
import tkinter
from tkinter import IntVar

def Incrementation():
    a = 10
    while type(a) != type(v.get()):
        print("Entrer un nombre !")
    return v.get()

def garderTexteOriginal():
    while garder_text not in ['oui', 'non']:
        if garder_text == 'oui':
            return True
        elif garder_text=='non':
            return False

def ajoutTexte():

    while ajouter_texte not in ['oui', 'non']:
        if ajouter_texte == 'oui':
            return True
        elif ajouter_texte == 'non':
            return False



def renommage():
    dossierInitiale = os.getcwd()
    os.chdir('./renommage')

    Increment = Incrementation()

    for rep, souRep, files in os.walk('.'):
        for fileName in files:
            Ex = "\.\w+$"
            match = re.search(Ex, fileName)
            extension = match.group()
            positions_ex = match.span()
            debut, fin = positions_ex
            fileNamePre = fileName[:debut]
            newName = "%03d" % Increment
            if garderTexteOriginal():
                newName = newName + ' - ' + fileNamePre[Conservation:]
            elif ajoutTexte():
                newName = newName + ' - ' + str(texte)
            newName += extension
            os.rename(fileName, newName)
            Increment+=1
        break
    os.chdir(dossierInitiale)
    #print("Voici le nouveau de l'image :" + newName + "\n")
    os.chdir(dossierInitiale)

app = tkinter.Tk()
app.title("Renommage")
# mainapp.minsize(640, 480)
# mainapp.maxsize(1280,720)
# mainapp.resizable(width=False, height=False)
# mainapp.sizefrom("user")
# mainapp.geometry("800x600")
screen_x = int(app.winfo_screenwidth())
screen_y = int(app.winfo_screenheight())
window_x = 800
window_y = 600
posX = (screen_x // 2) - (window_x // 2)
posY = (screen_y // 2) - (window_y // 2)
app.geometry('%dx%d+%d+%d' % (window_x, window_y, posX, posY))

label_welcome = tkinter.Label(app, text="Bienvenue à nous allons renommer vos fichiers !")
label_welcome.pack()
text_Incr = tkinter.Label(app, text="De combien voulez-vous incrémenter ?")
text_Incr.pack()
v = IntVar()
entry_Incrementation = tkinter.Entry(app, width=45, exportselection=0, textvariable=v)
entry_Incrementation.pack()
affiche_garder_texte = tkinter.Label(app, text='Voulez-vous garder du texte ? \n')
affiche_garder_texte.pack()
garder_text = tkinter.Entry(app, width=45, exportselection=0)
garder_text.pack()
text_conservation = tkinter.Label(app, text="Combien de caractère voulez-vous garder ?\n")
text_conservation.pack()
Conservation = tkinter.Entry(app, width=45, exportselection=0)
Conservation.pack()
affiche_ajouter_texte = tkinter.Label(app, text='Voulez-vous ajouter le texte? \n')
affiche_ajouter_texte.pack()
ajouter_texte = tkinter.Entry(app, width=45, exportselection=0)
ajouter_texte.pack()
saisie_texte = tkinter.Label(app, text='Quelle est le texte voulu ? \n')
saisie_texte.pack()
texte= tkinter.Entry(app, width=45, exportselection=0)
texte.pack()

valider = tkinter.Button(app, width= 45, height=4, command=renommage)
valider.pack()
app.mainloop()

