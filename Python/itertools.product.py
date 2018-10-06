from itertools import product
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
n=list(product(arr,arr2))
for i in n:
    print(i,end=" ")
