import numpy
n,m,p =map(int,input().split())
a=[]
b=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
for j in range(m):
    k=list(map(int,input().split()))
    b.append(k)
a1=numpy.array(a)
b1=numpy.array(b)
print(numpy.concatenate((a1,b1),axis=0))


