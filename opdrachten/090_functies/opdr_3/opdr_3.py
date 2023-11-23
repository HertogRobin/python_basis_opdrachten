# Opdracht 1 functies
# Naam student:
# Groep:


import math

def kubus_vol(m):
    volume = m ** 3
    return volume

def bol_vol(r):
    volume = (4 / 3) * math.pi * r**3
    return volume

if __name__ == "__main__":
    zijde = 5
    radius = 4

    print(kubus_vol(zijde))
    print(bol_vol(radius))

