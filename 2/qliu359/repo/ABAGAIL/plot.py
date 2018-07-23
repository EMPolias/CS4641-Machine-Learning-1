import sys
import numpy as np
from math import log
import matplotlib.pyplot as plt		# For plotting the data

def plot(iter_map, fit_map, time_map, title, ylim=None):
	# ylim : tuple, shape (ymin, ymax), optional. Defines minimum and maximum yvalues plotted.

	# Plotting fit against iteration
	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Iteration")
	plt.ylabel("Fitness")
	plt.grid()
	# x = np.arange(0, len(accu_list), 1)
	plt.plot(iter_map[0], fit_map[0],'o-',color="#ca0020",label="RHC")
	plt.plot(iter_map[1], fit_map[1],'o-',color="#f4a582",label="SA")
	plt.plot(iter_map[2], fit_map[2],'o-',color="#92c5de",label="GA")
	plt.plot(iter_map[3], fit_map[3],'o-',color="#0571b0",label="MIMIC")
	plt.legend(loc="best")

	# Plotting fit against iteration
	plt.figure()
	plt.title(title)
	if ylim is not None:
		plt.ylim(*ylim)
	plt.xlabel("Time")
	plt.ylabel("Fitness")
	plt.grid()
	# x = np.arange(0, len(accu_list), 1)
	plt.plot(time_map[0], fit_map[0],'o-',color="#ca0020",label="RHC")
	plt.plot(time_map[1], fit_map[1],'o-',color="#f4a582",label="SA")
	plt.plot(time_map[2], fit_map[2],'o-',color="#92c5de",label="GA")
	plt.plot(time_map[3], fit_map[3],'o-',color="#0571b0",label="MIMIC")
	plt.legend(loc="best")

	return plt

def parse(file):
	iter_map = []
	fit_map = []
	time_map = []
	rec_list = []
	partCount = 0 # 0: rhc stat, 1: sa stat, 2: ga stat, 3: mimic stat
	with open(file) as stat:
		for i,line in enumerate(stat):
			if "Start" in line:
				rec_list = []
				continue
			if "Time" in line:
				iter_list = []
				fit_list = []
				time_list = []
				for rec in rec_list:
					iter_list.append(rec[0])
					fit_list.append(rec[1])
					time_list.append(rec[2])

				iter_map.append(np.array(iter_list).astype(np.float))
				fit_map.append(np.array(fit_list).astype(np.float))

				time_list = np.array(time_list).astype(np.float)
				# [log(y,10) for y in time_list]
				time_map.append(time_list)
				continue
			try:
				rec_list.append( list(line.rstrip().split(',')))
			except:
				print line

	plt = plot(iter_map, fit_map, time_map, file[:-4])

	plt.show()


if __name__ == '__main__':
	file = 'stat.csv'
	parse(sys.argv[1])
