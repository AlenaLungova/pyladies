rodne_cislo = input("Rodne cislo: ")

jedenacti = rodne_cislo[:6] + rodne_cislo[7:]

if len(rodne_cislo) == 11 and rodne_cislo[:6].isdigit() and rodne_cislo[6] == "/" and rodne_cislo[7:].isdigit() and int(jedenacti) % 11 == 0:
    print("Číslo zadáno správně.")
else:
    print("Někde je chyba.")