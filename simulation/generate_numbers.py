import math

# LinearCongruentialGenerator: Esta clase implementa un generador de
# números pseudoaleatorios utilizando el algoritmo LCG.


class LinearCongruentialGenerator:
    def __init__(self, seed=1):
        # Coeficientes del LCG (a, c, m) y semilla inicial
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32
        self.seed = seed

    def rand(self):
        # Calcula el siguiente número pseudoaleatorio
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m  # Devuelve un número en el rango [0, 1)


# box_muller(mean, std_dev, lcg): Esta función utiliza el método Box-Muller
# para generar dos números con distribución normal dados una media (mean) y
# una desviación estándar (std_dev), utilizando el generador LCG proporcionado.

# rand(): Genera un nuevo número pseudoaleatorio en el rango [0, 1).


def box_muller(mean, std_dev, lcg):
    # Genera dos números aleatorios uniformemente distribuidos en el rango (0, 1]
    u1 = 1.0 - lcg.rand()
    u2 = 1.0 - lcg.rand()

    # Aplica la transformación Box-Muller
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    z1 = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)

    # Escala y desplaza los números generados para tener la distribución deseada
    return mean + z0 * std_dev, mean + z1 * std_dev
