# Type of triangle - equilateral, isosceles, scalene, right angled

def triangle_eicr(x,y,z):
    if(x==y and y==z):
        return 1
    elif(x==y or x==z or y==z):
        return 2
    elif(pow(x,2)==(pow(y,2)+pow(z,2)) or pow(y,2)==(pow(x,2)+pow(z,2)) or pow(z,2)==(pow(x,2)+pow(y,2))):
        return 3
    else:
        return 4
