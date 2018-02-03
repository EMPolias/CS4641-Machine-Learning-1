import os
import sys
import numpy as np

def load_data(FILE):
	print "Loading the dataset " + FILE
	try:
		data = np.genfromtxt(FILE, delimiter=',')
		print "Dataset of size:\t"
		print data.shape
	except:
		print "Please input a correct file name."
		exit()
	return data

def debug_data(FILE):
	data = load_data(FILE)
	print data[0,0:]

if __name__ == '__main__':
	debug_data(sys.argv[1])
