
package com.bplstree.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BPlusTree {

    private Node root;
    private int degree;
    private LeafNode firstLeaf;

    public BPlusTree(int degree) {
        this.degree = degree;

        LeafNode initialLeaf = new LeafNode(degree);

        this.root = initialLeaf;
        this.firstLeaf = initialLeaf;
    }

    
    public void insert(int studentId) {

        LeafNode leaf = findLeaf(studentId);

        leaf.keys.add(studentId);
        Collections.sort(leaf.keys);

        if (leaf.isOverflow()) {
            splitLeaf(leaf);
        }
    }

    private LeafNode findLeaf(int key) {

        Node current = root;

        while (current instanceof InternalNode) {

            InternalNode internal = (InternalNode) current;

            int i = 0;

            while (i < internal.keys.size()
                    && key >= internal.keys.get(i)) {
                i++;
            }

            current = internal.children.get(i);
        }

        return (LeafNode) current;
    }

    
    private void splitLeaf(LeafNode leaf) {

        LeafNode newLeaf = new LeafNode(degree);

        int splitIndex = (leaf.keys.size() + 1) / 2;

        newLeaf.keys.addAll(
            leaf.keys.subList(splitIndex, leaf.keys.size())
        );

        leaf.keys.subList(
            splitIndex, leaf.keys.size()
        ).clear();

        newLeaf.next = leaf.next;
        leaf.next = newLeaf;

        if (leaf == firstLeaf) {
            firstLeaf = leaf;
        }

        int separator = newLeaf.keys.get(0);

        insertIntoParent(leaf, separator, newLeaf);
    }

    private void insertIntoParent(
            Node left, int key, Node right) {

        if (left == root) {

            InternalNode newRoot = new InternalNode(degree);

            newRoot.keys.add(key);
            newRoot.children.add(left);
            newRoot.children.add(right);

            root = newRoot;
            return;
        }

        InternalNode parent = findParent(root, left);

        if (parent == null) {
            return;
        }

        int index = parent.children.indexOf(left);

        parent.keys.add(index, key);
        parent.children.add(index + 1, right);

        if (parent.isOverflow()) {
            splitInternal(parent);
        }
    }

    
    private InternalNode findParent(Node current, Node child) {

        if (!(current instanceof InternalNode)) {
            return null;
        }

        InternalNode internal = (InternalNode) current;

        if (internal.children.contains(child)) {
            return internal;
        }

        for (Node node : internal.children) {

            InternalNode result = findParent(node, child);

            if (result != null) {
                return result;
            }
        }

        return null;
    }


    private void splitInternal(InternalNode node) {

        int middle = node.keys.size() / 2;

        int promotedKey = node.keys.get(middle);

        InternalNode newInternal = new InternalNode(degree);

        newInternal.keys.addAll(
            node.keys.subList(middle + 1, node.keys.size())
        );

        newInternal.children.addAll(
            node.children.subList(middle + 1, node.children.size())
        );

        node.keys.subList(middle, node.keys.size()).clear();

        node.children.subList(
            middle + 1, node.children.size()
        ).clear();

        insertIntoParent(node, promotedKey, newInternal);
    }

    public List<Integer> searchRange(int minId, int maxId) {

        List<Integer> result = new ArrayList<>();

        if (minId > maxId) {
            return result;
        }

        LeafNode current = findLeaf(minId);

        while (current != null) {

            for (int key : current.keys) {

                if (key >= minId && key <= maxId) {
                    result.add(key);
                }

                if (key > maxId) {
                    return result;
                }
            }

            current = current.next;
        }

        return result;
    }

    public LeafNode getFirstLeaf() {
        return firstLeaf;
    }
}
