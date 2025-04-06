## Checking the odd occurence in an array
import random
class Oddoccurence:
    a1=[]
    
    def solution(self, a1):
        unmatched= set()
        for elements in a1:
            try:
                unmatched.remove(elements)
            except KeyError:
                unmatched.add(elements)
            return unmatched.pop()
ega= Oddoccurence()
x=[1,2,1,3,2,3,9]
y=ega.solution(x)
print(y)