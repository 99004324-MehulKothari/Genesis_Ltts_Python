# Correct the malformed time string , for e.g "5:70:65" to "6:11:05"

def compute_time(s):
    b=s.split(":")
    ls=list(map(int,b))
    if(ls[2]>60):
        ls[1]+=int(ls[2]/60)
        ls[2]-=int(ls[2]/60)*60
    if(ls[1]>60):
        ls[0]+=int(ls[1]/60)
        ls[1]-=int(ls[1]/60)*60

    lstr=map(str,ls)
    a=":".join(lstr)
    return a