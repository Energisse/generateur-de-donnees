class Formule:
    
    def __init__(self,nom = ""):
        self.nom = nom
        self.lite_monoperiode = []

    def calcul(self,x):
        y = 0
        for formule_monoperiode in self.lite_monoperiode:
            y += formule_monoperiode.calcul(x)
        return y

    def ajouter_monoperiode (self,formule_monoperiode):
        self.lite_monoperiode.append(formule_monoperiode)
