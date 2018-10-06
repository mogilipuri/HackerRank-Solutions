def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        j=string[i:i+k]
        g=[]
        for h in j:
            if h not in g:
                g.append(h)
        print("".join(g))
