# Fibonacci sequence

def compute_fibonacci(n):
    sum=1
    x=1
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:    

        for i in range(3,n+1):
            val=x
            x=sum
            sum+=val
        return sum
            