import sys
import numpy as np
import random
import data_loader
#from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC, NuSVC, LinearSVC	# For Support Vector Machine
import learning_curve

EPISODE_NUM = 10
TITLE = "Learning Curve (Neural Network)"

def support_vector_machine(dataset):
	numOfFeature = dataset.shape[1]-1
	X = dataset[:,0:numOfFeature]
	y = dataset[:,numOfFeature]
	X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=EPISODE_NUM)

	# model = LinearSVC(multi_class = 'ovr')
	model = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape='ovr',
		degree=3, gamma='auto', kernel='rbf',max_iter=-1, probability=False, random_state=None,
		shrinking=True,tol=0.001, verbose=False)
	fit_model(model,X_train,y_train,X_test,y_test)
	score_model(model,X,y)
	learning_curve.learn_cur(model,TITLE,X,y)

def score_model(model,X,y):
	cv_scores = cross_val_score(model,X,y,cv=EPISODE_NUM)
	print "Cross Validation Scores:"
	print cv_scores


def fit_model(model,X_train,y_train,X_test,y_test):
	print "Trainning size:\t"
	print X_train.shape[0]
	model.fit(X_train,y_train)
	accu = accuracy_score(y_test,model.predict(X_test))
	print "Accuracy: \t"
	print accu

	return accu

def preprocess_feature(X):
	# Preprocess the Features
	scaler = StandardScaler().fit(X)
	X = scaler.transform(X)	# Rescale the data
	return X


if __name__ == '__main__':
	dataset = data_loader.load_data(sys.argv[1]) # argv[1] is the file storing the dataset
	support_vector_machine(dataset)