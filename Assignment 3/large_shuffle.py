# Given a number, find the largest number by shuffling the digits

def compute_large_shuffle(s):
    a=str(s)
    ls=[]
    for i in range(len(a)):
        ls.append(a[i:-1]+a[:i])