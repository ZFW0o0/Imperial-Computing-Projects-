## Introduction to Machine Learning: Coursework 1 (Decision Trees)

### Introduction

This repository contains the skeleton code and dataset files that you need 
in order to complete the coursework.


### Data

The ``data/`` directory contains the datasets you need for the coursework.

The primary datasets are:
- ``train_full.txt``
- ``train_sub.txt``
- ``train_noisy.txt``
- ``validation.txt``

Some simpler datasets that you may use to help you with implementation or 
debugging:
- ``toy.txt``
- ``simple1.txt``
- ``simple2.txt``

The official test set is ``test.txt``. Please use this dataset sparingly and 
purely to report the results of evaluation. Do not use this to optimise your 
classifier (use ``validation.txt`` for this instead). 


### Codes

- ``classification.py``

	* Contains the skeleton code for the ``DecisionTreeClassifier`` class. Your task 
is to implement the ``train()`` and ``predict()`` methods.


- ``improvement.py``

	* Contains the skeleton code for the ``train_and_predict()`` function (Task 4.1).
Complete this function as an interface to your new/improved decision tree classifier.


- ``example_main.py``

	* Contains an example of how the evaluation script on LabTS might use the classes
and invoke the methods/functions defined in ``classification.py`` and ``improvement.py``.


### Instructions

The codebase is separated into multiple function/class files and scripts to run 
these methods/functions to generate results.

All files that are scripts are named as ``PartX_Code.py`` to distinguish them from 
other files

* ``Part1_Code.py`` - Contains code to generate results relevant to part 1 of the report
and can be run end to end without any changes. Rows 11, 35, and 62 can be updated with different 
``read_data(path_to_file)`` outputs to produce different results.
* ``Part3_Code.py`` - Contains code to generate results relevant to part 3 of the report
and can be run end to end without any changes.
* ``Part4_Code.py`` - Contains code to generate results relevant to part 4 of the report. Parts
of the code should be uncommented as needed to run desired outputs otherwise it may be too time
consuming to run all of it at once. Each portion of the code is separated with a comment line
and ended by a #-----------------.
  - The ``first and second scripts`` are for early depth stop charts and the range of the for loop should be updated
  to reflect whichever early stop function is being run. 1 (entropy), 2 (percentage), 3 (depth). The
  iterator "i" adn titles/axis of the chart may also need to be updated to reflect the function being run.
  - The ``third script`` is used to evaluate the early stop method on ``training_full.txt`` and can be
  run as is.
  - The ``fourth script`` is used to produce the PCA metrics of ``training_full.txt`` and can be run as is.
  - The ``fifth and sixth scripts`` are used to evaluate the ``train_predict()`` method on a training dataset and has
  default parameter ``col_drop_num`` set to 1, which can be updated as needed. The fifth script evaluates on ``training_full.txt``
  and the sixth script evaluates on ``training_noisy.txt``.