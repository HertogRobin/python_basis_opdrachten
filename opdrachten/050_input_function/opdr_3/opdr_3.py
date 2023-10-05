# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
# Vraag de gebruiker om een lijst van objecten in te voeren, gescheiden door komma's
input_string = input("Vul steden in, gescheiden door komma's: ")

# Split de invoerstring in een lijst van objecten
objecten = input_string.split(',')

# Verwijder eventuele extra spaties aan het begin en einde van elk object
objecten = [object.strip() for object in objecten]

# Sorteer de lijst in omgekeerde volgorde, waarbij woorden die met 'Z' beginnen vooraan staan
objecten.sort(key=lambda x: x[::-1])

# Druk de gesorteerde lijst af
print(objecten)

