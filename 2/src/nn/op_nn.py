import sys
import numpy as np
import data_loader
#from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier	# For Neural Network
import matplotlib.pyplot as plt		# For plotting the data
from random import randrange
import plot_accu

FILE = "cancer.csv"
EPISODE_NUM = 10
iterNum = 20
nodeStep = 3
layerStep = 2

class Neural_Network:
	para = [10,10] # nodes,layers
	X = y = X_train = X_test = y_train = y_test = None # store the data

	def __init__(self,dataset):
		self.prepare_data(dataset)

	def prepare_data(self,dataset):
		print "Preparing the data..."
		numOfFeature = dataset.shape[1]-1
		X = dataset[:,0:numOfFeature]
		self.y = dataset[:,numOfFeature]
		self.X = preprocess_data(X)
		self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y, random_state=EPISODE_NUM)

	def evaluate(self,curr_accu,new_para):
		archi = new_para if new_para != None else self.para
		print "Archi to be evaluated: ", archi
		model = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto',
			beta_1=0.9, beta_2=0.999, early_stopping=False,
			epsilon=1e-08, hidden_layer_sizes=(archi[0],archi[1]), learning_rate='constant',
			learning_rate_init=0.01, max_iter=200, momentum=0.9,
			nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
			solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
			warm_start=False)
		fit_model(model,self.X_train,self.y_train,self.X_test,self.y_test)
		cv_scores = score_model(model,self.X,self.y)
		accu = cv_scores.mean()
		if (curr_accu != None and accu > curr_accu):
			self.para = new_para

		# print "Previous Accuracy: ", curr_accu
		# print "New Accuracy: ", accu

		return accu if accu>curr_accu else curr_accu

	def random_vary_para(self):
		new_para = []
		nodes = self.para[0]
		layers = self.para[1]

		node_diff = get_random(nodeStep)
		while ( (nodes+node_diff) <= 0):
			node_diff = get_random(nodeStep)
		new_para.append(nodes+node_diff)

		layer_diff = get_random(layerStep)
		while ( (layers+layer_diff) <= 0):
			layer_diff = get_random(layerStep)
		new_para.append(layers+layer_diff)

		# print "Para: ", self.para
		# print "Diff: ", node_diff, ",", layer_diff
		return new_para


def random_hill_climbing(model, iterNum):
	accu_list = []
	curr_accu = model.evaluate(curr_accu=None,new_para=None)
	accu_list.append(curr_accu)

	for i in range(iterNum):
		new_para = model.random_vary_para()
		curr_accu = model.evaluate(curr_accu,new_para) # pass in current accuracy for comparing and update para
		accu_list.append(curr_accu)

	print accu_list
	plt = plot_accu.plot(accu_list, "RHC Strategy")
	plt.show()

def get_random(range):
	return randrange(-range, range)


def preprocess_data(X):
	scaler = StandardScaler().fit(X)
	return scaler.transform(X)

def score_model(model,X,y):
	cv_scores = cross_val_score(model,X,y,cv=EPISODE_NUM)
	return cv_scores

def fit_model(model,X_train,y_train,X_test,y_test):
	# print "Training size:\t"
	# print X_train.shape[0]
	model.fit(X_train,y_train)
	return

if __name__ == '__main__':
	dataset = data_loader.load_data(FILE)
	nn = Neural_Network(dataset)
	random_hill_climbing(nn,iterNum)
