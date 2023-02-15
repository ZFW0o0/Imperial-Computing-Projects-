import numpy as np
from numpy.random import default_rng
from classification import DecisionTreeClassifier
from evaluation_functions import calculate_confusion_matrix, calculate_accuracy

"""
function to perform splitting for k times to split dataset into k-1 training folds and 1 testing fold.
"""


def split_data(k_fold, n_instances, random_generator=default_rng(60012)):
    # generate a random permutation of indices from 0 to n_instances
    shuffled_indices = random_generator.permutation(n_instances)

    # split shuffled indices into almost equal sized splits
    split_indices = np.array_split(shuffled_indices, k_fold)

    folds = []
    for k in range(k_fold):
        test_indices = split_indices[k]

        # combine remaining splits as train
        train_indices = np.hstack(split_indices[:k] + split_indices[k + 1:])

        folds.append([train_indices, test_indices])

    return folds


"""
function to perform k-fold cross validation on a dataset
"""


def cross_validation(k_fold, split_folds, attributes_data, label_data):
    accuracies = []
    for i in range(k_fold):
        train_indices = split_folds[i][0]
        test_indices = split_folds[i][1]

        attribute_train = attributes_data[train_indices, :]
        label_train = label_data[train_indices]
        attribute_test = attributes_data[test_indices, :]
        label_test = label_data[test_indices]

        # Train the decision tree
        classifier = DecisionTreeClassifier()
        classifier.fit(attribute_train, label_train)
        predictions = classifier.predict(attribute_test)

        confusion_matrix = calculate_confusion_matrix(predictions, label_test)
        acc = calculate_accuracy(confusion_matrix)
        accuracies.append(acc)

    # Calculate average accuracy and standard deviation across the 10 folds of cross-validation
    accuracies_np = np.array(accuracies)
    avg_accuracy = accuracies_np.mean()
    std_dev = accuracies_np.std()
    return accuracies, avg_accuracy, std_dev
