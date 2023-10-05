# Opdracht 1 lists
# Naam student:
# Groep:
# Maak een lijst om de dictionaries op te slaan
lijst = []

# Maak de eerste persoonsdictionary
persoon1 = { "id": 1, "voornaam": "Henk", "achternaam": "Boer" }
lijst.append(persoon1)

# Maak de tweede persoonsdictionary
persoon2 = { "id": 2, "voornaam": "John", "achternaam": "Doe" }
lijst.append(persoon2)

# Maak de derde persoonsdictionary
persoon3 = { "id": 3, "voornaam": "Sieb", "achternaam": "Laan" }
lijst.append(persoon3)

# Maak de vierde persoonsdictionary
persoon4 = { "id": 4, "voornaam": "Rik", "achternaam": "Wit" }
lijst.append(persoon4)

# Print de volledige naam van de tweede persoon
print(lijst[2]["voornaam"], lijst[2]["achternaam"])
