# Sum of triangular numbers

def compute_sum_triang(n):
    sum=0
    if n<1:
        return 0
    else:
        for i in range(1,n+1):
            for j in range(1,i+1):
                sum+=j

        return sum