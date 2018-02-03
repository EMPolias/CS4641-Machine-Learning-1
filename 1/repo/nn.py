import numpy as np
import random
import data_loader
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier 	# For Neural Network

EPISODE_NUM = 10

def neural_network():
	dataset = data_loader.load_data()
	episodeSize = dataset.shape[0]/EPISODE_NUM
	numOfFeature = dataset.shape[1]-1

	X = dataset[episodeSize:,0:numOfFeature]
	y = dataset[episodeSize:,numOfFeature]
	test = dataset[0:episodeSize,0:numOfFeature]
	target = dataset[0:episodeSize,numOfFeature]

	model = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes = (1000,), learning_rate = 'invscaling' ,max_iter = 1000, alpha = 1e-5)
	fit_model(model,X,y,test,target)
	# score_model(model,X,y)

	# for i in range(EPISODE_NUM):
	# 	numOfTraining = episodeSize*(i+1)
	# 	X = dataset[0:numOfTraining,0:numOfFeature]		# Features
	# 	y = dataset[0:numOfTraining,numOfFeature]		# Target
	# 	test = dataset[episodeSize:,0:numOfFeature]	# Test
	# 	target = dataset[episodeSize:,numOfFeature]	# Target

def score_model(model,X,y):
	cv_errors = cross_val_score(model,X,y,cv=EPISODE_NUM)
	print "Cross Validation Errors:\n"
	print cv_errors


def fit_model(model,X,y,test,target):
	print "Trainning size:\t"
	print X.shape[0]
	model.fit(X,y)
	error = accuracy_score(target,model.predict(test))
	print "Error rate: \t"
	print error
	print type(error)

	return error

def preprocess_feature(X):
	# Preprocess the Features
	scaler = StandardScaler().fit(X)
	X = scaler.transform(X)	# Rescale the data
	return X

if __name__ == '__main__':
	neural_network()