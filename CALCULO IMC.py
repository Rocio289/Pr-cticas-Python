#crear un programa que mida el IMC(Indice de masa Corporal)
#la formula es imc = peso / (altura*altura)
#si imc es menor a 18.5 se asigna bajo peso
#si imc esta entre 18.5 y 24.9 peso normal
#si imc esta entre 25 y 29.9 sobrepeso
#en cualquier otro caso IMC es mayor o igual a 30 obesidad

def logicaIMC(peso, altura):
    imc = peso / altura**2
    
    if imc < 18.5:
        print(f"Su imc es {imc: 2f}, indica que está en 'BAJO PESO' ")
    elif (imc >= 18.5 and imc <= 24.9):
        print(f"Su imc es {imc: 2f}, indica que está en 'PESO NORMAL' ")
    elif (imc >= 24.9 and imc <= 29.9):
        peso_ideal = peso - pesoIdeal(altura)
        print(f"Su imc es {imc: 2f}, indica que está en 'SOBREPESO', debes bajar {peso_ideal} para estar en 'PESO NORMAL' ")
    else:
        peso_ideal = peso - pesoIdeal(altura)
        print(f"Su imc es {imc: 2f}, indica que está en 'OBESIDAD', debes bajar {peso_ideal} para estar en 'PESO NORMAL' ")
        
def pesoIdeal(altura):
    peso = (altura*altura)*24.9
    return peso

        
peso = 0.0
altura = 0.0
imc = 0.0
continuar = True

while continuar:    
    print("Quieres saber si estas en peso correcto")
    peso = float(input("Ingrese su peso en kg"))
    altura = float(input("Ingrese su altura en metros"))
    logicaIMC(peso, altura)

    fin = input("Desea continuar con el programa? s/n")
    if fin == 'n':
        continuar = False
        
else:
    print("Fin del programa")
    

