import numpy as np


def read_data(filename):
    buffer_data = np.loadtxt(filename, delimiter=',', dtype=str, max_rows=1)
    last_column = len(buffer_data) - 1
    attributes_column = []

    for i in range(last_column):
        attributes_column.append(i)

    attributes_data = np.loadtxt(filename, delimiter=',', dtype=int, usecols=attributes_column)
    label_data = np.loadtxt(filename, delimiter=',', dtype=str, usecols=last_column)

    return attributes_data, label_data