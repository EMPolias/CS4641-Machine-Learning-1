import sys
import numpy as np
import random
import data_loader
#from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier	# For Neural Network
import learning_curve

EPISODE_NUM = 10
TITLE = "Learning Curve (Neural Network)"

def neural_network(dataset):
	numOfFeature = dataset.shape[1]-1
	X = dataset[:,0:numOfFeature]
	y = dataset[:,numOfFeature]
	X_train,X_test,y_train,y_test = train_test_split(X,y, random_state=EPISODE_NUM)

	model = MLPClassifier(solver='adam', activation='relu', hidden_layer_sizes = (1000,), learning_rate = 'invscaling' ,max_iter = 1000, alpha = 1e-5)
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

def learn_cur(model, title, X, y, ylim=None, cv=None, n_jobs=1, train_sizes=np.linspace(.1, 1.0, 10)):
								# ylim : tuple, shape (ymin, ymax), optional. Defines minimum and maximum yvalues plotted.

	# Cross validation with 100 iterations to get smoother mean test and train
	# score curves, each time with 20% data randomly selected as a validation set.
	cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Training examples")
	plt.ylabel("Score")
	train_sizes, train_scores, test_scores = learning_curve(
		model, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
	train_scores_mean = np.mean(train_scores, axis=1)
	train_scores_std = np.std(train_scores, axis=1)
	test_scores_mean = np.mean(test_scores, axis=1)
	test_scores_std = np.std(test_scores, axis=1)
	plt.grid()

	plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
					 train_scores_mean + train_scores_std, alpha=0.1,
					 color="r")
	plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
					 test_scores_mean + test_scores_std, alpha=0.1, color="g")
	plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
			 label="Training score")
	plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
			 label="Cross-validation score")

	plt.legend(loc="best")
	plt.show()
	print "Check out the graph popped up"
	return plt

if __name__ == '__main__':
	dataset = data_loader.load_data(sys.argv[1]) # argv[1] is the file storing the dataset
	neural_network(dataset)