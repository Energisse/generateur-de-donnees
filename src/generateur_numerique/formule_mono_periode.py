import math
from select import select

class FormuleMonoPeriode:
    
    def __init__(self,periode = 1,amplitude = 1):
        self.periode = periode
        self.amplitude = amplitude

    def calcul(self,x):
        if(self.periode == 0):
           return self.amplitude
           
        return math.sin(math.pi*2*(x/self.periode))*self.amplitude