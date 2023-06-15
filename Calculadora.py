
def suma(num_1:int,num_2:int):
    return num_1+num_2
def resta(num_1:int,num_2:int):
    return num_1-num_2
def multiplicacion(num_1:int,num_2:int):
    return num_1*num_2
def division(num_1:int,num_2:int):
    return num_1/num_2


inicio=True

while inicio:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Seleccione la opción deseada: "))

    if opcion ==1:
        print("Ha seleccionado la opcion Sumar")
        num_1=int(input("Seleccione primer numero a sumar: "))
        num_2=int(input("Seleccione segundo numero a sumar: "))
        print("El resultado de la suma es: ", suma(num_1,num_2))

    if opcion ==2:
        print("Ha seleccionado la opcion Resta")
        print("Ha seleccionado la opcion Resta")
        num_1=int(input("Seleccione primer numero a restar: "))
        num_2=int(input("Seleccione segundo numero a restar: "))
        print("El resultado de la resta es: ", resta(num_1,num_2))



    if opcion ==3:
        print("Ha seleccionado la opcion Multiplica")
        num_1=int(input("Seleccione primer numero a multiplicar: "))
        num_2=int(input("Seleccione segundo numero a multiplicar: "))
        print("El resultado de la resta es: ", multiplicacion(num_1,num_2))


    if opcion ==4:
        print("Ha seleccionado la opcion Dividir")
        num_1=int(input("Seleccione primer numero a dividir: "))
        num_2=int(input("Seleccione segundo numero a dividir: "))
        print("El resultado de la resta es: ", division(num_1,num_2))


    if opcion ==5:
        print("Ha seleccionado Salir")
inicio=False



