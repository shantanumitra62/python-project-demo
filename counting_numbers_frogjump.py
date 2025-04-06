import logging


logging.basicConfig( 
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def solution(X, A):
    logging.DEBUG("hello")
    # my_set=set()
    # for value in range(1, X+1):
    #     my_set.add(value)
    
    # for index in range(0, len(A)):
    A=[1,3,1,4,2,3,5,4]
    X=5
    leaves=set()
    for leaf,count in enumerate(A):
        if leaf<=X:
            leaves.add(leaf)
        if len(leaves)>=X:
            return count
    return 1
        
        
    
    