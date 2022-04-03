from datetime import datetime, timedelta
import os
import pandas as pd
import numpy as np

class Controleur:
    def __init__(self,taille = 10,intervalle = 1):
        self.liste_formule = []
        self.intervalle = intervalle
        self.taille = taille
        self.data_frame = None
    
    def ajouter_formule(self,formule):
        self.liste_formule.append(formule)

    def calcul(self):
        liste_mesure = []
        liste_date = []
        liste_nom_formule = []

        for formule in self.liste_formule:
            liste_nom_formule.append(formule.nom)

        date = datetime.now()
        for x in range(self.taille):
            liste_mesure_ligne = []

            for formule in self.liste_formule:
                liste_mesure_ligne.append(formule.calcul(x*self.intervalle))

            date +=  timedelta(seconds=self.intervalle)

            liste_date.append(date.strftime("%H:%M:%S %Y/%m/%d"))
            liste_mesure.append(liste_mesure_ligne)
            
        self.data_frame = pd.DataFrame(liste_mesure, index = liste_date,columns=liste_nom_formule)
        
    def afficher(self):
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.data_frame)
        
    def enregistrer_en_csv(self,nom_fichier):
        if os.path.exists(nom_fichier):
             os.remove(nom_fichier)
       
        self.data_frame.to_csv(nom_fichier)
