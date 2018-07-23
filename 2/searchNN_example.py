import numpy as np
import tflearn
import tensorflow as tf
from tflearn import conv_2d, max_pool_2d, local_response_normalization, batch_normalization, fully_connected, regression, input_data, dropout, custom_layer, flatten, reshape, embedding,conv_2d_transpose


#DATA
X = [[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0],[0,1,0,0,0],[1,0,0,0,0],

	[1,1,0,0,0],[1,0,1,0,0],[1,0,0,1,0],[1,0,0,0,1],[0,1,1,0,0],
	[0,1,0,1,0],[0,1,0,0,1],[0,0,1,0,1],[0,0,1,1,0],[0,0,0,1,1],

	[1,1,1,0,0],[1,1,0,1,0],[1,1,0,0,1],[1,0,1,1,0],[1,0,1,0,1],
	[0,1,1,1,0],[0,1,1,0,1],[0,1,0,1,1],[0,0,1,1,1],

	[1,0,1,1,1],[1,1,1,0,1],[1,1,0,1,1],[1,1,1,1,0],[0,1,1,1,1],
	[1,1,1,1,1]]

Y = [[1,0],[1,0],[1,0],[1,0],[1,0],
	[0,1],[0,1],[0,1],[0,1],[0,1],
	[0,1],[0,1],[0,1],[0,1],[0,1],
	[1,0],[1,0],[1,0],[1,0],[1,0],
	[1,0],[1,0],[1,0],[1,0],[0,1],
	[0,1],[0,1],[0,1],[0,1],[1,0]]

X = np.array(X)
Y = np.array(Y)

def heuristic(model,X,Y):
	predY = model.predict(X)
	score = 0
	for i in range(0, len(predY)):
		maxVal = max(predY[i])
  		maxIndex = list(predY[i]).index(maxVal)

  		trueIndex = list(Y[i]).index(1)
  		if maxIndex==trueIndex:
  			score+=1
  	return score

def getRandomNeighbor(weights):
	neighbor =np.copy(weights)
	for i in range(0, 5): #CHANGE ME
		neighbor[np.random.randint(0,5)][np.random.randint(0,2)]= np.random.random_sample()
	return neighbor

#DEFINE AN ARCHITECTURE
networkInput = tflearn.input_data(shape=[None, 5])#Input
fc = tflearn.fully_connected(networkInput, 2, activation='leaky_relu')
network = tflearn.regression(fc, optimizer='adam', loss='categorical_crossentropy')
model = tflearn.DNN(network)

currScore = heuristic(model,X,Y)
currWeights = model.get_weights(fc.W)
prevScore = -100#arbitrary

while prevScore<currScore:
	print ("while loop")
	prevScore = currScore
	for i in range(0, 20):#CHANGE ME
		n = getRandomNeighbor(currWeights)
		model.set_weights(fc.W, n)
		nScore = heuristic(model,X,Y)
		if nScore>currScore:
			currWeights = n
			currScore = nScore

print ("")
print ("Curr Score: "+str(currScore))