#!/usr/bin/python3.8
from collections import Counter
class countOccur :
#global
    #list1=[10,10,20,20,20,40,40,40,40,40,40]
   # l=len(list1)
    print("\nEntering the count method\n")
    def countNum(self,list1,l):
        self.list1=list1
        self.l=l
        for i in range(0,l) :
           y= Counter(list1)

        print(y)
           # print(list1[i] ,"\n Initially\n")
        # print(list1.count(i),list1[i])




co=countOccur()
list1=[10,10,10,20,20,20,20,20,30,40,40,40,30]
l=len(list1)
co.countNum(list1,l)