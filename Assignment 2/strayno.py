# In a given list of elements, all elements are equal except the one.Write a code to find the odd man out

from typing import Counter


def compute_stray_no(ls):
    a=Counter(ls)
    for i in a:
        if a[i]==1:
            return i