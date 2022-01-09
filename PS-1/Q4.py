import statistics
from scipy.stats import skew
heights= [167.65, 167, 172, 175, 165, 167, 168, 167, 167.3, 170, 167.5, 170, 167, 169, 172]
print("Mean height : "+str(statistics.mean(heights)))
print("Median : "+str(statistics.median(heights)))
print("Mode : "+str(statistics.mode(heights)))
print("Standard Deviation : "+str(statistics.pstdev(heights)))
print("Skewness : "+str(skew(heights)))