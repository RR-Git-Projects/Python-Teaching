#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Plotting.py shows how to import modules and make plots in python.
#
#  Created by Robert Radloff, 2025-03-03
#  Last edit: 2025-03-03
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Import some libraries.
import numpy
#import matplotlib.pyplot as plotter

# Print some constants from numpy.
#print(numpy.pi)
#print(numpy.e)

# Make an array of numbers from 0 to 10 with a step size of 0.1.
#xvals = numpy.arange(0, 10, 0.1)

# Make new arrays that contain the sin and cos values of the original xvals array.
#yvals_1 = numpy.sin(xvals)
#yvals_2 = numpy.cos(xvals)

# Create plot objects for the two sets of x and y values.
#plotter.scatter(xvals, yvals_1, label="Set 1", marker='.')
#plotter.plot(xvals, yvals_1, label="Set 1", marker='.', linestyle='-')
#plotter.plot(xvals, yvals_2, label="Set 2", marker='x', linestyle='--')

# Add the finishing touches to fill out the plot display.
#plotter.title("Plotting Example")
#plotter.xlabel("X Values")
#plotter.ylabel("Y Values")
#plotter.grid(True)
#plotter.legend()

plotter.show()

print("")
print("Done!")