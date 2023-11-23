# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier
def main():
    # Vraag 1
    antwoord1 = input("Wat vind je van de huidige regering? ")

    # Vraag 2
    antwoord2 = input("Wat vind je van de Python-lessen tot nu toe? ")

    # Vraag 3
    antwoord3 = input("Wat vind jij de mooiste stad van Nederland? ")

    # Sla de resultaten op in een tekstbestand
    with open("enquete_resultaten.txt", "a") as file:
        file.write(f"Antwoord op vraag 1: {antwoord1}\n")
        file.write(f"Antwoord op vraag 2: {antwoord2}\n")
        file.write(f"Antwoord op vraag 3: {antwoord3}\n")

    print("Bedankt voor het invullen van de enquête! De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")

if __name__ == "__main__":
    main()
