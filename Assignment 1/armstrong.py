# Check if given number is armstrong or not

def armnum(n):
    a=list(map(int,str(n)))
    sum=0
    for i in a:
        sum+=pow(int(i),3)
    if(sum==n):
        return 1
    else:
        return 0
