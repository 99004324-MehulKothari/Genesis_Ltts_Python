# Generate accumulated strings,e.g. abcd ==> A-Bb-Ccc-Dddd

def compute_accu(s):
    a=list(s)
    c=""
    for i in range(len(a)):
        for j in range(i+1):
            if j==0:
                c+=a[i].upper()
            else:
                c+=a[i]
        c+="-"

    return c[:-1]
            