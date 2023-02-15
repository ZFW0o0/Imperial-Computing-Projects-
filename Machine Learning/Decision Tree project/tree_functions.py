import numpy as np
import calculate_percentage as cp
import node_class as node
import calculate_entropy as ce


def build_tree(attributes_data, label_data):
    if ce.calculate_entropy(label_data) == 0:
        leaf = node.Node(True)
        leaf.add_leaf(label_data[0])
        return leaf

    reference_column, reference_value, smaller_set_attribute, smaller_set_label, larger_set_attribute, larger_set_label = ce.find_best_split(
        attributes_data, label_data)

    if (reference_column == -1) or (reference_value == -1):
        num_of_value, percentage = cp.calculate_label_percentage(label_data)
        leaf = node.Node(True)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
        return leaf

    root = node.Node(False)

    root.add_reference_column(reference_column)
    root.add_reference_value(reference_value)
    root.add_left_node(build_tree(smaller_set_attribute, smaller_set_label))
    root.add_right_node(build_tree(larger_set_attribute, larger_set_label))

    return root


def make_predict(predict_attributes, this_node):
    if this_node.is_leaf:
        return this_node.leaf
    if predict_attributes[this_node.reference_column] < this_node.reference_value:
        return make_predict(predict_attributes, this_node.left)
    else:
        return make_predict(predict_attributes, this_node.right)


def print_tree(this_node, level):
    for i in range(level):
        print("     ", end="")

    if level == 0:
        print("+----root:", this_node.reference_column, "  ", this_node.reference_value)
    elif this_node.is_leaf:
        print("+----leaf: ", this_node.leaf)
    else:
        print("+----node:", this_node.reference_column, "  ", this_node.reference_value)

    if not this_node.is_leaf:
        print_tree(this_node.right, level + 1)
        print_tree(this_node.left, level + 1)