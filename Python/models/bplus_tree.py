from abc import ABC


class Node(ABC):
    def __init__(self, degree):
        self.keys = []
        self.degree = degree

    def is_overflow(self):
        return len(self.keys) >= self.degree


class LeafNode(Node):
    def __init__(self, degree):
        super().__init__(degree)
        self.next = None


class InternalNode(Node):
    def __init__(self, degree):
        super().__init__(degree)
        self.children = []


class BPlusTree:
    def __init__(self, degree):
        self.degree = degree
        initial_leaf = LeafNode(degree)
        self.root = initial_leaf
        self.first_leaf = initial_leaf

    def insert(self, student_id):
        leaf = self.find_leaf(student_id)
        leaf.keys.append(student_id)
        leaf.keys.sort()

        if leaf.is_overflow():
            self.split_leaf(leaf)

    def find_leaf(self, key):
        current = self.root

        while isinstance(current, InternalNode):
            i = 0
            while i < len(current.keys) and key >= current.keys[i]:
                i += 1
            current = current.children[i]

        return current

    def split_leaf(self, leaf):
        new_leaf = LeafNode(self.degree)
        split_index = (len(leaf.keys) + 1) // 2

        new_leaf.keys.extend(leaf.keys[split_index:])
        del leaf.keys[split_index:]

        new_leaf.next = leaf.next
        leaf.next = new_leaf

        if leaf is self.first_leaf:
            self.first_leaf = leaf

        separator = new_leaf.keys[0]
        self.insert_into_parent(leaf, separator, new_leaf)

    def insert_into_parent(self, left, key, right):
        if left is self.root:
            new_root = InternalNode(self.degree)
            new_root.keys.append(key)
            new_root.children.append(left)
            new_root.children.append(right)
            self.root = new_root
            return

        parent = self.find_parent(self.root, left)
        if parent is None:
            return

        index = parent.children.index(left)
        parent.keys.insert(index, key)
        parent.children.insert(index + 1, right)

        if parent.is_overflow():
            self.split_internal(parent)

    def find_parent(self, current, child):
        if not isinstance(current, InternalNode):
            return None

        if child in current.children:
            return current

        for node in current.children:
            result = self.find_parent(node, child)
            if result is not None:
                return result

        return None

    def split_internal(self, node):
        middle = len(node.keys) // 2
        promoted_key = node.keys[middle]

        new_internal = InternalNode(self.degree)
        new_internal.keys.extend(node.keys[middle + 1:])
        new_internal.children.extend(node.children[middle + 1:])

        del node.keys[middle:]
        del node.children[middle + 1:]

        self.insert_into_parent(node, promoted_key, new_internal)

    def search_range(self, min_id, max_id):
        result = []

        if min_id > max_id:
            return result

        current = self.find_leaf(min_id)

        while current is not None:
            for key in current.keys:
                if min_id <= key <= max_id:
                    result.append(key)
                if key > max_id:
                    return result
            current = current.next

        return result

    def get_first_leaf(self):
        return self.first_leaf