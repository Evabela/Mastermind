"""DOCSTRING
La fonction init intialise le tableau de couleur réponse avec des couleurs aléatoires
---------------------
ARGUMENT:
---------------------
SORTIE:
list(initial)
---------------------"""

from random import *

def init():
    initial = [randrange(1,9) for i in range(4)] 
    return initial

if __name__ == "__main__":
    print(init())