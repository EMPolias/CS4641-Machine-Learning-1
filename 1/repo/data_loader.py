import os
import numpy as np

def load_data():
	FILE = 'data.csv'
	print "Loading the dataset..."
	data = np.genfromtxt(FILE, delimiter=',')
	print "Dataset of size:\t"
	print data.shape
	return data

def debug_data():
	data = load_data()
	print data[0,0:]

if __name__ == '__main__':
	debug_data()
