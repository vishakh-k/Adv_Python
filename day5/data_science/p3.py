# ----------------------------
# 📦 IMPORTS
# ----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# 🐼 PANDAS METHODS
# ----------------------------

# Creating DataFrames
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Inspecting Data
print(df.head())
print(df.info())
print(df.describe())

# Selecting Data
print(df['A'])
print(df[['A', 'B']])
print(df.iloc[0])
print(df.loc[0])
print(df[df['A'] > 1])

# Modifying Data
df['C'] = df['A'] + df['B']
df.rename(columns={'A': 'X'}, inplace=True)
df.drop(['C'], axis=1, inplace=True)
df.set_index('X', inplace=True)
df.reset_index(inplace=True)

# Aggregation
print(df.sum())
print(df.mean())
print(df.groupby('B').mean())

# Null Handling
df['D'] = [np.nan, 1, 2]
print(df.isnull())
df.fillna(0, inplace=True)

# Sorting
df.sort_values(by='B', inplace=True)
df.sort_index(inplace=True)

# ----------------------------
# 🔢 NUMPY METHODS
# ----------------------------

# Creating Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.zeros((2, 2))
arr3 = np.ones((3, 3))
arr4 = np.arange(0, 10, 2)
arr5 = np.linspace(0, 1, 5)
arr6 = np.random.rand(2, 2)
arr7 = np.random.randint(1, 10, (2, 3))

# Array Properties
print(arr1.shape)
print(arr3.size)
print(arr3.dtype)

# Array Operations
print(arr1 + 2)
print(arr1 * 3)
print(np.add(arr1, arr1))
print(np.dot(arr3, np.ones((3, 1))))
print(np.mean(arr1))
print(np.std(arr1))
print(np.sum(arr1))
print(np.min(arr1))
print(np.max(arr1))

# Indexing/Slicing
print(arr1[0])
print(arr1[1:3])
print(arr3[:, 1])
print(arr3[1:, ::2])

# Reshaping
reshaped = arr7.reshape(3, 2)
flattened = arr7.flatten()
transposed = arr7.T

# ----------------------------
# 📊 MATPLOTLIB METHODS
# ----------------------------

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Line plot
plt.plot(x,y, label="Line Plot")

# Scatter
plt.scatter(x, y, color='red', label="Scatter")

# Bar plot
#plt.barh(x, y, color="green", label="Bar", alpha=0.5 , )

# Histogram
plt.hist(x, bins=5, label="Histogram")

# Boxplot
plt.boxplot([[1, 2, 5], [2, 3, 4]])

# Pie chart
plt.figure()
plt.pie([25,25,25,25], labels=["A", "B", "C","D",], colors=['white','blue','white','blue'] )

# Labels and Grid
plt.title("Sample Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)

# Show and Save
plt.savefig("plot.png")
plt.show()
