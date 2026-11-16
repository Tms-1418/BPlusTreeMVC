# models/bplus_tree.py

class Node:
    """Clase base abstracta (conceptual) para los nodos del árbol."""

    def __init__(self, degree):
        self.keys = []
        self.degree = degree

    def is_overflow(self):
        # Si el número de claves alcanza el grado, hay que hacer split
        return len(self.keys) >= self.degree


class InternalNode(Node):
    """Nodo interno: solo actúa como guía/índice."""

    def __init__(self, degree):
        super().__init__(degree)
        self.children = []


class LeafNode(Node):
    """Nodo hoja: guarda los datos y se enlaza con la siguiente hoja."""

    def __init__(self, degree):
        super().__init__(degree)
        self.next_leaf = None  # El enlace horizontal clave del B+


class BPlusTree:
    """Implementación didáctica del Árbol B+ (enfocada en hojas y rangos)."""

    def __init__(self, degree=3):
        self.degree = degree
        # Iniciamos (por simplicidad del demo) asumiendo que la raíz es una hoja
        self.root = LeafNode(degree)

    def insert(self, student_id: int):
        """Inserta un nuevo estudiante. Si la hoja se llena, hace un split."""
        if not self.root.is_overflow():
            self.root.keys.append(student_id)
            self.root.keys.sort()  # Mantenemos las claves ordenadas
        else:
            # Lógica de Split (División de la hoja llena)
            new_leaf = LeafNode(self.degree)

            # Añadimos el nuevo ID y reordenamos antes de dividir
            self.root.keys.append(student_id)
            self.root.keys.sort()

            # Calculamos la mitad
            mid_index = len(self.root.keys) // 2

            # Pasamos la mitad superior a la nueva hoja
            new_leaf.keys = self.root.keys[mid_index:]
            # Y dejamos la mitad inferior en la hoja original
            self.root.keys = self.root.keys[:mid_index]

            # ¡MANTENEMOS LA LISTA ENLAZADA! (La magia del B+)
            new_leaf.next_leaf = self.root.next_leaf
            self.root.next_leaf = new_leaf

            # Para la demostración rápida (KISS), avanzamos la referencia
            # a la nueva hoja. En un sistema real, crearíamos un InternalNode arriba.
            self.root = new_leaf

    def search_range(self, min_id: int, max_id: int, start_node: LeafNode) -> list:
        """
        La operación estrella: Recorre la lista enlazada de hojas sin
        subir y bajar por el árbol, obteniendo velocidad O(K).
        """
        results = []
        current = start_node

        while current is not None:
            for key in current.keys:
                if min_id <= key <= max_id:
                    results.append(key)

                # Optimización: si superamos el máximo, detenemos la búsqueda de inmediato
                if key > max_id:
                    return results

            # Avanzamos a la siguiente hoja sin tener que usar recursión
            current = current.next_leaf

        return results