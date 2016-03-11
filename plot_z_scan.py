#!/usr/bin/env python


""" File: plot_zscan.py
	Author: Sarah Lindner
	Date of last change: 10.11.2015

"""
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import pickle # save plots in pickle format which can be opened in interactive window

current_script, my_file = argv 	# get the arguments from the command line
								# by default, the executing script is also passed to
								# argv; to seperate the inpu filename, the current 
								# script is stored in a dummy variable

my_output = my_file.replace('.txt', '')

print "Plotting file: %r" % my_file


replaced_file = open(my_file, "rw")
replaced_file = (line.replace(",", ".") for line in replaced_file) # replace comma as decimal seperator by dot

xdata, ydata = np.loadtxt( replaced_file, delimiter="\t", unpack=True) 

ax = plt.subplot(111)


plt.plot(xdata, ydata, linestyle = "-", color = 'black')



plt.title(my_output, fontsize = 23)
plt.xlabel('Z-axis (mm)', fontsize = 20)
plt.ylabel('Intensity (a.u.)', fontsize = 20)
plt.tick_params(axis = 'both', labelsize = 15)

axes = plt.gca()
axes.set_xlim([min(xdata),max(xdata)])

plt.tight_layout() # suppress chopping off labels

plt.savefig( (my_output +'.pdf'))

pickle.dump(ax, file((my_output +'.pickle'), 'w'))

# plt.show()
