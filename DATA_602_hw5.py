import csv
import urllib2

# Load csv file
response = urllib2.urlopen('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/brainandbody.csv')
brainbody = csv.reader(response)
next(brainbody, None)  # skip the headers
brainbody = list(csv.reader(response))


# Let's assume brain is independent variable 'x' and body is dependent variable 'y'

# To Solve the problem we will use the formula, PREDICTED y = a + bx, where 'b' is the slope and 'a' is the intercept 

# Sum of 'x' values
x_values = [float(i[2]) for i in brainbody]
x_sum = sum(x_values)


# Sum of 'y' values
y_values = [float(i[1]) for i in brainbody]
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

