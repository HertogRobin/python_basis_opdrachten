# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Initialiseer een lege lijst om de resultaten op te slaan
resultaten = []

# Maak een for-loop om de gewenste berekeningen uit te voeren
for num in range(3, 82, 3):
    kwadraat = num ** 2
    gedeeld_door_3 = kwadraat / 3
    resultaten.append(gedeeld_door_3)

# Druk de lijst met resultaten af
print(resultaten)
