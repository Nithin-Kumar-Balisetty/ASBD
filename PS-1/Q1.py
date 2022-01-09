import random
import collections
import pandas as pd

testset = random.choices(range(1, 10), k=60)
frequencyDict = collections.Counter(testset)
df= pd.DataFrame.from_dict({'Value' : frequencyDict.keys() , 'Frequency' : frequencyDict.values()})
print("Dataset : ")
print(testset,end="\n\n")
print("Final Result :")
print(df)
