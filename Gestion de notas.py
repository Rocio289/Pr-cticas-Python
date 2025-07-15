def show_menu():
    print("-Gestión de Notas-")
    print("1. Agregar estudiante")
    print("2. Quitar estudiante")
    print("3. Mostrar estudiantes aprobados")
    print("4. Buscar estudiante por nombre")
    print("5. Mostrar todos los estudiantes")
    print("6. Salir")

def add_student(students):
    name = input("Ingrese el nombre del estudiante: ")
    if name in students:
        print("El estudiante ya está registrado.")
        
    marks = []
    for qualification in range(1, 4):
        while True:
            mark = float(input(f"Ingrese la nota {qualification} (0-10): "))
            if 0 <= mark <= 10:                               
                marks.append(mark)
                break
            else:
                print("Número no válido, vuelva a ingresar nota")
                
    students[name] = marks
    print(f"Estudiante {name} agregado.")

def remove_student(students):
    name = input("Ingrese el nombre del estudiante a eliminar: ")
    if name in students:
        del students[name]
        print(f"Estudiante {name} eliminado.")
    else:
        print("Estudiante no encontrado.")

def show_approved(students):
    print("-Estudiantes Aprobados-")
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        if average >= 6:
            print(f"{name}: Promedio = {average:.2f}")

def search_student(students):
    name = input("Ingrese el nombre del estudiante que busca: ")
    if name in students:
        marks = students[name]
        average = sum(marks) / len(marks)
        print(f"{name}: Notas = {marks}, Promedio = {average:.2f}")
    else:
        print("Estudiante no encontrado.")

def show_all_students(students):
    print("-Todos los Estudiantes-")
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        print(f"{name}: Notas = {marks}, Promedio = {average:.2f}")

def main():
    students = {}

    while True:
        show_menu()
        option = input("Seleccione una opción: ")

        if option == '1':
            add_student(students)
        elif option == '2':
            remove_student(students)
        elif option == '3':
            show_approved(students)
        elif option == '4':
            search_student(students)
        elif option == '5':
            show_all_students(students)
        elif option == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
