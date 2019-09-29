import pandas as pd
import matplotlib.pyplot as plt

#read the data from csv file
data = pd.read_csv('D:\Python\\births.csv')

#Find the aggregation of max births in a year
value_max_data= data.groupby(["year"],as_index=False).agg({"births":"max"})

#plot with x axis as year and y axis with births
plt.plot(value_max_data["year"],value_max_data["births"])

#Save it as a file
plt.savefig("D:\Python\\test.png")



