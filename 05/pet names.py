# Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.(at least 3 pairs)
# Use a for loop to print out a series of statements such as "Willie is a dog."

pet_names = {"Aki": "dog", "Monty": "pigeon", "Franta": "pig", "Jitka": "rabbit", "Bob": "spider"}

for key, value in pet_names.items():
    print("{} is a {}.".format(key, value))


