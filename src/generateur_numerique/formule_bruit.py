import random

class FormuleBruit:
    
    def __init__(self,amplitude = 1):
        self.amplitude = amplitude

    def calcul(self,x):
        return self.amplitude*(random.random()-0.5)