"""Napiš tyto funkce. Každá z nich dostane jako argument řetězec s rodným číslem a nějak ho zanalyzuje:

(a) Je ve správném formátu: 6 číslice, lomítko, 4 číslice? (vrací True nebo False)
(b) Je dělitelné jedenácti? (vrací True nebo False)
(c) Jaké datum narození je v čísle zakódováno? (vrací trojici čísel – den, měsíc, rok)
(d) Jaké pohlaví je v čísle zakódováno? (vrací 'muž' nebo 'žena')"""

rodne_cislo = input("Rodne cislo: ")

rok = "19" + str(rodne_cislo[:2])
měsíc = ""
den = rodne_cislo[4:6]
narozeni = int(rodne_cislo[2:4])

def format(rodne_cislo):
    return len(rodne_cislo) == 11 and rodne_cislo[:6].isdigit() and rodne_cislo[6] == "/" and rodne_cislo[7:].isdigit()

def del_11(rodne_cislo):
    jedenacti = rodne_cislo[:6] + rodne_cislo[7:]
    return int(jedenacti) % 11 == 0

def datum_narozeni(rodne_cislo):
    if narozeni > 12:
        měsíc = narozeni - 50
    else:
        měsíc = narozeni   
    return (den, měsíc, rok)

def pohlaví(rodne_cislo):
    if narozeni > 12:
        return ("Žena")
    else:
        return ("Muž")
    

print (format(rodne_cislo))
print (del_11(rodne_cislo))
print (datum_narozeni(rodne_cislo))
print (pohlaví(rodne_cislo))