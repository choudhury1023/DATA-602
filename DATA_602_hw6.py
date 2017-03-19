'''
With this assignment, we'll take a look at some of what the numpy module can do.  

Do both of the following:

Using your submission of homework 1 as a base, replace as many of the functions as you can with numpy functions.  For example, instead of using your sort function that you wrote, use numpy.sort.  Refer to here for most of the functions you'll need.   
Using the timeit function measure the execution times of all the sort and search functions you have.  You'll most likely need to do a large number of tests on each one to get a meaningful result.  Something like 10000 or more.  
Your submission will be a single file that has all the functions from homework 1 and the additional approach using numpy.  Additionally, you will have the timing of all the functions output to the console. Something like.

Sort using iteration:  x loops = y seconds
Sort using built in python: x' loops = y' seconds
Sort using numpy: x'' loops  = y''seconds
You fill in all the values for x and y.
'''


import timeit

setup = '''
import numpy
import copy
import random

# Sorting
def sortwithloops(input):
    for i in range (1, len(input)):
        for r in range(i-1, -1, -1):
            if input[r] > input[r+1]:
                input[r], input[r+1] = input[r+1], input[r]
            else:
                break
    return input
	

def sortwithoutloops(input):
    input.sort()
    return input


def sortwithnumpy(input):
    return numpy.sort(input)


# Searching
def searchwithloops(input, value):
    while value in input:
        return "True"
    else:
        return "False"


def searchwithoutloops(input, value):
    output = value in input
    return output


def searchwithnumpy(input, value):
    return value in input


L = [5,3,6,3,13,5,6]
NL = numpy.array(L)

L1 = random.sample(range(1, 10000), 1000) # Generate a dataset of 1000 numbers between 1 and 100000
NL1 = numpy.array(L1);
'''

if __name__ == "__main__":	

    n = 100
    print 'Sort using dataset from week 1'
    print ''.center(75, '-')
    t = timeit.Timer("x=copy.copy(L); sortwithloops(x)", setup=setup)
    print 'Sort using iteration: ', n, 'loops = ',t.timeit(n), 'seconds'
    t = timeit.Timer ("x=copy.copy(L); sortwithoutloops(x)", setup=setup)
    print 'Sort using built in python: ', n, 'loops = ', t.timeit(n), 'seconds' 
    t = timeit.Timer ("x=copy.copy(NL); sortwithnumpy(x)", setup=setup)
    print 'Sort using numpy: ',  n, 'loops = ', t.timeit(n), 'seconds' 

    print ''
    print ''.center(75, '#')
    print ''

    print 'Sort using random 1000 numbers between 1 and 10000'
    print ''.center(75, '-')
    t = timeit.Timer("x=copy.copy(L1); sortwithloops(x)", setup=setup)
    print 'Sort using iteration: ',  n, 'loops = ', t.timeit(n), 'seconds' 
    t = timeit.Timer ("x=copy.copy(L1); sortwithoutloops(x)", setup=setup)
    print 'Sort using built in python: ',  n, 'loops = ', t.timeit(n), 'seconds' 
    t = timeit.Timer ("x=copy.copy(NL1); sortwithnumpy(x)", setup=setup)
    print 'Sort using numpy: ',  n, 'loops = ', t.timeit(n), 'seconds'

    print ''
    print ''.center(75, '#')
    print ''

    print 'Search using dataset from week 1'
    print ''.center(75, '-')
    t = timeit.Timer("x=copy.copy(L); searchwithloops(x,5)", setup=setup)
    print 'Search using iteration: ',  n, 'loops = ', t.timeit(n), 'seconds' 
    t = timeit.Timer ("x=copy.copy(L); searchwithoutloops(x,5)", setup=setup)
    print 'Search using built in python: ',  n, 'loops = ', t.timeit(n), 'seconds'
    t = timeit.Timer ("x=copy.copy(NL); searchwithnumpy(x,5)", setup=setup)
    print 'Search using numpy: ',  n, 'loops = ', t.timeit(n), 'seconds'
    
