import matplotlib.pyplot as plt

data = {'S':31, 'A':0, 'B':29,'C':25}
data['D']=100-sum(list(data.values()))
print(data)
grades = list(data.keys())
values = list(data.values())
plt.bar(grades, values, color ='black')
plt.title("Bar Graph")
plt.show()
plt.pie(values,labels=grades)
plt.title("Pie Graph")
plt.show()


