temp = int(input("Entrez la température : "))
if temp < 0:
    print = "gel"
elif temp < 15:
    print ("froid")
elif temp < 25:
    print = ("doux")
else:
    print = ("chaud")


annee = int(input("Entrez les années: "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("bissextile")
else:
    print("non bissextile")