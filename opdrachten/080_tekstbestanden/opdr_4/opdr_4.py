# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
def vragenlijst_invullen():
    vragen = [
        "Wat is je voornaam?",
        "Wat is je achternaam?",
        "Wat neem je mee aan drank?",
        "Wat neem je mee om te eten?"
    ]

    antwoorden = {}

    for i, vraag in enumerate(vragen, 1):
        antwoord = input(f"{i}. {vraag}\n")
        antwoorden[vraag.split()[-1][:-1].lower()] = antwoord

    with open("feestgangers.txt", "a") as file:
        file.write("----\n")
        for key, value in antwoorden.items():
            file.write(f"{key}: {value}\n")

if __name__ == "__main__":
    vragenlijst_invullen()
    print("Bedankt voor het invullen!\nSee you at the party.")
