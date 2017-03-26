""" -Take what you did on homework 5 as a starting point (using any of the provided datasets).
    Replace the regression calculation using least squares with a curve fitting approach (examples in the reading).
    To start, just fit a linear equation.  Output the equation to the console.
    You don't need to graph anything (we'll look at that in a couple more weeks).

    -Again, using timeit, compare the performance of your solution in homework 5 to the scipy function.
    Output the results to the console.

    -(Optional)  There are other models that can be fitted to the data we have.
    Try to fit other equations, like Gaussian, to the data.  Output the equation to the console.
    """


import timeit

#HW 5 approach

s = """\
import csv
import urllib2


# Load csv file
response = urllib2.urlopen('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/brainandbody.csv')
brainbody = csv.reader(response)
next(brainbody, None)  # skip the headers
brainbody = list(csv.reader(response))


# Let's assume brain is independent variable 'x' and body is dependent variable 'y'

# To Solve the problem we will use the formula, PREDICTED y = a + bx, where 'b' is the slope and 'a' is the intercept 


x_values = [float(i[2]) for i in brainbody]
y_values = [float(i[1]) for i in brainbody]
# Sum of 'x' values
x_sum = sum(x_values)


# Sum of 'y' values
y_sum = sum(y_values)


# Average of 'x' values    
x_ave = x_sum*1.0/(len(x_values))


# Average of 'y' values
y_ave = y_sum*1.0/(len(y_values))


# 'x' values minus average of 'x' values
xMin = [float(i[2]) - x_ave for i in brainbody]


# 'y' values minus average of 'y' values
yMin = [float(i[1]) - y_ave for i in brainbody]


# 'x' minus 'x squred'
xMinSq = [(float(i[2]) - x_ave)**2 for i in brainbody]


# 'x' values minus average of 'x' values multiplied by 'y' values minus average of 'y' values
xy = [((float(i[2])-x_ave) * (float(i[1])-y_ave)) for i in brainbody]


# Calculate slope or b
b = sum(xy)/sum(xMinSq)
print 'Slope = ', (round(b,3))


# Calculate intercept or a
a = y_ave- b* x_ave
print 'Intercept = ', (round(a,3))

print 'the model is,', 'bo =', (round(b,3)), '*br +', (round(a,3))
print 'Total time taken form loading the file to getting the model:'
"""

print 'Using python builtin functions:'
print ''.center(75, '-')
t = timeit.Timer(stmt=s)
print  t.timeit(1) , 'seconds'

# Using scipy curve fitting

s = """\
import csv
import urllib2
import numpy as np
from scipy.optimize import curve_fit
response = urllib2.urlopen('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/brainandbody.csv')
brainbody = csv.reader(response)
next(brainbody, None)
brainbody = list(csv.reader(response))

x = [float(i[2]) for i in brainbody]
y = [float(i[1]) for i in brainbody]
# Creating a function to model and create data
def func(x, a, b):
    return a * x + b

# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))

# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)

# popt returns the best fit values for parameters of

# the given model (func).
print 'the model is,','bo = %s * br + %s' % ((round(popt[0],3)), (round(popt[1],3)))

print 'Total time taken form loading the file to getting the model:'
"""
print ''
print 'Using scipy curve fitting approach:'
print ''.center(75, '-')
t = timeit.Timer(stmt=s)
print t.timeit(1), 'seconds'


# Gaussian model

import csv
import urllib2
import numpy as np
from scipy.optimize import curve_fit

response = urllib2.urlopen('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/brainandbody.csv')
brainbody = csv.reader(response)
next(brainbody, None)
brainbody = list(csv.reader(response))

x = [float(i[2]) for i in brainbody]
y = [float(i[1]) for i in brainbody]
def func(x, a, b, c):
    return  a*np.exp(-(x-b)**2/(2*c**2))

# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))

# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)

print ''
print "The Gaussian model is: bo = (%f) * np.exp(-(br - (%f))**2/(2 * (%f) **2))" % (popt[0], popt[1], popt[2])
             
#The Homework would have been easier if I had used function approach in HW5
