import numpy as np


# generate all combinations based on input_list
def combs(combination_list):
    if len(combination_list) == 0:
        return [[]]
    cs = []
    for c in combs(combination_list[1:]):
        cs += [c, c + [combination_list[0]]]
    return cs


# generate list of column combinations to drop from dataset x based on drop_num
def columns_to_drop(x, drop_num):
    if np.shape(x)[1] < drop_num:
        print("Unable to determine columns to drop as drop_num exceeds num of columns in dataset")
        print("Returning empty list")
        return []

    col_num = []
    for i in range(np.shape(x)[1]):
        col_num.append(i)

    combinations = combs(col_num)

    drop_list = []
    for i in range(len(combinations)):
        if len(combinations[i]) == drop_num:
            drop_list.append(combinations[i])

    return drop_list
