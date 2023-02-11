# Alejandro Alonso Sánchez
# Eventos aleatorios. 
import random
from random import choices
print('Programa para obtener probabilidades de eventos aleatorios empíricamente')

n = 1000
def lanzamiento():
    return choices(['Aguila','Sol']).count('Sol')
print('Probabilidad de saliera sol, luego de ' + str(n) + ' lanzamientos: ' + str(sum(lanzamiento() for i in range(n))*100 /n )+'%')