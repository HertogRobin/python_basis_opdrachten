# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizza_landen = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizza_landen.sort()

# Voeg een pizza naar eigen smaak toe
pizza_landen.append('yo-favorito')

# Verwijder de minst favoriete pizza
pizza_landen.remove('olivio')

# Print de eerste 3 pizza's
print(pizza_landen[:3])

# Print alleen de middelste pizza
print([pizza_landen[len(pizza_landen) // 2]])

# Print de laatste 3 pizza's
print(pizza_landen[-3:])
