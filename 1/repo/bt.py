import sys
import numpy as np
import random
import data_loader
#from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier		# For Boosting Decision Tree
from sklearn.metrics import classification_report
import learning_curve

EPISODE_NUM = 10
TITLE = "Learning Curve (Neural Network)"

def boosting_decision_tree(dataset):
	numOfFeature = dataset.shape[1]-1
	X = dataset[:,0:numOfFeature]
	y = dataset[:,numOfFeature]
	X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=EPISODE_NUM)

	model = GradientBoostingClassifier(n_estimators=200, learning_rate=0.1, max_depth=1, random_state=0)
	fit_model(model,X_train,y_train,X_test,y_test)
	class_report(model,X_test,y_test)
	learning_curve.learn_cur(model,TITLE,X,y)

def class_report(model,X_test,y_test):
	# Boosting: many many weak classifiers (max_depth=1) refine themselves sequentially
	# tree is the default the base classifier
	y_pred = model.predict(X_test)
	print(classification_report(y_test, y_pred))


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
	boosting_decision_tree(dataset)