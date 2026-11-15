
package com.bplstree.controller;

import com.bplstree.model.BPlusTree;
import com.bplstree.view.StudentConsoleView;

import java.util.List;


public class StudentController {

    private BPlusTree treeModel;
    private StudentConsoleView view;

    public StudentController(
            BPlusTree model, StudentConsoleView view) {

        this.treeModel = model;
        this.view = view;
    }


    public void registerStudent(int studentId) {

        treeModel.insert(studentId);

        view.showMessage(
            "Estudiante con ID " + studentId +
            " registrado correctamente."
        );
    }


    public void generateRangeReport(int minId, int maxId) {

        List<Integer> results =
            treeModel.searchRange(minId, maxId);

        view.showRangeResults(minId, maxId, results);
    }


    public static void main(String[] args) {

        BPlusTree model = new BPlusTree(3);

        StudentConsoleView view = new StudentConsoleView();

        StudentController controller =
            new StudentController(model, view);

        System.out.println(
            "=== SISTEMA DE REGISTRO ESTUDIANTIL ===\n"
        );


        controller.registerStudent(10);
        controller.registerStudent(15);
        controller.registerStudent(20);
        controller.registerStudent(25);
        controller.registerStudent(30);
        controller.registerStudent(45);
        controller.registerStudent(50);


        controller.generateRangeReport(15, 45);
    }
}
