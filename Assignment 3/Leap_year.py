# Check if given year is Leap year or not

def leap(year):
    if(year%4)==0:
        if(year%100)==0:
            if(year%400)==0:
                return 1
            else:
                return 0
            
        else:
            return 1
    else:
        return 0