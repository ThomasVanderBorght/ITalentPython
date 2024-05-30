#oefenig voor een fionacci reeks waarbij elk getal de som is van de 2 voorgaande getallen
n = int(input("Voer een positie in de Fibonacci-reeks in: "))

def fibonacci(n):
    if n <= 0:
        return "Ongeldige invoer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b
print("Het", n, "de Fibonacci-getal is:", fibonacci(n))