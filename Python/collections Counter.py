from collections import Counter 
n=int(input())
l = list(map(int, input().split()))
k=Counter(l)
s=int(input())
sum1=0
for i in range(s):
    j=list(map(int, input().split()))
    if k[j[0]]>0:
        sum1=sum1+j[1]
        k[j[0]]=k[j[0]]-1
print(sum1)
