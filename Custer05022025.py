import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn.cluster as sk


df = pd.read_csv("Mall_Customers.csv")

print(df.head())

#Plot 2D
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.show()

#Plot 3d

