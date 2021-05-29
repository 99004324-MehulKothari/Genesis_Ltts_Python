# Convert ip address from "a.b.c.d" format into integer and vice versa


def compute_ip(s):
    
    a=s.split('.')
    b="".join(a)
    c=int(b)
    return c

    