# Opdracht 2 lists
# Naam student:
# Groep:
rivier_info = { 
    "rijn": ["nederland", "duitsland", "Frankrijk"], 
    "maas": ["nederland", "belgië", "duitsland"], 
    "nijl": ["egypte", "soedan", "oeganda"] 
}

rivieren = list(rivier_info.keys())

# Afdrukken van de naam van de 1e rivier en het 2e land waar de 1e rivier doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info['rijn'][1].capitalize()}")

# Afdrukken van de naam van de 2e rivier en het 1e land waar de 2e rivier doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info['maas'][0].capitalize()}")

# Afdrukken van de naam van de 3e rivier en het 3e land waar de 3e rivier doorheen stroomt
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info['nijl'][2].capitalize()}")
