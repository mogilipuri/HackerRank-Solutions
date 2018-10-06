if __name__ == '__main__':
    student={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[name]=score
    g=list(student.values())
    g.sort()
    g
    y=0
    for i in range(0,len(g)-1):
        if g[i]<g[i+1]:
            y=g[i+1]
            break
    y
    k=[]
    for i in student:
        if student[i]==y:
            k.append(i)
    k.sort()
    for h in k:
        print(h)
    
