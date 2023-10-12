# Opdracht 4 condities
# Naam student:
# Groep:

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Genereer een lijst van beschikbare toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een keuze
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Zoek de gekozen topping en toon de prijs
gevonden = False
for topping, prijs in toppings:
    if keuze == topping:
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        gevonden = True
        break

# Als de topping niet gevonden is, toon een foutmelding
if not gevonden:
    print("Uw keuze zit niet in ons assortiment")
