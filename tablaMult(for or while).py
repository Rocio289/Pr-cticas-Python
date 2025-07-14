

def tablaDeMultiplicar(numero, forma):
    if forma =="for":
        for num in range(1, 11):
            print(f"{num}x{numero}={num*numero}")
            
    elif forma == "while":
        i = 1
        while i <= 10:
            print(f"{i}x{numero}={i*numero}")
            i += 1
            
    else:
        print("No selecciono la forma de ejecucion")
            
seguirMultiplicando = True

while seguirMultiplicando:  
    numero = int(input("Introduce un numero"))
    forma = input("Ingrese la forma")
    tablaDeMultiplicar(numero, forma)
        
    valor = input("Desea seguir con esto? s/n")
    if valor == "n":
        seguirMultiplicando = False
        
        print("Fin del programa")
