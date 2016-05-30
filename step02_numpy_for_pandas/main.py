import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.dtype)
print(type(a))
print(np.size(a))

# NumPy will try to coerce all the items to the same type.
a2 = np.array([1, 2.2, 3, 4, 5])
print(a2)
print(a2.dtype)
print(type(a2))
print(np.size(a2))


# shorthand to repeat a sequence 10 times
a3 = np.array([2]*10)
print(a3)


# convert a python range to numpy array
a4 = np.array(range(5))
print(a4)

# To efficiently create an array of a specific size that is initialized with zeros
a5 = np.zeros(5)
print(a5)
print(a5.dtype)

# with types
a6 = np.zeros(3, dtype=int)
print(a6)
print(a6.dtype)

#using numpy arange
a7 = np.arange(5, 10)
print(a7)

a8 = np.arange(0, 10)
a9 = a8 * 2 # multiply a array
print(a9)

a10 = np.array([1, 2, 3])
a11 = np.array([4, 5, 6])
a12 = a10 + a11 #add two arrays
print(a12)

a13 = np.array([[1, 2, 3], [4, 5, 6]]) #two dimensional array
print(a13)
print(a13[0, 2]) #accessing two dimentionsional array
print(a13[0,]) #accessing a entire row
print(a13[:,1])#accessing a entire column

b = np.array([1, 2, 3, 4, 5])
print(b.mean())
print(b.max())
print(b.min())
print(b.std())