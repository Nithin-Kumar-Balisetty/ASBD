#from colorama import Fore, Back, Style
import pandas as pd
import statistics
import collections
grades=['S','A','B','C','D','E','F']
df = pd.read_excel('./SampleGrader.xlsx')
print("DataSet : ")
print(df.to_string(index=False),end="\n\n")

def grade(marks):
    if marks>=s_cutoff:
        return "S"
    elif marks>=a_cutoff:
        return "A"
    elif marks>=b_cutoff:
        return "B"
    elif marks>=c_cutoff:
        return "C"
    elif marks>=d_cutoff:
        return "D"
    elif marks>=e_cutoff:
        return "E"
    else:
        return  "F"

average = (statistics.mean(df['Total Marks'].tolist()))
e_cutoff = int(0.5*average)
pass_total=0 
pass_count =0
for i in df['Total Marks']:
    if(i>=e_cutoff):
        pass_count+=1
        pass_total+=i

pass_mean= int(pass_total/pass_count)
x = pass_mean-e_cutoff
maxmark = max(df['Total Marks'])
s_cutoff= maxmark - 0.1*(maxmark-pass_mean)
y= s_cutoff - pass_mean
a_cutoff = pass_mean + y*(5/8)
b_cutoff = pass_mean + y*(2/8)
c_cutoff = pass_mean - x*(2/8)
d_cutoff = pass_mean - x*(5/8)

rollist = df['Roll No'].tolist()
gradelist=[]
for i in range(len(rollist)):
    gradelist.append(grade(df['Total Marks'][i]))
df['Grade'] = gradelist

print('Table with grades')
print(df.to_string(index=False),end="\n\n")

frequencyDict = collections.Counter(gradelist)
table = pd.DataFrame.from_dict({'Grade' : frequencyDict.keys() , 'Frequency' : frequencyDict.values()})
for i in grades:
    if (i not in gradelist):
        table.loc[len(table.index)] = [i,0]

print('Grades and their count')
print(table.to_string(index=False))





