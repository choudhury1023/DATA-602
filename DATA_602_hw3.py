import Tkinter
import tkFileDialog
import pandas as pd


root= Tkinter.Tk()
root.withdraw() # This prevents the root GUI box from appearing
filename= tkFileDialog.askopenfilename(parent=root) # Shows a 'open' dialog box to select file
print filename
try: #error handling in case wrong input selected
    cars = pd.read_csv(filename)
    cars.columns = ["buying", "maint","doors","seats","cargo","safety","accept"]
except:
    print 'Needs cars.data.csv to execute', '\n'
            
def safetyFun(row):  #create a function to give safety column numeric values for sorting purposes
    if row['safety'] == 'low':
        return 1
    elif row['safety'] == 'med':
        return 2 
    elif row['safety'] =='high':
        return 3
    else:
        return 'NA'

cars['safetyScore'] = cars.apply(safetyFun, axis=1)

print "Top 10 rows of the dataset sorted by 'safety' in descending order:"

print cars.sort_values(by="safetyScore", ascending = False).head(10)

def maintFun(row): #create a function to give maint column numeric values for sorting purposes
    if row['maint'] == 'low':
        return 1
    elif row['maint'] == 'med':
        return 2 
    elif row['maint'] =='high':
        return 3
    elif row['maint'] =='vhigh':
        return 4
    else:
        return 'NA'

cars['maintScore'] = cars.apply(maintFun, axis=1)

print "Bottom 15 rows of the dataset sorted by 'maint' in ascending order:"

print cars.sort_values(by="maintScore", ascending = True).tail(15)

print "All rows that are high or vhigh in fields 'buying', 'maint', and 'safety', sorted by 'doors' in ascending order:"

print cars[
    (cars.buying.str.extract('(vhigh|high)').str.len() > 0) & 
    (cars.maint.str.extract('(vhigh|high)').str.len() > 0) &
    (cars.safety.str.extract('(vhigh|high)').str.len() > 0)].sort_values(by="doors", ascending = True)
    
print "Saving to a file all rows that are: 'buying': vhigh, 'maint': med, 'doors': 4, and 'seats': 4 or more."
print "File has been saved as 'output.txt' in the current directory"

subset = cars.query('buying == "vhigh" and maint == "med" and doors == "4" and (seats == "4" or seats == "more")')
print subset

subset.to_csv('output.txt')
   
