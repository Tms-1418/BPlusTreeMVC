package com.bplstree.model;

import java.util.ArrayList;
import java.util.List;

public abstract class Node {
	
	protected List<Integer> keys;
	protected int degree;
	
	public Node(int degree) {
		this.keys = new ArrayList<>();
		this.degree = degree;
	}
	
	public boolean isOverflow() {
		return keys.size() >= degree;
	}
}
