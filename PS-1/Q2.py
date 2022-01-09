import pandas as pd

arr=[]
for i in range(1,19):
    if i%2==0:
        arr.append(['CSE20D0'+str(i) , 25+((i+8)%10)]) if int(i/10) == 0 else arr.append(['CSE20D'+str(i) , 25+((i+8)%10)])
    else:
        arr.append(['CSE20D0'+str(i) , 25+((i+7)%10)]) if int(i/10) == 0 else arr.append(['CSE20D'+str(i) , 25+((i+7)%10)])

df = pd.DataFrame(arr,columns=['Roll No','Marks'])

print("Dataset : ")
print(df,end="\n\n")

print("Mean : "+str(df['Marks'].mean()) )
print("Median : "+ str(df['Marks'].median()) )
