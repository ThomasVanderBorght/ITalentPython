# oefening voor faculteit van een getal
getal = int(input("Voer een positief geheel getal in: "))
factorial = 1
for i in range(1, getal + 1):
    factorial *= i
print("De faculteit van ", getal, "is: ", factorial)