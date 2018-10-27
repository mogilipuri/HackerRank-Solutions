import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
a1=numpy.array(a)
sum1=numpy.sum(a1,axis=0)
print(numpy.prod(sum1))



