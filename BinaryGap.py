import unittest
class Binary:
    def solutiom(self,n):
        binary_string=str(bin(n))[2:]
        gap=max_gap=0
        for char in binary_string:
            if char=="0":
                gap+=1
            else:
                max_gap=max(gap,max_gap)
                gap=0
        return max_gap
n=int(input("\nEnter the number for which you want to know the binary gap:"))
bina=Binary()
x=bina.solutiom(n)
print(f"the binary gap is:",x)