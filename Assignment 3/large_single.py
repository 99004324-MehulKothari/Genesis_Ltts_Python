# Given a number, find the largest number by deleting single digit

def compute_large_single(s):
    a=str(s)
    ls=[]
    for i in range(len(a)):
        ls.append(int(a[:i]+a[i+1:]))
    return max(ls)