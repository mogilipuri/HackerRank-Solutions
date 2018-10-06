def wrap(string, max_width):
    x=len(string)
    list1=[]
    count=0
    s=''
    for i in range(0,x,max_width):
        count=count+1
        if count==1: 
            list1.append(string[0:max_width])
        else:
            list1.append(string[i:max_width+i])
    for i in list1:
        if i!=list1[-1]:
            print(i)
        if i==list1[-1]:
            print(i,end="")
    return " "
