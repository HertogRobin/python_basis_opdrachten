# Opdracht 1 functies
# Naam student:
# Groep:


def volledige_naam(lijst_met_namen):
    for naam in lijst_met_namen:
        # Voeg de delen van de naam samen met spaties en verwijder overbodige spaties
        volledige_naam = " ".join([deel for deel in [naam["voornaam"], naam["tussenvoegsel"], naam["achternaam"]] if deel])
        print(volledige_naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
