# A Python program to print all combinations of items in a list, and minimize based on target
#Import
from itertools import combinations
import pandas as pd

#Set your list of numbers and the target value you want to achieve
numbers = [49.07, 122.29, 88.53, 73.02, 43.99]
target = 250

combo_list = []

#Create a list of combinatorial tuples
for i in range(len(numbers)):
    comb=combinations(numbers,i+1)
    combs = list(comb)
    combo_list.extend(combs)

#Create a list of the sums of those tuples
combo_sum = [sum(tup) for tup in combo_list]

#Create a dataframe with them both
df = pd.DataFrame({'Combo': combo_list, 'Sum': combo_sum})
            
#Add a column showing the difference between the target and the sum
df['Difference']=target-df['Sum']

#Remove all rows which go over the target price is right style
df = df[df['Difference']>=0]
df = df.sort_values(by='Difference', ascending=True)

df





