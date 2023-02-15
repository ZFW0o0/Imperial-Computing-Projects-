import numpy as np


# np.set_printoptions(precision=3, suppress=True)


def calculate_label_percentage(label_data):
    num_of_datas = label_data.shape[0]
    num_of_value = np.zeros(26, dtype=int)

    for i in range(num_of_datas):
        for k in range(26):

            if label_data[i] == chr(ord('A') + k):
                num_of_value[k] = num_of_value[k] + 1
                break
    percentage = np.divide(num_of_value, num_of_datas)
    return num_of_value, percentage
