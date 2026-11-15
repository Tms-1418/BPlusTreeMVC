package com.bplstree.model;

import com.bplstree.model.LeafNode;
import com.bplstree.model.Node;

public class LeafNode extends Node {
	
	protected LeafNode next;
	
	public LeafNode(int degree) {
		super(degree);
		this.next = null;
	}
}
