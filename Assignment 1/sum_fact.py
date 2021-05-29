# Sum of the factors
from math import sqrt
def compute_sum_fact(n):
    ls=[1,n]
    if (n<=0):
        return 0
    elif (n==1):
        return 1
    else:  
        for i in range(2,int(sqrt(n))+1):
            if(n%i==0):
                ls.append(i)
                if ((n/i) not in ls):
                    ls.append(n/i)
    return sum(ls)
