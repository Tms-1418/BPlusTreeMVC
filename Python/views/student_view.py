class StudentConsoleView:
    def show_message(self, message):
        print(message)

    def show_range_results(self, min_id, max_id, student_ids):
        print("\n --- REPORTE DE ESTUDIANTES ---")
        print(f"Buscando IDs entre {min_id} y {max_id}...")

        if not student_ids:
            print("No se encontraron estudiantes en ese rango.")
        else:
            print(f"Estudiantes encontrados: {student_ids}")
            print(f"Total encontrados: {len(student_ids)}")

        print("------------------------------\n")