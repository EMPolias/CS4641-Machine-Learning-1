import sys
import numpy as np
import random
import data_loader
#from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier	# For Support Vector Machine
import learning_curve
import timer

EPISODE_NUM = 10
TITLE = "Learning Curve (K-Nearest Neighbor)"
N_NEIGHBORS = [1,2,3,5,7,10,20,30,50]

def k_nearest_neighbor(dataset):
	numOfFeature = dataset.shape[1]-1
	X = dataset[:,0:numOfFeature]
	y = dataset[:,numOfFeature]
	X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=EPISODE_NUM)

	for n_nei in N_NEIGHBORS:
		print "\nN_Neighbors: " + str(n_nei)
		# model = KNeighborClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=1, **kwargs)
		model = KNeighborsClassifier(n_neighbors=n_nei)

		start_time = timer.start()	# Set the timer
		fit_model(model,X_train,y_train,X_test,y_test)
		timer.end(start_time)		# End

		# score_model(model,X,y)
		# learning_curve.learn_cur(model,TITLE,X,y)

def score_model(model,X,y):
	cv_scores = cross_val_score(model,X,y,cv=EPISODE_NUM)
	print "Cross Validation Scores:"
	print cv_scores


def fit_model(model,X_train,y_train,X_test,y_test):
	print "Training size:\t"
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
	k_nearest_neighbor(dataset)