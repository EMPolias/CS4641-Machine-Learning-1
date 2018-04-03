import numpy as np
import matplotlib.pyplot as plt		# For plotting the data
def plot(accu_list, title, ylim=None):
	# ylim : tuple, shape (ymin, ymax), optional. Defines minimum and maximum yvalues plotted.

	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Iteration")
	plt.ylabel("Accuracy")
	plt.grid()
	x = np.arange(0, len(accu_list), 1)
	plt.plot(x, accu_list,'o-',color="r",label="Accuracy")
	plt.legend(loc="best")

	return plt