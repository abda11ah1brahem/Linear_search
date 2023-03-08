def linear (nlist,value):
    for i in range (len(nlist)):
        if nlist[i] == value:
            return i
    return -1
list1=[2,3,4,6,8,9,90,65,35,90]
x=35
index=linear(list1,x)
print("index of i =",index)