##############################################################################
# Introduction to Machine Learning
# Coursework 1 Skeleton code
# Prepared by: Josiah Wang
#
# Your tasks: Complete the train_and_predict() function. 
#             You are free to add any other methods as needed. 
##############################################################################

import numpy as np
import columns_to_drop as ctd
from classification import DecisionTreeClassifier, DecisionTreeClassifierES
import evaluation_functions as eva


def train_and_predict(x_train, y_train, x_test, x_val, y_val, drop_col_num=1):
    """ Interface to train and test the new/improved decision tree.
    
    This function is an interface for training and testing the new/improved
    decision tree classifier. 

    x_train and y_train should be used to train your classifier, while 
    x_test should be used to test your classifier. 
    x_val and y_val may optionally be used as the validation dataset. 
    You can just ignore x_val and y_val if you do not need a validation dataset.

    Args:
    x_train (numpy.ndarray): Training instances, numpy array of shape (N, K) 
                       N is the number of instances
                       K is the number of attributes
    y_train (numpy.ndarray): Class labels, numpy array of shape (N, )
                       Each element in y is a str 
    x_test (numpy.ndarray): Test instances, numpy array of shape (M, K) 
                            M is the number of test instances
                            K is the number of attributes
    x_val (numpy.ndarray): Validation instances, numpy array of shape (L, K) 
                       L is the number of validation instances
                       K is the number of attributes
    y_val (numpy.ndarray): Class labels of validation set, numpy array of shape (L, )
    
    Returns:
    numpy.ndarray: A numpy array of shape (M, ) containing the predicted class label for each instance in x_test
    """

    #######################################################################
    #                 ** TASK 4.1: COMPLETE THIS FUNCTION **
    #######################################################################

    # TODO: Train new classifier
    drop_cols_list = ctd.columns_to_drop(x_train, drop_col_num)

    best_classifier = DecisionTreeClassifierES()
    best_accuracy = 0
    best_drop_cols = []
    # iterate over drop_cols_list and compare model accuracy for each set of dropped columns
    # on the validation datasets
    for i in range(len(drop_cols_list)):
        x_train_subset = np.delete(x_train, drop_cols_list[i], 1)
        x_val_subset = np.delete(x_val, drop_cols_list[i], 1)
        print("Fitting model {num} after dropping columns: {dropped}".format(num=(i + 1), dropped=drop_cols_list[i]))

        temp_classifier = DecisionTreeClassifierES()
        temp_classifier.fit_early_stop(x_train_subset, y_train, early_stop=3, stop_value=15)
        temp_predictions = temp_classifier.predict(x_val_subset)

        temp_confusion_matrix = eva.calculate_confusion_matrix(temp_predictions, y_val)
        temp_accuracy = eva.calculate_accuracy(temp_confusion_matrix)

        if temp_accuracy > best_accuracy:
            best_classifier = temp_classifier
            best_accuracy = temp_accuracy
            best_drop_cols = drop_cols_list[i]

        print("Process is {per}% complete".format(per=round(((i + 1) * 100 / len(drop_cols_list)), 1)))

    # set up an empty (M, ) numpy array to store the predicted labels 
    # feel free to change this if needed
    # predictions = np.zeros((x_test.shape[0],), dtype=np.object)

    # TODO: Make predictions on x_test using new classifier
    print("Best columns to be dropped are: {}".format(best_drop_cols))
    x_test_subset = np.delete(x_test, best_drop_cols, 1)
    predictions = best_classifier.predict(x_test_subset)

    # remember to change this if you rename the variable
    return predictions
