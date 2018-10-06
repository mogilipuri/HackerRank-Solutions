def swap_case(s):
    count=0
    for i in s:
        count=count+1
        if count==1:
            if s[count-1].islower()==True:
                s=s[count-1].upper()+s[count:]
            else:
                s=s[count-1].lower()+s[count:]
        else:
            if s[count-1].islower()==True:
                s=s[:count-1]+s[count-1].upper()+s[count:]
            else:
                s=s[:count-1]+s[count-1].lower()+s[count:]
    return s
