numero1 = 0
numero1 = 0
operacion = ""
continuar = True
seguir = ""

#funcion que realice las operaciones aritmeticas segun opcion
def operaciones_matematicas(n1, n2, op):
    n1 = float(n1)
    n2 = float(n2)
    
    if op == "+":
        print(f"La suma es: {n1+n2}")
    elif op =="-":
        print(f"La resta es: {n1-n2}")
    elif op =="*":
        print(f"La multiplicacion es: {n1*n2}")
    elif op =="/":
        print(f"La division es: {n1/n2}")
    else:
        print("El operador no es valido!!!")


while continuar:
    
    #entrada
    numero1 = input("ingrese valor 1: ")
    numero2 = input("ingrese valor 2: ")
    operacion = input("ingrese la operacion: +, -, *, /")
    
        
    while numero1.isnumeric() == False or numero2.isnumeric()==False or operacion not in "+-*/":
        numero1 = input("ingrese valor 1")
        numero2 = input("ingrese valor 2")
        operacion = input("ingrese la operacion:+, -, *, /")
        
    #transformacion de cadena en numeros
    operaciones_matematicas(numero1, numero2, operacion)

    seguir = input("Desea continuar s/n")
    if seguir == "n":
        continuar = False
        
        print("Fin del programa")