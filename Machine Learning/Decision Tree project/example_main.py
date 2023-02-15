##############################################################################
# Introduction to Machine Learning
# Coursework 1 example execution code
# Prepared by: Josiah Wang
##############################################################################

import numpy as np

from classification import DecisionTreeClassifier
from improvement import train_and_predict
from read_data import read_data
if __name__ == "__main__":
       
    print("Loading the training dataset...");
    x = np.array([
            [5,7,1],
            [4,6,2],
            [4,6,3], 
            [1,3,1], 
            [2,1,2], 
            [5,2,6]
        ])
    
    y = np.array(["A", "A", "A", "C", "C", "C"])
    attributes_data, label_data = read_data("data/train_full.txt")
    print("Training the decision tree...")
    classifier = DecisionTreeClassifier()
    classifier.fit(attributes_data, label_data)

    print("Loading the test set...")
    
    x_test = np.array([
                [1,6,3], 
                [0,5,5], 
                [1,5,0], 
                [2,4,2]
            ])
    
    y_test = np.array(["A", "A", "C", "C"])
    attributes_data_test, label_data_test = read_data("data/validation.txt")
    print("Making predictions on the test set...")
    predictions = classifier.predict(attributes_data_test)
    print("Predictions: {}".format(predictions))
    count = 0
    for i in range (np.size(predictions)):
    	if predictions[i]!=label_data_test[i]:
    		count=count+1
    print(count)
    x_val = np.array([
                [6,7,2],
                [3,1,3]
            ])
    y_val = np.array(["A", "C"])
                   
    print("Training the improved decision tree, and making predictions on the test set...")
    predictions = train_and_predict(x, y, x_test, x_val, y_val)
    print("Predictions: {}".format(predictions))
    
