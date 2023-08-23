"""1 escribir una función  que calcule el maximo divisor entre dos numeros"""
comprobar = True
while comprobar:

    num1= int(input("Ingrese el primer número:"))
    num2= int(input("Ingrese el segundo número:"))

    max_cd = False

    if num1 > 0 and num2 > 0 and num1 != num2:
        comprobar = False
        if num2 < num1:
            cambio_valor = num1
            num1 = num2
            num2 = cambio_valor
        i=num1    

        while not max_cd and i >= 1:
         if num1 % 1 == 0 and num2 % i == 0:
            print("El maximo comun divisor es", i)
            max_cd = True
        else:
                i -= 1 
            
    else:
        if num1 == num2:
                print("Los números son iguales. Inténtelo nuevamente")
        else:    
                print("Incorrecto, igrese nuevamente los números")  

    













#6. crea una clase llamada persona. Sus atributos son: nombre, edad, dni. Construya los siguientes metodos para la clase#
#A. Un constructos donde los datos puedan estar vacíos#
#B. los setters y los getters para cada uno de los atributos. Hay qie validar las entradas de datos#
#C. mostrar(): Muestra los datos de la persona#
#D. Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad#

#7 crear una clase llamada Persona. Sus atributos son: nombre, edad y dni. Construya los siguites métodos para la clasee:
#A. Un constructor, donde los datos puedan estar vacíos#
#B. Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo  ingresando o retirando dinerol#
#C. mostrar(): Muestra los datos de la cuenta#
#D. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos#

#8. Vamos a definir ahora una "Cuenta joven", poara ello vamos a crear una nueva clase CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, ademas del titular y la cantiadad se debe guardar una bonificación que estara expresada en tanto por ciento. Crear los siguientes métodos para la clase:#
#A. Um constructor#
#B. Los setters y getters para el nuevo atributo#
#C. En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en el caso contrario#
#D. Además, la retirada de dinero sólo se prodra hacer si el titular es válido#
#E. El método mostrar() deve devolver el mensaje de "Cuenta Joven" y la bonificación de la cuenta

