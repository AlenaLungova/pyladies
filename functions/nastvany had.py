zvirata = ["pes", "kočka", "králík", "had", "andulka"]

pismenka = []
for i in zvirata:
    pismenka.append(i[1])

s_klicem = list(zip(pismenka, zvirata))

serazene = sorted(s_klicem)

konecny_seznam = []

for j in serazene:
    konecny_seznam.append(j[1])

print(konecny_seznam)
