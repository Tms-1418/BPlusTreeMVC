from models.bplus_tree import BPlusTree
from views.student_view import StudentConsoleView


class StudentController:
    def __init__(self, degree=3):
        self.tree_model = BPlusTree(degree)
        self.view = StudentConsoleView()

    def register_student(self, student_id):
        self.tree_model.insert(student_id)
        self.view.show_message(
            f"Estudiante con ID {student_id} registrado correctamente."
        )

    def generate_range_report(self, min_id, max_id):
        results = self.tree_model.search_range(min_id, max_id)
        self.view.show_range_results(min_id, max_id, results)