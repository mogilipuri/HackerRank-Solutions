l=[]
if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
y=0
l.sort()
l.reverse()
for i in range(0,len(l)):
    if l[i]>l[i+1]:
        y=l[i+1]
        break
print(y)
