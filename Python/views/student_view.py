# views/student_view.py

class StudentConsoleView:
    """Maneja toda la interacción por consola con el usuario."""

    @staticmethod
    def show_message(message: str):
        print(message)

    @staticmethod
    def show_range_results(min_id: int, max_id: int, students: list):
        print("\n--- Reporte de Estudiantes ---")
        print(f"Buscando IDs entre {min_id} y {max_id}...")

        if not students:
            print("No se encontraron estudiantes en ese rango.")
        else:
            print(f"Estudiantes encontrados: {students}")
            print(f"Total encontrados: {len(students)}")
        print("------------------------------\n")