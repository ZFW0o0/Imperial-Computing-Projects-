#############################################################################
# Introduction to Machine Learning
# Coursework 1 Skeleton code
# Prepared by: Josiah Wang
#
# Your tasks: Complete the fit() and predict() methods of DecisionTreeClassifier.
# You are free to add any other methods as needed. 
##############################################################################

import numpy as np
import tree_functions as tf
import early_stop as es


class DecisionTreeClassifier(object):
    """ Basic decision tree classifier
    
    Attributes:
    is_trained (bool): Keeps track of whether the classifier has been trained
    
    Methods:
    fit(x, y): Constructs a decision tree from data X and label y
    predict(x): Predicts the class label of samples X
    prune(x_val, y_val): Post-prunes the decision tree
    """

    def __init__(self):
        self.decision_tree = None
        self.is_trained = False

    def fit(self, x, y):
        """ Constructs a decision tree classifier from data
        
        Args:
        x (numpy.ndarray): Instances, numpy array of shape (N, K) 
                           N is the number of instances
                           K is the number of attributes
        y (numpy.ndarray): Class labels, numpy array of shape (N, )
                           Each element in y is a str 
        """

        # Make sure that x and y have the same number of instances
        assert x.shape[0] == len(y), \
            "Training failed. x and y must have the same number of instances."

        #######################################################################
        #                 ** TASK 2.1: COMPLETE THIS METHOD **
        #######################################################################
        self.decision_tree = tf.build_tree(x, y)

        # set a flag so that we know that the classifier has been trained
        self.is_trained = True

    def predict(self, x):
        """ Predicts a set of samples using the trained DecisionTreeClassifier.
        
        Assumes that the DecisionTreeClassifier has already been trained.
        
        Args:
        x (numpy.ndarray): Instances, numpy array of shape (M, K) 
                           M is the number of test instances
                           K is the number of attributes
        
        Returns:
        numpy.ndarray: A numpy array of shape (M, ) containing the predicted
                       class label for each instance in x
        """

        # make sure that the classifier has been trained before predicting
        if not self.is_trained:
            raise Exception("DecisionTreeClassifier has not yet been trained.")

        # set up an empty (M, ) numpy array to store the predicted labels 
        # feel free to change this if needed
        predictions = np.zeros((x.shape[0],), dtype=np.object)

        #######################################################################
        #                 ** TASK 2.2: COMPLETE THIS METHOD **
        #######################################################################
        for i in range(np.size(x, 0)):
            predictions[i] = tf.make_predict(x[i, :], self.decision_tree)

        # remember to change this if you rename the variable
        return predictions


class DecisionTreeClassifierES(DecisionTreeClassifier):
    def __init__(self):
        super().__init__()

    def fit_early_stop(self, x, y, early_stop=0, stop_value=0):
        """ Constructs a decision tree classifier from data

        Args:
        x (numpy.ndarray): Instances, numpy array of shape (N, K)
                           N is the number of instances
                           K is the number of attributes
        y (numpy.ndarray): Class labels, numpy array of shape (N, )
                           Each element in y is a str
        """

        # Make sure that x and y have the same number of instances
        assert x.shape[0] == len(y), \
            "Training failed. x and y must have the same number of instances."

        if early_stop == 1:
            self.decision_tree = es.build_tree_early_stop_by_entropy(x, y, stop_value)
        elif early_stop == 2:
            self.decision_tree = es.build_tree_early_stop_by_percentage(x, y, stop_value)
        elif early_stop == 3:
            self.decision_tree = es.build_tree_early_stop_by_depth(x, y, stop_value)
        else:
            self.decision_tree = tf.build_tree(x, y)

        # set a flag so that we know that the classifier has been trained
        self.is_trained = True
