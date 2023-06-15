
#Sin argumento y sin retorno
def saludo():
    print("Saludando a mis estudiantes")
for n in range(10):
    saludo()

#sin argumento y con retorno
def suma1():
    num_1=10
    num_2=5
    resultado=num_1+num_2
    return resultado
resultado_suma=suma1()
print("Forma A de utilizar la funcion retorno:", resultado_suma)
print("Forma B de utilizar la funcion retorno:", suma1())
print("Forma C de utilizar la funcion retorno:", suma1()+suma1())

#funcion con argumentos y sin retorno
def resta1(num_1,num_2):
    resultado = num_1-num_2
    print("El resultado de la resta es: ", resultado)
resta1(10,1)


def resta2(num_1,num_2):
    resultado = num_1-num_2
    return resultado
resultado_1=resta2(10,1)
resultado_2=resta2(8,3)
print(resultado_1-resultado_2)

     