ukol lekce 5
pet_names = {"Aki": "dog", "Monty": "pigeon", "Franta": "pig", "Jitka": "rabbit", "Bob": "spider"}

# Modify one of the values in your dictionary. You could clarify to name a breed, or you could change an animal from a cat to a dog.
pet_names["Bob"] = "insect"

for key, value in pet_names.items():
    print("{} is a {}.".format(key, value))

# Add a new key-value pair to your dictionary.
pet_names["Jurášek"] = "horse"

for key, value in pet_names.items():
    print("{} is a {}.".format(key, value))

# Remove one of the key-value pairs from your dictionary.
del pet_names["Franta"]

for key, value in pet_names.items():
    print("{} is a {}.".format(key, value))