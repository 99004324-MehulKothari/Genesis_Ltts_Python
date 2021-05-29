# List/count of prime numbers for given range

def compute_prime(n):
    count=0
    if (n<=1):
        return 0
    else:

        for i in range(2,n):
            flag=0
            for j in range(2,i):
                if (i%j==0):
                    flag=1
                    break
            if(flag==0):
                count+=1
        return count