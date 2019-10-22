#Caesar cipher

plaintext = input ("enter text you want to cipher: ")
key = input ("enter cipher key: ")

while key.isdigit()== False or (int(key) <= 0):
    print ("Incorrect, enter only number > 0, please!")
    key = input ("enter cipher key: ")


ciphertext = ""
for i in range(len(plaintext)):
    letter = plaintext[i]
    if letter == " ":
        ciphertext += " "
    elif letter == letter.lower():
        ciphertext += chr((ord(letter) + int(key) - 97) % 26 + 97)
    else:
        ciphertext += chr((ord(letter) + int(key) - 65) % 26 + 65)

# funguje jen pro znaky abecedy a mezeru, ne pro ostatní znaky

print ("original text: " + plaintext)
print ("cipher text: " + ciphertext)