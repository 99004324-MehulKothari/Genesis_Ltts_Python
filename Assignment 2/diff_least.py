# Find the difference between two lowest numbers in the list

def compute_diff_least(ls):
    d=set(ls)
    a=min(d)
    d.remove(a)
    c=min(d)
    return c-a