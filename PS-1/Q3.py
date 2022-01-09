import statistics
import random

x_axis = random.sample(range(6,100),20)
y_axis = [2*i+3 for i in x_axis]
print("X-axis : ")
print(x_axis,end="\n\n")
print("DataSet(Y-axis) : ")
print(y_axis,end="\n\n")
print("Standard Deviation : "+str(statistics.pstdev(y_axis)))