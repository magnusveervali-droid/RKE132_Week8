import random


def calculate_hit(name, weapon):
    baas = len(name)
    Boonus = random.randint(0, len(weapon))

    return baas + Boonus