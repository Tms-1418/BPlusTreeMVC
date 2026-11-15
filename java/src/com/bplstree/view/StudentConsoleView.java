package com.bplstree.view;

import java.util.List;

public class StudentConsoleView {
	
	public void showMessage(String message) {
		System.out.println(message);
	}
	
	public void showRangeResults(int min, int max, List<Integer> studentIds) {
		System.out.println("\n --- REPORTE DE ESTUDIANTES ---");
		System.out.println("Buscando IDs entre " + min + " y " + max + "...");
		
		if(studentIds.isEmpty()) {
			System.out.println("No se encontraron estudiantes en ese rango.");
		}else {
			System.out.println("Estudiantes encontrados: " + studentIds);
			System.out.println("Total encontrados: " + studentIds.size());
		}
		
		System.out.println("------------------------------\n");
		
	}

}
