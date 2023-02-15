from read_data import read_data
import numpy as np
from calculate_percentage import calculate_label_percentage


# calculate the entropy for a set of given label_data
def calculate_entropy(label_data):
    num, label_percentage = calculate_label_percentage(label_data)

    entropy = 0
    for i in range(26):
        if label_percentage[i] != 0:
            entropy = entropy - (label_percentage[i]) * np.log2((label_percentage[i]))

    return entropy


# calculate the entropy of two split set of label data
# split according to attributes data's reference column and reference value

def calculate_entropy_by_attributes(attributes_data, label_data, reference_column, reference_value):
    entropy = 0
    smaller_set = label_data[(attributes_data[:, reference_column] < reference_value)]
    larger_set = label_data[(attributes_data[:, reference_column] > reference_value)]
    smaller_set_entropy = calculate_entropy(smaller_set)
    larger_set_entropy = calculate_entropy(larger_set)
    entropy = np.size(smaller_set) / np.size(label_data) * smaller_set_entropy + np.size(larger_set) / np.size(
        label_data) * larger_set_entropy
    return entropy


# find the best split way which leads to the smallest entropy
# return reference column and reference value
def find_best_split(attributes_data, label_data):
    reference_column = -1
    reference_value = -1
    entropy = calculate_entropy(label_data)
    for i in range(np.size(attributes_data, 1)):
        for j in range(round(np.min(attributes_data[:, i])), round(np.max(attributes_data[:, i]))):
            if calculate_entropy_by_attributes(attributes_data, label_data, i, 0.5 + j) < entropy:
                entropy = calculate_entropy_by_attributes(attributes_data, label_data, i, 0.5 + j)
                reference_column = i
                reference_value = j + 0.5
    smaller_set_attribute = attributes_data[(attributes_data[:, reference_column] < reference_value)]
    larger_set_attribute = attributes_data[(attributes_data[:, reference_column] > reference_value)]
    smaller_set_label = label_data[(attributes_data[:, reference_column] < reference_value)]
    larger_set_label = label_data[(attributes_data[:, reference_column] > reference_value)]
    return reference_column, reference_value, smaller_set_attribute, smaller_set_label, larger_set_attribute, larger_set_label