import pandas as pd
import numpy as np
from pandas import DataFrame
from functools import reduce
from scipy.stats import mode


#Cheat Sheet

#selecting within columns
print(df['Winning Numbers'].iloc[1][2:8])



print(df)
print(df['Winning Numbers'].iloc[0])
type(df['Winning Numbers'].iloc[0][1])
df['Winning Numbers'][5][1]


##########################




#capture all winning numbers from 1/3/20 to 5/19/20 for MEGAMILLIONS

data = pd.read_html('https://www.flalottery.com/site/winningNumberSearch?searchTypeIn=range&gameNameIn=MEGAMILLIONS&singleDateIn=&fromDateIn=01%2F03%2F2020&toDateIn=05%2F19%2F2020&n1In=&n2In=&n3In=&n4In=&n5In=&n6In=&pbIn=&mbIn=&lbIn=&pnIn=&cbIn=&n7In=&n8In=&n9In=&n10In=&n11In=&n12In=&n13In=&n14In=&n15In=&n16In=&n17In=&n18In=&n19In=&n20In=&n21In=&n22In=&n23In=&n24In=&submitForm=Submit')
#neat trick to convert list to dataframe
df = data[0]

#print(df)

#These regex calls replace the 'MB' and the multiplier number seen at the end of the powerball thing
#one before last regex replaces whitespace and hyphens at with comma.
#Last regex removes final comma at end of num list
df['Winning Numbers'] = df['Winning Numbers'].str.replace('[MB]', '')
df['Winning Numbers'] = df['Winning Numbers'].str.replace('x\d+', '')
df['Winning Numbers'] = df['Winning Numbers'].str.replace(r'\W+', ',')
df['Winning Numbers'] = df['Winning Numbers'].str.replace(r'([^\w\s]|_)+(?=\s|$)', '')
#print(df)
#Problem occurs here, all characters are considered string and not a list
#converting elements of winning numbers to an array because it is currently a massive string of numbers and commas
#research ways to iterate through the list without needing for loop (lambda maybe??)
all = []
mini = []
maxi = []
for i in range(len(df['Winning Numbers'])):
    df['Winning Numbers'][i] = np.array(df['Winning Numbers'][i].split(','),int)
    df['Winning Numbers'][i] = df['Winning Numbers'][i].tolist()
    #Now we find max values in all of the arrays
    indmax = np.argmax(df['Winning Numbers'][i])
    maxi.append(df['Winning Numbers'][i][indmax])
    #and the min values
    indmin = np.argmin(df['Winning Numbers'][i])
    mini.append(df['Winning Numbers'][i][indmin])
    #and finally we capture all numbers into a huge list for analysis



np.bincount(maxi).argmax()
np.bincount(mini).argmin()
print(all)

type(df['Winning Numbers'][1])
print(df['Winning Numbers'])
