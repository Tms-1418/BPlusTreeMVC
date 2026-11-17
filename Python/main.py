from controllers.student_controller import StudentController


def main():
    print("=== SISTEMA DE REGISTRO ESTUDIANTIL ===\n")

    controller = StudentController(degree=3)

    ids_to_insert = [10, 15, 20, 25, 30, 45, 50]

    for student_id in ids_to_insert:
        controller.register_student(student_id)

    controller.generate_range_report(15, 45)


if __name__ == "__main__":
    main()