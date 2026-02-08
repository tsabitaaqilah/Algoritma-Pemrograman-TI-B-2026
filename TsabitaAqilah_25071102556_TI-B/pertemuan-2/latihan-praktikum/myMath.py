def penambahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b == 0:
        print("error")
    elif b != 0:
        return a / b

def modulus(a, b):
    return a % b

def fibonacci(n):
    if n <= 1:
        return n