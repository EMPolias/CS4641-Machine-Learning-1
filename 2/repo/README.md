# Supervised Learning Report
## COMP4641 Assignment #2

This is the Georgia Tech CS 4641 Machine Learning Assignment #2.
4 Optimization Algorithms: Random Hill Climbing (RHC), Simulated Annealing (SA), Genetic Algorithm (GA), and Mutual-Information-Maximizing Input Clustering (MIMIC) are tested out on 4 problems.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### What things you need to install

*  MATLAB R2013a
*  ABAGAIL

### Where to get the data

The whole data set, and the test and train data set are available in the "data" folder:

*  cancer.csv : contains the whole data set
*  cancertest.csv : is the validation/test data set
*  cancertrain.csv : is the training data set
*  cancertrain-1.csv : a subset of the training set, for variation of 2 fold cv
*  cancertrain-2.csv : a subset of the training set, for variation of 2 fold cv

## Running the program

### MATLAB

**Neural Networks Only**

To run the code for determining optimal weights for neural networks, set MATLAB\nnet directory as the working directory,and run

*  gannet.m : for genetic algorithm
*  hillnnet.m : for randomized hill search
*  sannet2.m : for simulated annealing
*  backpropnnet.m : for back propagation

### ABAGAIL

There are three problems: "traveling_salesman", "four_peaks", "flip_flop"
To run the code for each problem, go to ABAGAIL folder and run command:
	'sh run_[problem name].sh'
Or call the following command to run all problems one by one (this may take a long time):
	'sh run.sh'


## Author
**LIU Qinhan** - [qliuan](https://github.com/qliuan)
(qliu359@gatech.edu, qliuan@connect.ust.hk)
