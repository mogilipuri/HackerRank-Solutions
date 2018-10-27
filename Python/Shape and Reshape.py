import numpy
arr = input().strip().split(' ')
arr = list(map(int, arr))
arr=numpy.array(arr)
arr.shape = (3, 3)
print(arr)



