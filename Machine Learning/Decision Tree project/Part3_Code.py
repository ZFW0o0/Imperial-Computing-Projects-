##############################################################################
# Build  classification models by training decision trees on different training dataset (train_full.txt,
# train_sub.txt, train_noisy.txt)
# Evaluate model performance on test.txt dataset and calculate related evaluation metrics for report delivery
##############################################################################

import numpy as np
import sys
from classification import DecisionTreeClassifier
from kfold_cv_functions import split_data, cross_validation
from read_data import read_data
import evaluation_functions as eva

if __name__ == "__main__":
    attributes_data_test, label_data_test = read_data("data/test.txt")

    # Train decision tree on train_full.txt and calculate evaluation metrics
    print("Training the decision tree on full dataset")
    attributes_data_full, label_data_full = read_data("data/train_full.txt")
    classifier_full = DecisionTreeClassifier()
    classifier_full.fit(attributes_data_full, label_data_full)
    predictions_full = classifier_full.predict(attributes_data_test)

    confusion_matrix_full = eva.calculate_confusion_matrix(predictions_full, label_data_test)
    accuracy_full = eva.calculate_accuracy(confusion_matrix_full)
    recall_full = eva.calculate_recall_per_class(confusion_matrix_full)
    precision_full = eva.calculate_precision_per_class(confusion_matrix_full)
    F1_full = eva.calculate_F1_score_per_class(confusion_matrix_full)
    macro_avg_recall_full = eva.calculate_Macro_averaged_recall(confusion_matrix_full)
    macro_avg_precision_full = eva.calculate_Macro_averaged_precision(confusion_matrix_full)
    macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_full)

    np.set_printoptions(threshold=sys.maxsize)
    print("###Test results on decision tree trained by full dataset:###\n")
    print("Confusion Matrix: {}".format(confusion_matrix_full))
    print(f"Accuracy: {accuracy_full}")
    print("Recall: {}".format(recall_full))
    print("Precision: {}".format(precision_full))
    print("F1 score: {}".format(F1_full))
    print(f"Macro-averaged recall: {macro_avg_recall_full}")
    print(f"Macro-averaged precision: {macro_avg_precision_full}")
    print(f"Macro-averaged F1 score: {macro_avg_F1}")

    # Train decision tree on train_sub.txt and calculate evaluation metrics
    print("Training the decision tree on sub dataset")
    attributes_data_sub, label_data_sub = read_data("data/train_sub.txt")
    classifier_sub = DecisionTreeClassifier()
    classifier_sub.fit(attributes_data_sub, label_data_sub)
    predictions_sub = classifier_sub.predict(attributes_data_test)

    confusion_matrix_sub = eva.calculate_confusion_matrix(predictions_sub, label_data_test)
    accuracy_sub = eva.calculate_accuracy(confusion_matrix_sub)
    recall_sub = eva.calculate_recall_per_class(confusion_matrix_sub)
    precision_sub = eva.calculate_precision_per_class(confusion_matrix_sub)
    F1_sub = eva.calculate_F1_score_per_class(confusion_matrix_sub)
    macro_avg_recall_sub = eva.calculate_Macro_averaged_recall(confusion_matrix_sub)
    macro_avg_precision_sub = eva.calculate_Macro_averaged_precision(confusion_matrix_sub)
    macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_sub)

    np.set_printoptions(threshold=sys.maxsize)
    print("###Test results on decision tree trained by sub dataset:###\n")
    print("Confusion Matrix: {}".format(confusion_matrix_sub))
    print(f"Accuracy: {accuracy_sub}")
    print("Recall: {}".format(recall_sub))
    print("Precision: {}".format(precision_sub))
    print("F1 score: {}".format(F1_sub))
    print(f"Macro-averaged recall: {macro_avg_recall_sub}")
    print(f"Macro-averaged precision: {macro_avg_precision_sub}")
    print(f"Macro-averaged F1 score: {macro_avg_F1}")

    # Train decision tree on train_noisy.txt and calculate evaluation metrics
    print("Training the decision tree on noisy dataset")
    attributes_data_noisy, label_data_noisy = read_data("data/train_noisy.txt")
    classifier_noisy = DecisionTreeClassifier()
    classifier_noisy.fit(attributes_data_noisy, label_data_noisy)
    predictions_noisy = classifier_noisy.predict(attributes_data_test)

    confusion_matrix_noisy = eva.calculate_confusion_matrix(predictions_noisy, label_data_test)
    accuracy_noisy = eva.calculate_accuracy(confusion_matrix_noisy)
    recall_noisy = eva.calculate_recall_per_class(confusion_matrix_noisy)
    precision_noisy = eva.calculate_precision_per_class(confusion_matrix_noisy)
    F1_noisy = eva.calculate_F1_score_per_class(confusion_matrix_noisy)
    macro_avg_recall_noisy = eva.calculate_Macro_averaged_recall(confusion_matrix_noisy)
    macro_avg_precision_noisy = eva.calculate_Macro_averaged_precision(confusion_matrix_noisy)
    macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_noisy)

    np.set_printoptions(threshold=sys.maxsize)
    print("###Test results on decision tree trained by noisy dataset:###\n")
    print("Confusion Matrix: {}".format(confusion_matrix_noisy))
    print(f"Accuracy: {accuracy_noisy}")
    print("Recall: {}".format(recall_noisy))
    print("Precision: {}".format(precision_noisy))
    print("F1 score: {}".format(F1_noisy))
    print(f"Macro-averaged recall: {macro_avg_recall_noisy}")
    print(f"Macro-averaged precision: {macro_avg_precision_noisy}")
    print(f"Macro-averaged F1 score: {macro_avg_F1}")

    # Perform k-fold cross validation on full dataset
    x, y = read_data("data/train_full.txt")
    K_fold_dataset = split_data(10, np.size(y))
    accuracy_matrix, average_accuracy, standard_deviation = cross_validation(10, K_fold_dataset, x, y)
    print("Accuracy matrix:\n", accuracy_matrix, "\n")
    print("Average_accuracy: ", round(average_accuracy, 4), "\n")
    print("Standard deviation of accuracies: ", round(standard_deviation, 4))
