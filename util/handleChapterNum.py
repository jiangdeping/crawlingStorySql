# -*- coding: utf-8 -*-
#Author:jiang
#2020/10/29 14:03
def handleChaprerNum(list):
    newchaprernum=[]
    last_str=list[len(list)-1]
    first_str=0
    flag=False
    for i in range(len(list)):
        if i<len(list)-1:
            if int(list[i+1])-int(list[i])>1:
                first_str=list[i]
                flag=True
                break
        else:
            newchaprernum=list
    if flag:
        for i in range(int(first_str),int(last_str)+1):
            newchaprernum.append(str(i))
    # if int(first_str)==int(str[])
    return newchaprernum
