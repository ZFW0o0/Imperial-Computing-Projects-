import numpy as np
import calculate_percentage as cp
import node_class as node
import calculate_entropy as ce


def build_tree_early_stop_by_entropy(attributes_data, label_data, stop_entropy):
    if ce.calculate_entropy(label_data) == 0:
        leaf = node.Node(True)
        leaf.add_leaf(label_data[0])
        return leaf

    if ce.calculate_entropy(label_data) <= stop_entropy:
        leaf = node.Node(True)
        num_of_value, percentage = cp.calculate_label_percentage(label_data)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
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
    root.add_left_node(build_tree_early_stop_by_entropy(smaller_set_attribute, smaller_set_label, stop_entropy))
    root.add_right_node(build_tree_early_stop_by_entropy(larger_set_attribute, larger_set_label, stop_entropy))

    return root


def build_tree_early_stop_by_percentage(attributes_data, label_data, stop_percentage):
    if ce.calculate_entropy(label_data) == 0:
        leaf = node.Node(True)
        leaf.add_leaf(label_data[0])
        return leaf

    num_of_value, percentage = cp.calculate_label_percentage(label_data)

    if np.max(percentage) >= stop_percentage:
        leaf = node.Node(True)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
        return leaf

    reference_column, reference_value, smaller_set_attribute, smaller_set_label, larger_set_attribute, larger_set_label = ce.find_best_split(
        attributes_data, label_data)

    if (reference_column == -1) or (reference_value == -1):
        leaf = node.Node(True)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
        return leaf

    root = node.Node(False)

    root.add_reference_column(reference_column)
    root.add_reference_value(reference_value)
    root.add_left_node(build_tree_early_stop_by_percentage(smaller_set_attribute, smaller_set_label, stop_percentage))
    root.add_right_node(build_tree_early_stop_by_percentage(larger_set_attribute, larger_set_label, stop_percentage))

    return root


def build_tree_early_stop_by_depth(attributes_data, label_data, stop_count):
    if ce.calculate_entropy(label_data) == 0:
        leaf = node.Node(True)
        leaf.add_leaf(label_data[0])
        return leaf

    num_of_value, percentage = cp.calculate_label_percentage(label_data)

    if stop_count == 0:
        leaf = node.Node(True)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
        return leaf

    reference_column, reference_value, smaller_set_attribute, smaller_set_label, larger_set_attribute, larger_set_label = ce.find_best_split(
        attributes_data, label_data)

    if (reference_column == -1) or (reference_value == -1):
        leaf = node.Node(True)
        leaf.add_leaf(chr(np.argmax(percentage) + ord('A')))
        return leaf

    root = node.Node(False)

    root.add_reference_column(reference_column)
    root.add_reference_value(reference_value)
    root.add_left_node(build_tree_early_stop_by_depth(smaller_set_attribute, smaller_set_label, stop_count - 1))
    root.add_right_node(build_tree_early_stop_by_depth(larger_set_attribute, larger_set_label, stop_count - 1))

    return root