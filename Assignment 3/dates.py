# Correct the malformed date string , for e.g. "45/8/2018" to "14/9/2018
from Leap_year import leap

def compute_dates(s):
    b=s.split("/")
    ls=list(map(int,b))
    if(ls[1]%2==0 and ls[1]!=8 and ls[1]!=2):
        if(ls[0]>30):
            ls[1]+=int(ls[0]/30)
            ls[0]-=int(ls[0]/30)*30
        if(ls[1]>12):
            ls[2]+=int(ls[1]/12)
            ls[2]-=int(ls[1]/12)*12
    
    elif(ls[1]%2!=0 or ls[1]==8):
        if(ls[0]>31):
            ls[1]+=int(ls[0]/31)
            ls[0]-=int(ls[0]/31)*31
        if(ls[1]>12):
            ls[2]+=int(ls[1]/12)
            ls[2]-=int(ls[1]/12)*12

    else:
        x=leap(ls[2])
        if(x==1):
            if(ls[0]>29):
                ls[1]+=int(ls[0]/29)
                ls[0]-=int(ls[0]/29)*29

            if(ls[1]>12):
                ls[2]+=int(ls[1]/12)
                ls[2]-=int(ls[1]/12)*12

        else:
            if(ls[0]>28):
                ls[1]+=int(ls[0]/28)
                ls[0]-=int(ls[0]/28)*28

            if(ls[1]>12):
                ls[2]+=int(ls[1]/12)
                ls[2]-=int(ls[1]/12)*12

    lstr=map(str,ls)
    a="/".join(lstr)
    return a        







