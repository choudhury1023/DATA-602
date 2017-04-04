import scipy.ndimage as ndimage
import scipy.misc as misc
import numpy as np
import urllib
import cv2

 
# OpenCV, NumPy, and urllib
def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urllib.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image

def thres(image):
    image = url_to_image(url)
    cv2.waitKey(0)
    img = ndimage.gaussian_filter(image, sigma)
    thres = img > img.mean()
    return thres

# circles.png 
url = "https://raw.githubusercontent.com/choudhury1023/DATA-602/master/circles.png"
image = url_to_image(url)

# Thresholding
sigma = 1
thres1 = thres(image)
thres1 = image > (image.mean() + 2 * np.sqrt(image.var()))
img1 = misc.imsave('./circles2.png', thres1)
labeled, nr_objects = ndimage.label(thres1)

# Number of objects
print "circle.png".center(55, '#')
print "Number of objects is %d " % nr_objects

# Center of mass
lbl = list(range(1, nr_objects))
center = ndimage.measurements.center_of_mass(thres1, labeled, lbl)
for i in range(0, nr_objects):
    print  "Center points of object", i+1, "is:", center[i-1][0:2]
    

# objecs.png
url = "https://raw.githubusercontent.com/choudhury1023/DATA-602/master/objects.png"
image = url_to_image(url)

# Thresholding
sigma = 2
thres2 = thres(image)
img2 = misc.imsave('./objects2.png', thres2)
labeled, nr_objects = ndimage.label(thres2)

# Number of objects
print ''
print "objects.png".center(55, '#')
print "Number of objects is %d " % nr_objects

# Center of mass
lbl = list(range(1, nr_objects))
center = ndimage.measurements.center_of_mass(thres2, labeled, lbl)
for i in range(0, nr_objects):
    print  "Center points of object", i+1, "is:", center[i-1][0:2]
    

# peppers.png
url = "https://raw.githubusercontent.com/choudhury1023/DATA-602/master/peppers.png"
image = url_to_image(url)

# Thresholding
sigma = 3
thres3 = thres(image)
img3 = misc.imsave('./peppers2.png', thres3)
labeled, nr_objects = ndimage.label(thres3)

# Number of objects
print ''
print "peppers.png".center(55, '#')
print "Number of objects is %d " % nr_objects

# Center of mass
lbl = list(range(1, nr_objects))
center = ndimage.measurements.center_of_mass(thres3, labeled, lbl)
for i in range(0, nr_objects):
    print  "Center points of object", i+1, "is:", center[i-1][0:2]

# Reference
# http://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
# http://stackoverflow.com/questions/5298884/finding-number-of-colored-shapes-from-picture-using-python

