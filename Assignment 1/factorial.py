# Factorial of a given number

def compute_fact(n):
    if (n<0):
        return -1
    elif (n<=1):
        return 1
    else:
        return n*compute_fact(n-1)