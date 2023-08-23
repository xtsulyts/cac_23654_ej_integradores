"""2 escribir una función que calcule el numero comun multiplo entre dos numeros"""
num1 = int(input("Ingrese el primer número:"))
num2 = int(input("Ingrese el segundo número:"))

max_cm = False

if num1 > 0 and num2 > 0 and num1 != num2:
    comprobar = False
    if num2 > num1:
        cambio_valor = num1
        num1 = num2 
    i=num1 

    while not max_cm and  i >= 1:
        if num1 % 1 ==  0 and num2 % i == 0:

     
