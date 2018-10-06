if __name__ == '__main__':
    k=[]
    m=int(input())
    for i in range(0,m):
        l=input("").split()
        if l[0]=='insert':
            k.insert(int(l[1]),int(l[2]))
        elif l[0]=='print':
            print(k)
        elif l[0]=='remove':
            k.remove(int(l[1]))
        elif l[0]=='append':
            k.append(int(l[1]))
        elif l[0]=='sort':
            k.sort()
        elif l[0]=='pop':
            k.pop()
        elif l[0]=='reverse':
            k.reverse()


