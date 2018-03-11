# Supervised Learning Report
## COMP4641 Assignment #1

This is the Georgia Tech CS 4641 Machine Learning Assignment #1.
5 Machine Learning models: Decision Tree, Boosting Tree, Neural Networks, Support Vector Machine and K-Nearest Neighbor are analysed on 2 datasets.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
What things you need to install
* [numpy](http://www.numpy.org/) - For data manipulation
* [sklearn](http://scikit-learn.org/stable/) - For building supervised learning models
* [matplotlib](https://matplotlib.org/) - For plotting 2D data

Where to get the data
* [Breast Cancer Data](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data)
This is a set of data about the breast cancer diagnosis, that is, whether the tested cell is of malignant (bad) or benign (mild). 357 benign and 212 malignant samples with 30 features of each sample are included. The features are computed, as described on the website, based on the digitized images of a fine needle aspirate (FNA) of a breast mass. In the training process, the classification is indicated by “1” (malignant) and “0” (benign).

* [Credit Card Fraud Data](https://www.kaggle.com/dalpozz/creditcardfraud/version/2)
 This dataset contains totally 284,807 transactions made  by European cardholders in Sep. 2013. 492 frauds are recorded inside taking up only 0.172% of all transactions. 29 features are included and the fraud transactions are classified by “1”.


## Running the program

Simply call python compiler to run each model program on the desired data file
`python [model_program] [data_file]`
Sample runs:
`python nn.py cancer.csv`
`python svm.py card.csv`

## Author
**LIU Qinhan** - *Built the whole project* - [qliuan](https://github.com/qliuan)
(qliu359@gatech.edu, qliuan@connect.ust.hk)
