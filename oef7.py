getal1 = float(input("Voer het eerste getal in: "))
getal2 = float(input("Voer het tweede getal in: "))
bewerking = input("wil je optellen, aftrekken, vermenigvuldigen, delen of rest berekenen? ")

if bewerking == "optellen":
    resultaat = getal1 + getal2
    print("De som van de twee getallen is:", resultaat)
if bewerking == "aftrekken":
    resultaat = getal1 - getal2
    print("De som van de twee getallen is:", resultaat)
if bewerking == "vermenigvuldigen": 
    resultaat = getal1 * getal2
    print("het quotient van de twee getallen is:", resultaat)
if bewerking == "delen":
    resultaat = getal1 / getal2
    print("het quotient van de twee getallen is:", resultaat)
if bewerking == "rest":
    resultaat = getal1 % getal2
    print("het restant van de twee getallen is:", resultaat)

elif bewerking != "optellen" and bewerking != "aftrekken" and bewerking != "vermenigvuldigen" and bewerking != "delen" and bewerking != "rest":
    print("Ongeldige invoer")