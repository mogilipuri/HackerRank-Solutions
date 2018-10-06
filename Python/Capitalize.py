def capitalize(string):
    import re
    l=[]
    l=re.split(r"(\s+)",string)
    l2=[]
    for i in l:
        j=i.capitalize()
        l2.append(j)
    str1="".join(l2)
    return str1
