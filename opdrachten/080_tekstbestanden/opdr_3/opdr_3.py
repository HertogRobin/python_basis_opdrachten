# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:
def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Controleer of het een letter is
            # Verschuif de letter 5 plaatsen in het alfabet
            code = ord(char) + 5
            # Pas de verschuiving toe voor de letters 'z' en 'Z'
            if char.islower():
                if code > ord('z'):
                    code -= 26
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
            encrypted_text += chr(code)
        else:
            encrypted_text += char  # Behoud leestekens en spaties
    return encrypted_text

def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            # Verschuif de letter 5 plaatsen terug in het alfabet
            code = ord(char) - 5
            # Pas de verschuiving toe voor de letters 'a' en 'A'
            if char.islower():
                if code < ord('a'):
                    code += 26
            elif char.isupper():
                if code < ord('A'):
                    code += 26
            decrypted_text += chr(code)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    # Invoer van de gebruiker
    tekst = input("Geef de tekst die je wilt encrypten/decrypten: ")

    # Encrypteer de tekst
    versleutelde_tekst = encrypt(tekst)
    print(f"Versleutelde tekst: {versleutelde_tekst}")

    # Decrypteer de tekst
    ontsleutelde_tekst = decrypt(versleutelde_tekst)
    print(f"Ontsleutelde tekst: {ontsleutelde_tekst}")



