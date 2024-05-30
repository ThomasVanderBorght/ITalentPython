# lijst van getallen en hiervan gemiddelde berekenen
getallen = input("Voer een lijst van getallen in(gelieve spaties te zetten): ")
getallen_lijst = [float(getal) for getal in getallen.split()]
gemiddelde = sum(getallen_lijst) / len(getallen_lijst)
print("Het gemiddelde van de ingevoerde getallen is:", gemiddelde)