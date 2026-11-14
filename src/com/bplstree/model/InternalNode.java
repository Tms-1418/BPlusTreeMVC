package com.bplstree.model;

import java.util.ArrayList;
import java.util.List;

public class InternalNode extends Node {
	
	protected List<Node> children;
	
	public InternalNode(int degree) {
		super(degree);
		this.children = new ArrayList<>();
	}
}
