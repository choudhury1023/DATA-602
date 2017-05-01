import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import scipy.ndimage as ndimage
import scipy.misc as misc
import urllib
import cv2



cars = pd.read_csv('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/cars.data.csv',
                        names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class'])
print cars.head(5)

# Cars
# Group and count
price_freq = cars.groupby('buying').buying.count()
maint_freq = cars.groupby('maint').maint.count()
safety_freq = cars.groupby('safety').safety.count()
doors_freq = cars.groupby('doors').doors.count()

plt.subplot(221)
price_freq.plot(kind='bar')
plt.title('"Buying" Frequency')
plt.xlabel('Buying')
plt.xticks(rotation='horizontal')

plt.subplot(222)
maint_freq.plot(kind='bar')
plt.title('"Manintenance" Frequency')
plt.xlabel('Maintenance')
plt.xticks(rotation='horizontal')

plt.subplot(223)
safety_freq.plot(kind='bar')
plt.title('"Safety" Frequency')
plt.xlabel('Safety')
plt.xticks(rotation='horizontal')

plt.subplot(224)
doors_freq.plot(kind='bar')
plt.title('"Doors" Frequency')
plt.xlabel('Doors')
plt.xticks(rotation='horizontal')

plt.subplots_adjust( hspace=0.5)

plt.show()



# Linear Regression

brainbody = pd.read_csv('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/brainandbody.csv')
print brainbody.head(5)

def func(x, a, b):
    return a * x + b

popt, pcov = curve_fit(func, brainbody.brain, brainbody.body)

a = round(popt[0],3)
b = round(popt[1],3)

model = 'Body Weight = %s * Brain Weight + %s' % ((round(popt[0],3)), (round(popt[1],3)))


plt.plot(brainbody.brain, a*brainbody.brain + b, color = 'red')
plt.scatter(brainbody.brain, brainbody.body, alpha = 0.5,)
plt.title('Brain Weight vs. Body Weight, with regression line')
plt.xlabel('Brain Weight')
plt.ylabel('Body Weight')
plt.text(500, 5000, model, color = 'green', horizontalalignment = 'left', fontsize=12)

plt.show()



# Image

def url_to_image(url):
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


url = "https://raw.githubusercontent.com/choudhury1023/DATA-602/master/objects.png"
image = url_to_image(url)
sigma = 2
thres2 = thres(image)
labeled, nr_objects = ndimage.label(thres2)

lbl = list(range(1, nr_objects + 1))
center = ndimage.measurements.center_of_mass(thres2, labeled, lbl)

plt.imshow(image)
plt.scatter([c[1] for c in center], [c[0] for c in center], color = 'red')
plt.title('Center of Objects')
plt.show()



# Change in number of request hour by hour

requests = pd.read_csv('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/epa-http.txt',
                 delim_whitespace=True, header=None,
                 names = ['host', 'date', 'request', 'reply_code', 'bytes'])
print requests.head(5)

requests['hours'] = requests['date'].str[4:6]
num_hours = requests.groupby('hours').hours.count()
df = pd.DataFrame(num_hours)
df['hour'] = df.index
df=df.rename(columns = {'hours':'frequency'})


plt.plot(df.hour, df.frequency, label="Number of Requests")
plt.xlabel("Hour")
plt.ylabel("Number of Requests")
plt.legend()
plt.title('Number of Requests by Hour')

plt.show()

