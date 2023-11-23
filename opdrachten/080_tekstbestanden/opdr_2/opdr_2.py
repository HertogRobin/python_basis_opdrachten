# Opdracht 2 tekstbestanden
# Naam student:
# Groep:
import random

def raad_het_getal():
    prompt = "Raad mijn geheime getal \n"
    geheim_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print(prompt)

    while True:
        poging = int(input())
        aantal_pogingen += 1

        if poging < geheim_getal:
            print("hoger")
        elif poging > geheim_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden, het is {geheim_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer geraden.")
            break

if __name__ == "__main__":
    raad_het_getal()
