# Given a number, find the largest number by shuffling the digits

def compute_large_shuffle(s):
    a=list(map(int,str(s)))
    b=list(map(int,a))
    d=sorted(b,reverse=True)
    c=''
    for i in d:
        c+=str(i)
    return int(c)

    