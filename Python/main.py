# main.py
from controllers.student_controller import StudentController


def main():
    print("=== SISTEMA DE REGISTRO ESTUDIANTIL (Árbol B+) ===\n")

    # 1. Instanciamos el controlador (que a su vez crea el modelo y la vista)
    # Usamos grado m=3 para que haga divisiones (splits) rápidamente en el ejemplo.
    controller = StudentController(degree=3)

    # 2. Registramos varios IDs (puedes cambiarlos en el video para mostrar que funciona)
    ids_to_insert = [10, 15, 20, 25, 30, 45, 50]

    for student_id in ids_to_insert:
        controller.register_student(student_id)

    # 3. Probamos el requerimiento clave: la consulta por rangos.
    # El B+ es eficiente aquí porque lee la lista enlazada de las hojas.
    controller.generate_range_report(15, 45)


if __name__ == "__main__":
    main()