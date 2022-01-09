import matplotlib.pyplot as plt

data = {"Studying" : 33,'Sleeping' : 30,'Playing' : 18,'Hobby Activities' : 5}
data['Spending with Family and Friends'] = 100 - sum(list(data.values()))
plt.pie(list(data.values()),labels = list(data.keys()),autopct='%1.1f%%')
plt.title("Pie graph of activities")
plt.show()