def mostrar_menu():
    print("\n-Gestión de Notas-")
    print("1. Agregar estudiante")
    print("2. Quitar estudiante")
    print("3. Mostrar estudiantes aprobados")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar todos los estudiantes")
    print("6. Salir")

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in estudiantes:
        print("El estudiante ya está registrado.")
        return
    notas = []
    for calificacion in range(1, 4):
        while True:
            nota = float(input(f"Ingrese la nota {calificacion} (0-10): "))           
            notas.append(nota)
            break
                
    estudiantes[nombre] = notas
    print(f"Estudiante {nombre} agregado.")

def quitar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado.")
    else:
        print("Estudiante no encontrado.")

def mostrar_aprobados(estudiantes):
    print("\n-Estudiantes Aprobados-")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        if promedio >= 6:
            print(f"{nombre}: Promedio = {promedio:.2f}")

def buscar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante que busca: ")
    if nombre in estudiantes:
        notas = estudiantes[nombre]
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: Notas = {notas}, Promedio = {promedio:.2f}")
    else:
        print("Estudiante no encontrado.")

def mostrar_todos(estudiantes):
    print("\n-Todos los Estudiantes-")
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: Notas = {notas}, Promedio = {promedio:.2f}")

def main():
    estudiantes = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_estudiante(estudiantes)
        elif opcion == '2':
            quitar_estudiante(estudiantes)
        elif opcion == '3':
            mostrar_aprobados(estudiantes)
        elif opcion == '4':
            buscar_estudiante(estudiantes)
        elif opcion == '5':
            mostrar_todos(estudiantes)
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()