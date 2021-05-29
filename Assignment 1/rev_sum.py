# Reverse the number, sum of digits

def reverse(n):
    a=str(n)
    b=a[::-1]
    return int(b)

def sum_n(n):
    return sum([int(i) for i in list(map(int,str(n)))])