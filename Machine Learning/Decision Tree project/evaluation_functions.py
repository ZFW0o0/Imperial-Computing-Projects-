"""
This file contains all the functions for evaluation of classifier
"""
import numpy as np

"""
function to calculate the confusion matrix. The first input parameter is a 1D np array, which is the predicted value, namely the result of the make prediction function.
The second parameter is np array of the same size as the first, which is the correct answer(actual label).
The out put is the 2D square np matrix
"""


def calculate_confusion_matrix(predicted, actual):
    # check if the two input parameters are 1D and have the same size
    if predicted.ndim != 1 or actual.ndim != 1 or np.size(predicted) != np.size(actual):
        print("Wrong input format when calculating confusion matrix!")
        quit()

    # calculate the number of different types of labels
    actual_label_unique = np.unique(actual)

    confusion_matrix = np.zeros(np.square(len(actual_label_unique))).reshape(len(actual_label_unique),
                                                                             len(actual_label_unique))

    # construct the matrix by iterating over the predicted result and comparing every result with actual result
    for i in range(np.size(predicted, 0)):
        if predicted[i] == actual[i]:
            for j in range(np.size(actual_label_unique, 0)):
                if predicted[i] == actual_label_unique[j]:
                    confusion_matrix[j][j] += 1
                    break
        if predicted[i] != actual[i]:
            actual_label_index = -1
            predicted_label_index = -1
            for j in range(np.size(actual_label_unique, 0)):
                if predicted[i] == actual_label_unique[j]:
                    predicted_label_index = j
                if actual[i] == actual_label_unique[j]:
                    actual_label_index = j
                if actual_label_index != -1 and predicted_label_index != -1:
                    break
            if predicted_label_index != -1:
                confusion_matrix[actual_label_index][predicted_label_index] += 1
            else:
                print("Unexpected predicted value")
                quit()
    return confusion_matrix


"""
function to calculate accuracy. The input parameter is a confusion matrix. The output is double
"""


def calculate_accuracy(confusion_matrix):
    correct_num = np.trace(confusion_matrix)
    total_num = np.sum(confusion_matrix)
    accuracy = correct_num / total_num
    return accuracy


"""
function to calculate recall for every class. The input parameter is a confusion matrix. The output is 1D np array contains the recall of every class.
"""


def calculate_recall_per_class(confusion_matrix):
    recall = np.zeros(np.size(confusion_matrix, 0))
    for i in range(np.size(confusion_matrix, 1)):
        recall[i] = confusion_matrix[i][i] / np.sum(confusion_matrix[i, :])
    return recall


"""
function to calculate precision for every class. The input parameter is a confusion matrix. The output is 1D np array contains the precision of every class.
"""


def calculate_precision_per_class(confusion_matrix):
    precision = np.zeros(np.size(confusion_matrix, 0))
    for i in range(np.size(confusion_matrix, 0)):
        precision[i] = confusion_matrix[i][i] / np.sum(confusion_matrix[:, i])
    return precision


"""
function to calculate F1_score for every class. The input parameter is a confusion matrix. The output is 1D np array contains the F1_score of every class.
"""


def calculate_F1_score_per_class(confusion_matrix):
    recall = calculate_recall_per_class(confusion_matrix)
    precision = calculate_precision_per_class(confusion_matrix)
    F1_score = 2 * precision * recall / (precision + recall)
    return F1_score


"""
function to calculate Macro averaged recall. The input parameter is a confusion matrix. The output is double.
"""


def calculate_Macro_averaged_recall(confusion_matrix):
    recall = calculate_recall_per_class(confusion_matrix)
    Macro_averaged_recall = np.mean(recall)
    return Macro_averaged_recall


"""
function to calculate Macro averaged precision. The input parameter is a confusion matrix. The output is double.
"""


def calculate_Macro_averaged_precision(confusion_matrix):
    precision = calculate_precision_per_class(confusion_matrix)
    Macro_averaged_precision = np.mean(precision)
    return Macro_averaged_precision


"""
function to calculate Macro averaged f1_score. The input parameter is a confusion matrix. The output is double.
"""


def calculate_Macro_averaged_f1_score(confusion_matrix):
    F1_score = calculate_F1_score_per_class(confusion_matrix)
    Macro_averaged_F1_score = np.mean(F1_score)
    return Macro_averaged_F1_score
