# No.of combinations for n teams to play each other
from factorial import compute_fact

def compute_combinations(n,r):
    val=compute_fact(n)/(compute_fact(n-r)*compute_fact(r))
    return val
