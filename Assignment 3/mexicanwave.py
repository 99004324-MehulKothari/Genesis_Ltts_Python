# Given a string, find the mexican wave

def compute_mexicanwave(s):
    ls=[]
    for i in range(len(s)):
        a=s[i].upper()
        ls.append(s[:i]+a+s[i+1:])
    return ls