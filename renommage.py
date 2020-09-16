#!/usr/bin/python3


import os
import re


def Incrementation():
	a = 10
	saisie = ""
	while type(a) != type(saisie):
		saisie = int(input('Incrémentation de combien ?\n'))
	return saisie



def garderTexteOriginal():
	saisie = input('Voulez vous garder le texte original ?\n')
	while saisie not in ['oui', 'non']:
		saisie = input('Voulez vous garder le texte original ?\n')
		if saisie == 'oui':
			return True
		elif saisie =='non':
			return False



def ajoutTexte():
	saisie ="machin"
	while saisie not in ['oui', 'non']:
		saisie = input('Voulez-vous ajouter le texte? \n')
		if saisie == 'oui':
			return True
		elif saisie =='non':
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
			newName = "%03d" %Increment


			if garderTexteOriginal():
				Conservation  = int(input("Combien de caractère voulez-vous garder ?\n"))
				newName = newName + ' - ' + fileNamePre[Conservation:]
			elif ajoutTexte():
				texte = input("Veuillez saisir le texte voulu : \n")
				newName = newName + ' - ' + texte
			newName += extension
			os.rename(fileName, newName)
			Increment += 1
		break
	os.chdir(dossierInitiale)
	print("Voici le nouveau de l'image :"+newName+"\n")
renommage()