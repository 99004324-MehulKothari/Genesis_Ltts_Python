# Digital root of a given number

def compute_digital_root(n):
    while n>10:
        a=list(map(int,str(n)))
        b=list(map(int,a))
        n=sum(b)
    return n