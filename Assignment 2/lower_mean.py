# In a given list, count no.of elements smaller than their mean

def compute_lower_mean(ls):
    a=sum(ls)/len(ls)
    count=0
    for i in ls:
        if i<a:
            count+=1
    return count