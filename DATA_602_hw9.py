import urllib
import pandas as pd
import numpy as np
import re



data = urllib.urlopen('https://raw.githubusercontent.com/choudhury1023/DATA-602/master/epa-http.txt')
df = pd.read_csv(data, delim_whitespace=True, header=None,
                 names = ['host', 'date', 'request', 'reply_code', 'bytes'])

# Data cleansing
df['request'] = df['request'].str.rstrip("HTTP/1.0")
df['request'] = df['request'].str.lstrip("GET")
df['reply_code'] = df['reply_code'].str.lstrip("HTTP/1.0")
df['reply_code'] = df['reply_code'].str.replace('"','')


print "Which hostname or IP address made the most requests?"

requests = df['host'].value_counts()[:1]

print "Hostname or IP address \"%s\" requests: %d." % (requests.index[0],requests[0])
print ""
print ""


print "Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive? "

# Replace "-" with 0
df['bytes'] = df['bytes'].replace('-', 0)
# Group by "host"
grouped_host = df.groupby('host')
# Convert "bytes" column to all numeric
df['bytes'] = pd.to_numeric(df['bytes'])
bytes_total = grouped_host['bytes'].aggregate(np.sum).sort_values(ascending=False)

print "Hostname or IP address \"%s\" total bytes: %d." % (bytes_total.index[0],bytes_total[0])
print ""
print ""


print "During what hour was the server the busiest in terms of requests?"

# Add another column with hours only
df['hours'] = df['date'].str[4:6]
# Group by "hours"
grouped_hours = df.groupby('hours')
busiest_hour = df['hours'].value_counts()[:1]

print "Busiest hour is : %s" % (busiest_hour.index[0])
print ""
print ""


print "Which .gif image was downloaded the most during the day?"

# Create new data frame that only contains ".gif" in column "request"
df_gif = df[df['request'].str.contains(".gif") == True]
# Group by ".gif"
grouped_gif = df_gif.groupby('request')
most_downloaded = df_gif['request'].value_counts()[:1]

print "Most downloaded .gif is: %s" % (most_downloaded.index[0])
print ""
print ""


print "What HTTP reply codes were sent other than 200?"

# Create new data frame without "reply_code" 200
df_reply = df[df['reply_code'].str.contains("200") == False]
# Find all unique value in "reply_code" column
unique = df_reply['reply_code'].unique()


print "HTTP reply codes other than 200 are", unique



# Reference
# http://stackoverflow.com/questions/20970279/how-to-do-a-left-right-and-mid-of-a-string-in-a-pandas-dataframe
# http://stackoverflow.com/questions/28679930/how-to-drop-rows-from-pandas-data-frame-that-contains-a-particular-string-in-a-p
# https://chrisalbon.com/python/pandas_list_unique_values_in_column.html
# http://stackoverflow.com/questions/13682044/pandas-dataframe-remove-unwanted-parts-from-strings-in-a-column
