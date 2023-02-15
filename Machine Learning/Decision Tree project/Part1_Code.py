import numpy as np
import matplotlib.pyplot as plt
from read_data import read_data

# Part 1 Understanding the data
full_features, full_labels = read_data("./data/train_full.txt")
sub_features, sub_labels = read_data("./data/train_sub.txt")
noisy_features, noisy_labels = read_data("./data/train_noisy.txt")

# code to visualise the data labels
unique, counts = np.unique(noisy_labels, return_counts=True)
count_labels_dict = dict(zip(unique, counts))
print(count_labels_dict)
total_count = sum(counts)

graph = plt.bar(count_labels_dict.keys(), count_labels_dict.values())

i = 0
for p in graph:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()

    plt.text(x + width / 2,
             y + height * 1.01,
             str(round(count_labels_dict[list(count_labels_dict.keys())[i]] * 100 / total_count, 1)) + '%',
             ha='center',
             weight='bold')
    i += 1

plt.show()

# code to interrogate the data features
# check each column of features array for type and range
temp_array = full_features
type_dict = dict()
min_dict = dict()
max_dict = dict()

for j in range(temp_array.shape[1]):
    col_type = type(0)
    for i in range(temp_array.shape[0]):
        if (i != 0) and (type(temp_array[i, j]) != col_type):
            print("Mismatching type in column{col} row{row} detected".format(col=j, row=i))
        col_type = type(temp_array[i, j])

    type_dict[j] = col_type
    min_dict[j] = min(temp_array[:, j])
    max_dict[j] = max(temp_array[:, j])
print(type_dict)
print(min_dict)
print(max_dict)

range_array = np.empty((3, temp_array.shape[1]))
for j in range(temp_array.shape[1]):
    range_array[0, j] = j
    range_array[1, j] = min_dict[j]
    range_array[2, j] = max_dict[j]
print(range_array)

# code to compare full and noisy training datasets
unq, count = np.unique(full_features, axis=0, return_counts=True)
print(sum(i > 1 for i in count))

num_equal = 0
num_diff = 0
checked_list = []

for i in range(full_features.shape[0]):
    temp_array = full_features[i, :]
    for i2 in range(noisy_features.shape[0]):
        comp_array = noisy_features[i2, :]
        if (np.array_equal(temp_array, comp_array)) and (i2 not in checked_list):
            if full_labels[i] == noisy_labels[i2]:
                num_equal += 1
            else:
                num_diff += 1

            checked_list.append(i2)

if full_features.shape[0] != (num_equal + num_diff):
    print("Total does not tally, need to check")
print(num_equal)
print(num_equal / (num_equal + num_diff))
print(num_diff)
print(num_diff / (num_equal + num_diff))

# check if dataset contains duplicated rows
full_data = np.loadtxt("./data/train_full.txt", delimiter=',', dtype=str)
unique_data = np.unique(full_data, axis=0)
print(unique_data.shape)
