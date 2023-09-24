import figureDrawer as fd
from random import randint as rand

def chooseFigure():
    return rand(1,7)

def defineFigureType(case):
    if case == 1:
        return "Z"
    if case == 2:
        return "S"
    if case == 3:
        return "T"
    if case == 4:
        return "L"
    if case == 5:
        return "J"
    if case == 6:
        return "I"
    if case == 7:
        return "O"

   

