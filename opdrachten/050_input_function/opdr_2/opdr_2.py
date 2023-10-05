# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Maak een lijst met de oorspronkelijke gasten
gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

# Print de oorspronkelijke lijst
print(gasten)

# Verwijder Marie uit de lijst
gasten.remove("Marie")

# Print de bijgewerkte lijst zonder Marie
print(gasten)

# Voeg George toe naast Kees
kees_index = gasten.index("Kees")
gasten.insert(kees_index + 1, "George")

# Print de definitieve lijst met George naast Kees
print(gasten)
