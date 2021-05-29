# Check whether given string is isogram or not

from typing import Counter


def compute_isogram(s):
    a=Counter(s)
    for i in a:
        if a[i]>1:
            return 0
    
    return 1
