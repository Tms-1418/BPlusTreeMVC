# controllers/student_controller.py
from models.bplus_tree import BPlusTree
from views.student_view import StudentConsoleView


class StudentController:
    """Actúa como puente entre el BPlusTree y la interfaz de usuario."""

    def __init__(self, degree: int = 3):
        self.tree_model = BPlusTree(degree)
        self.view = StudentConsoleView()
        # Guardamos la referencia a la primera hoja para simular el inicio
        # de nuestra cadena de hojas en esta demostración simplificada.
        self.first_leaf = self.tree_model.root

    def register_student(self, student_id: int):
        """Pide al modelo insertar y a la vista mostrar confirmación."""
        self.tree_model.insert(student_id)
        self.view.show_message(f"Estudiante con ID {student_id} registrado en el sistema.")

    def generate_range_report(self, min_id: int, max_id: int):
        """Coordina la búsqueda en rango y manda los resultados a la vista."""
        # Solicitamos la búsqueda pasando nuestra primera hoja como inicio
        results = self.tree_model.search_range(min_id, max_id, self.first_leaf)
        self.view.show_range_results(min_id, max_id, results)