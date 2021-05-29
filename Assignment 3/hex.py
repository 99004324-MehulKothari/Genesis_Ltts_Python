# RGB to Hex conversion and vice versa, e.g. (255,0,255) into 0xFF00FF

def compute_hex(ls):
    if(isinstance(ls,list)):
        a="0x"
        for i in ls:
            b=hex(i)
            c=b[2:]
            if(len(c)==1):
                e='0'
                e+=b[2:]
            else:
                e=b[2:]
            d=e.upper()
            a+=d
        return a

    else:
        a=ls[2:]
        c=a.lower()
        b=[]
        b.append(int((ls[0:2]+c[0:2]),16))
        b.append(int((ls[0:2]+c[2:4]),16))
        b.append(int((ls[0:2]+c[4:6]),16))
        return b