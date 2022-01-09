import pandas as pd
import statistics
import collections
grades=['S','A','B','C','D','E','F']
df = pd.read_excel('./SampleGrader.xlsx')
print("DataSet : ")
print(df.to_string(index=False),end="\n\n")
def grade(marks,avg):
    if marks>=90:
        return "S"
    elif marks>=80:
        return "A"
    elif marks>=70:
        return "B"
    elif marks>=60:
        return "C"
    elif marks>=50:
        return "D"
    elif marks>=0.5*avg:
        return "E"
    else:
        return "F"

average = (statistics.mean(df['Total Marks'].tolist()))
rollist = df['Roll No'].tolist()
gradelist=[]
for i in range(len(rollist)):
    gradelist.append(grade(df['Total Marks'][i],average))
df['Grade'] = gradelist
frequencyDict = collections.Counter(gradelist)
table = pd.DataFrame.from_dict({'Grade' : frequencyDict.keys() , 'Frequency' : frequencyDict.values()})
print('Table with grades')
print(df.to_string(index=False),end="\n\n")
for i in grades:
    if (i not in gradelist):
        table.loc[len(table.index)] = [i,0]

print('Grades and their count')
print(table.to_string(index=False))




