import numpy as np

#creating 2 x 2 array using
a = np.array([np.arange(2), np.arange(2), np.arange(2)])
print(a)
print(a.shape)

#make another 2 x 2 array directly
b = np.array([[1, 2], [3, 4]])
print(b)
print(b.shape)

#size of the data in bytes
print(a.dtype.itemsize)
print(b.dtype.itemsize)

#float type
c = np.arange(2, dtype=np.float)
print(c)
print(b.dtype.itemsize)

#using conversion function
d = np.float(43)
print(d)