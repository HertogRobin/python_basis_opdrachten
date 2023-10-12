# Opdracht 3 condities
# Naam student:
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd_invoer = int(input("Geef uw leeftijd in aantal jaar: "))

# Bepaal de leeftijdsgroep
leeftijdsgroep = None
for groep, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_invoer <= max_leeftijd:
        leeftijdsgroep = groep
        break

if leeftijdsgroep is not None:
    korting = kortings_percentages[leeftijdsgroep]
    korting_bedrag = (korting / 100) * normale_toegangsprijs
    te_betalen = normale_toegangsprijs - korting_bedrag

    print(f"U behoort tot de groep {leeftijdsgroep}")
    print(f"U krijgt {korting}% korting")
    print(f"U betaalt daarom {te_betalen:.2f}")
else:
    print("Leeftijdsgroep niet gevonden")


# Hier komt je code...
