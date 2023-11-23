# Opdracht 1 functies
# Naam student:
# Groep:
def write_to_file(afile, atext):
    try:
        with open(afile, "a") as file:
            file.write(atext + "\n")
        print(f"Tekst succesvol toegevoegd aan het bestand {afile}")
    except Exception as e:
        print(f"Fout bij schrijven naar bestand: {e}")

def main():
    my_tekst = "Schrijf dit maar even in een bestandje"
    my_file = "test.txt"
    write_to_file(my_file, my_tekst)

if __name__ == "__main__":
    main()
