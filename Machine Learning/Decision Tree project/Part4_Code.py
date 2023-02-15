##############################################################################
# Build  classification models by training decision trees on different training dataset (train_full.txt,
# train_sub.txt, train_noisy.txt)
# Evaluate model performance on test.txt dataset and calculate related evaluation metrics for report delivery
##############################################################################
import sys
import numpy as np
from classification import DecisionTreeClassifierES
from kfold_cv_functions import split_data, cross_validation
from principal_component_analysis import calculate_pca_characteristics
from read_data import read_data
import evaluation_functions as eva
import matplotlib.pyplot as plt
from improvement import train_and_predict

if __name__ == "__main__":
    # # Train decision tree on train_full.txt with early stop and produce charts
    # print("Training the decision tree on full dataset with early stop")
    # attributes_data_full, label_data_full = read_data("data/train_full.txt")
    # attributes_data_validation, label_data_validation = read_data("data/validation.txt")
    # classifier_full_es = DecisionTreeClassifierES()
    #
    # accuracy_list = []
    # step_list = []
    # for i in range(20, 105, 5):
    #     classifier_full_es.fit_early_stop(attributes_data_full, label_data_full, early_stop=2, stop_value=i / 100)
    #     predictions_full_es = classifier_full_es.predict(attributes_data_validation)
    #
    #     confusion_matrix_full_es = eva.calculate_confusion_matrix(predictions_full_es, label_data_validation)
    #     accuracy_full_es = eva.calculate_accuracy(confusion_matrix_full_es)
    #
    #     accuracy_list.append(accuracy_full_es)
    #     step_list.append(i / 100)
    #
    # plt.plot(step_list, accuracy_list)
    # plt.title("Accuracy at different early stop percentage levels")
    # plt.xlabel("Percentage Stop Value")
    # plt.ylabel("Accuracy")
    # plt.show()
    # ------------------------------------------------------------------------------------------------------------------
    # # Train decision tree on train_full.txt with early stop over k folds and produce charts
    # print("Training the decision tree on full dataset with early stop")
    # x, y = read_data("data/train_full.txt")
    # split_folds = split_data(10, np.size(y))
    # all_accuracy = []
    # all_step = []
    # for k in range(10):
    #     train_indices = split_folds[k][0]
    #     test_indices = split_folds[k][1]
    #
    #     attributes_data_full = x[train_indices, :]
    #     label_data_full = y[train_indices]
    #     attributes_data_validation = x[test_indices, :]
    #     label_data_validation = y[test_indices]
    #     classifier_full_es = DecisionTreeClassifierES()
    #
    #     accuracy_list = []
    #     step_list = []
    #     for i in range(5, 25, 1):
    #         classifier_full_es.fit_early_stop(attributes_data_full, label_data_full, early_stop=3, stop_value=i)
    #         predictions_full_es = classifier_full_es.predict(attributes_data_validation)
    #
    #         confusion_matrix_full_es = eva.calculate_confusion_matrix(predictions_full_es, label_data_validation)
    #         accuracy_full_es = eva.calculate_accuracy(confusion_matrix_full_es)
    #
    #         accuracy_list.append(accuracy_full_es)
    #         step_list.append(i)
    #
    #     all_accuracy.append(accuracy_list)
    #     all_step.append(step_list)
    #
    # avg_accuracy = [sum(sub_list) / len(sub_list) for sub_list in zip(*all_accuracy)]
    # avg_step = [sum(sub_list) / len(sub_list) for sub_list in zip(*all_step)]
    #
    # plt.plot(avg_step, avg_accuracy)
    # plt.title("Accuracy at different early stop depth levels")
    # plt.xlabel("Depth Stop Value")
    # plt.ylabel("Accuracy")
    # plt.show()
    # ------------------------------------------------------------------------------------------------------------------
    # # Train decision tree on train_full.txt and calculate evaluation metrics
    # attributes_data_test, label_data_test = read_data("data/test.txt")
    # print("Training the decision tree on full dataset based on early stop depth")
    # attributes_data_full, label_data_full = read_data("data/train_full.txt")
    # classifier_full = DecisionTreeClassifierES()
    # classifier_full.fit_early_stop(attributes_data_full, label_data_full, early_stop=3, stop_value=15)
    # predictions_full = classifier_full.predict(attributes_data_test)
    #
    # confusion_matrix_full = eva.calculate_confusion_matrix(predictions_full, label_data_test)
    # accuracy_full = eva.calculate_accuracy(confusion_matrix_full)
    # recall_full = eva.calculate_recall_per_class(confusion_matrix_full)
    # precision_full = eva.calculate_precision_per_class(confusion_matrix_full)
    # F1_full = eva.calculate_F1_score_per_class(confusion_matrix_full)
    # macro_avg_recall_full = eva.calculate_Macro_averaged_recall(confusion_matrix_full)
    # macro_avg_precision_full = eva.calculate_Macro_averaged_precision(confusion_matrix_full)
    # macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_full)
    #
    # np.set_printoptions(threshold=sys.maxsize)
    # print("###Test results on decision tree trained by full dataset:###\n")
    # print("Confusion Matrix: \n{}".format(confusion_matrix_full))
    # print(f"Accuracy: {accuracy_full}")
    # print("Recall: {}".format(recall_full))
    # print("Precision: {}".format(precision_full))
    # print("F1 score: {}".format(F1_full))
    # print(f"Macro-averaged recall: {macro_avg_recall_full}")
    # print(f"Macro-averaged precision: {macro_avg_precision_full}")
    # print(f"Macro-averaged F1 score: {macro_avg_F1}")
    # ------------------------------------------------------------------------------------------------------------------
    # # Test for principal component analysis of full training dataset
    # x, y = read_data("data/train_full.txt")
    # eigenvectors, eigenvalues, eigenvector_contribution = calculate_pca_characteristics(x)
    # print(eigenvectors)
    # print(eigenvalues)
    # print(np.around(eigenvector_contribution * 100, decimals=1))
    # ------------------------------------------------------------------------------------------------------------------
    # Test train_and_predict method from improvement.py on train_full
    attributes_data_full, label_data_full = read_data("data/train_full.txt")
    attributes_data_val, label_data_val = read_data("data/validation.txt")
    attributes_data_test, label_data_test = read_data("data/test.txt")

    predictions_imp = train_and_predict(attributes_data_full, label_data_full, attributes_data_test,
                                        attributes_data_val, label_data_val, drop_col_num=1)

    confusion_matrix_imp = eva.calculate_confusion_matrix(predictions_imp, label_data_test)
    accuracy_imp = eva.calculate_accuracy(confusion_matrix_imp)
    recall_imp = eva.calculate_recall_per_class(confusion_matrix_imp)
    precision_imp = eva.calculate_precision_per_class(confusion_matrix_imp)
    F1_imp = eva.calculate_F1_score_per_class(confusion_matrix_imp)
    macro_avg_recall_imp = eva.calculate_Macro_averaged_recall(confusion_matrix_imp)
    macro_avg_precision_imp = eva.calculate_Macro_averaged_precision(confusion_matrix_imp)
    macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_imp)

    np.set_printoptions(threshold=sys.maxsize)
    print("###Test results on decision tree trained by train_predict_method:###\n")
    print("Confusion Matrix: \n{}".format(confusion_matrix_imp))
    print(f"Accuracy: {accuracy_imp}")
    print("Recall: {}".format(recall_imp))
    print("Precision: {}".format(precision_imp))
    print("F1 score: {}".format(F1_imp))
    print(f"Macro-averaged recall: {macro_avg_recall_imp}")
    print(f"Macro-averaged precision: {macro_avg_precision_imp}")
    print(f"Macro-averaged F1 score: {macro_avg_F1}")
    # ------------------------------------------------------------------------------------------------------------------
    # # Test train_and_predict method from improvement.py on train_noisy
    # attributes_data_full, label_data_full = read_data("data/train_noisy.txt")
    # attributes_data_val, label_data_val = read_data("data/validation.txt")
    # attributes_data_test, label_data_test = read_data("data/test.txt")
    #
    # predictions_imp = train_and_predict(attributes_data_full, label_data_full, attributes_data_test,
    #                                     attributes_data_val, label_data_val, drop_col_num=1)
    #
    # confusion_matrix_imp = eva.calculate_confusion_matrix(predictions_imp, label_data_test)
    # accuracy_imp = eva.calculate_accuracy(confusion_matrix_imp)
    # recall_imp = eva.calculate_recall_per_class(confusion_matrix_imp)
    # precision_imp = eva.calculate_precision_per_class(confusion_matrix_imp)
    # F1_imp = eva.calculate_F1_score_per_class(confusion_matrix_imp)
    # macro_avg_recall_imp = eva.calculate_Macro_averaged_recall(confusion_matrix_imp)
    # macro_avg_precision_imp = eva.calculate_Macro_averaged_precision(confusion_matrix_imp)
    # macro_avg_F1 = eva.calculate_Macro_averaged_f1_score(confusion_matrix_imp)
    #
    # np.set_printoptions(threshold=sys.maxsize)
    # print("###Test results on decision tree trained by train_predict_method:###\n")
    # print("Confusion Matrix: \n{}".format(confusion_matrix_imp))
    # print(f"Accuracy: {accuracy_imp}")
    # print("Recall: {}".format(recall_imp))
    # print("Precision: {}".format(precision_imp))
    # print("F1 score: {}".format(F1_imp))
    # print(f"Macro-averaged recall: {macro_avg_recall_imp}")
    # print(f"Macro-averaged precision: {macro_avg_precision_imp}")
    # print(f"Macro-averaged F1 score: {macro_avg_F1}")
    # ------------------------------------------------------------------------------------------------------------------
