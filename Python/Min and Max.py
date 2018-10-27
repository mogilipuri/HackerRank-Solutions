import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
a1=numpy.array(a)
sum1=numpy.min(a1,axis=1)
print(numpy.max(sum1))



