def count_substring(string, sub_string):
    count=0
    x=0
    l=len(sub_string)
    for i in string:
        x=x+1
        if i==sub_string[0]:
            y=string[x-1:x+l-1]
            if y==sub_string:
                count=count+1
    return count
