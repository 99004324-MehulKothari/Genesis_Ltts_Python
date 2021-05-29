# Quadrant of a given point (x,y)

def quad(x,y):
    if (x==0 and y==0):
        return 0
    elif (x==0 and y==1):
        return 1
    elif (x==1 and y==0):
        return 2
    elif (x==1 and y==1):
        return 3
    else:
        return -1