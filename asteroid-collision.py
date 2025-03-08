<<<<<<< HEAD
import os
from typing import List
class AsteroidSolution:
    def asteroidCollision(self, asteroid: List[int]) -> List[int]:
        stk = []
        for x in asteroid:
            if x>0:
                stk.append(x)
            else:
                while stk and stk[-1]>0 and stk[-1]< -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop
                elif not stk or stk[-1]<0:
                    stk.append(x)
        return stk
        

=======
import os
from typing import List
class AsteroidSolution:
    def asteroidCollision(self, asteroid: List[int]) -> List[int]:
        stk = []
        for x in asteroid:
            if x>0:
                stk.append(x)
            else:
                while stk and stk[-1]>0 and stk[-1]< -x:
                    stk.pop()
                if stk and stk[-1] == -x:
                    stk.pop
                elif not stk or stk[-1]<0:
                    stk.append(x)
        return stk
        

>>>>>>> bea3ef94151ca3d6990b13720d2f7762e5f36c24
