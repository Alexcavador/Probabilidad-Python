# Alejandro Alonso Sanchez
# Probabilidad condicional
# Probabilidad de tener 2 hijas, entre 2 bebés dado un dato:
# a) Que la mayor es una chica
# b) Que una de las 2 es una chica
import enum, random
class Hijo(enum.Enum):
    Hombre = 0
    Mujer = 1
def random_Hijo() -> Hijo:
    return random.choice([Hijo.Hombre, Hijo.Mujer])
ambas_mujer = 0
chica_mayor = 0
cualquiera_chica = 0

for _ in range(10000):
    menor = random_Hijo()
    mayor = random_Hijo()
    if mayor == Hijo.Mujer:
        chica_mayor += 1
    if mayor == Hijo.Mujer and menor == Hijo.Mujer:
        ambas_mujer += 1
    if mayor == Hijo.Mujer or menor == Hijo.Mujer:
        cualquiera_chica += 1
print("P(ambas | mayor):", ambas_mujer / chica_mayor)
print("P(ambas | cualquiera):", ambas_mujer / cualquiera_chica)