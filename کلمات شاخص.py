from collections import OrderedDict
mylist = []
mylist1 = []
mydict = OrderedDict() 
n = input().split(" ")
mylist.append(n)
for word in mylist:
    for x in word:
        mydict[x] = word.index(x)+1
    print(mydict)