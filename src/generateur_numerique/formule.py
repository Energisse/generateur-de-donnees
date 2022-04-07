class Formule:
    
    def __init__(self,nom = ""):
        self.nom = nom
        self.liste_composante = []

    def calcul(self,x):
        y = 0
        for formule_composante in self.liste_composante:
            y += formule_composante.calcul(x)
        return y

    def ajouter_composante_formule (self,formule_composante):
        self.liste_composante.append(formule_composante)
