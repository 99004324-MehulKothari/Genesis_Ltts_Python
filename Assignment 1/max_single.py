# Maximum number by deleting single digit in a 4 digit number

def compute_max_single(n):
    a=str(n)
    b=list(a)
    c=int(b[0]+b[1]+b[2])
    d=int(b[1]+b[2]+b[3])
    e=int(b[0]+b[2]+b[3])
    f=int(b[0]+b[1]+b[3])
    return max(c,d,e,f)
