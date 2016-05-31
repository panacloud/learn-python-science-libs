import pandas as pd
import numpy as np

# create scalar series
a = pd.Series(5)
print(a)
print(a[0])

# create with default index
a1 = pd.Series([1, 2, 3, 4, 5])
print(a1)
print(a1.index)
print(a1.values)

# create with a string index type
a2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(a2)
print(a2.index)
print(a2.values)
print(a2["c"])

# index based on already existing index
a3 = pd.Series(2, index=a1.index)
a4 = pd.Series(2, index=a2.index)
print(a3)
print(a4)

# use numpy to create series
np.random.seed(123456)
a5 = pd.Series(np.random.randn(5))
print(a5)

# use numpy array to create series
a6 = pd.Series(np.arange(5, 10))
print(a6)

# create Series from dict
a7 = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(a7)

a8 = pd.Series([0, 1, 1, 2, 3, 4, 5, 6, 7, np.nan])
print(a8)
print(a8.size)
print(a8.count())
a9 = a8.unique()
print(a9.size)
print(a8.value_counts())
