class Node:
    def __init__(self, is_leaf):
        self.left = None
        self.right = None
        self.leaf = None
        self.is_leaf = is_leaf
        self.reference_column = None
        self.reference_value = None

    def add_left_node(self, child_node):
        self.left = child_node

    def add_right_node(self, child_node):
        self.right = child_node

    def add_leaf(self, leaf):
        if self.is_leaf:
            self.leaf = leaf
        else:
            print("This node is not a leaf!")

    def add_reference_column(self, reference_column):
        self.reference_column = reference_column

    def add_reference_value(self, reference_value):
        self.reference_value = reference_value
