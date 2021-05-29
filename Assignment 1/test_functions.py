from greatest import great
from armstrong import armnum
from rev_sum import reverse,sum_n
from Leap_year import leap
from triangle import triangle_eicr
from quadratic import root1,root2
from quadrant import quad
from choice_art import calci
from vow_cons import v_c
from gcd import hcf
from lcm import compute_lcm
from fibonacci import compute_fibonacci
from tribonacci import printTribRec
from factorial import compute_fact
from sum_fact import compute_sum_fact
from digital_root import compute_digital_root
from prime import compute_prime
from sum_triang import compute_sum_triang
from max_single import compute_max_single
from combinations import compute_combinations

def test_great():
    assert great(2,3,4)==4
    assert great(8,1,2)==8

def test_arm():
    assert armnum(153)==1
    assert armnum(233)==0
    assert armnum(0)==1
    assert armnum(1)==1

def test_rev_sum():
    assert reverse(234)==432
    assert reverse(82341)==14328
    assert reverse(1)==1
    assert sum_n(123)==6
    assert sum_n(629)==17

def test_leap_year():
    assert leap(2012)==1
    assert leap(2000)==1
    assert leap(10)==0
    assert leap(2013)==0
    assert leap(900)==0

def test_triangle():
    assert triangle_eicr(2,2,2)==1
    assert triangle_eicr(2,3,3)==2
    assert triangle_eicr(5,3,4)==3
    assert triangle_eicr(1,2,3)==4


def test_root():
    assert root1(1,-13,30)==10
    assert root2(1,-13,30)==3

def test_quadrant():
    assert quad(0,0)==0
    assert quad(0,1)==1
    assert quad(1,0)==2
    assert quad(1,1)==3
    assert quad(2,3)==-1

def test_choice_art():
    assert calci(1,3,3)==6
    assert calci(2,3,3)==0
    assert calci(3,3,3)==9
    assert calci(4,3,3)==1

def test_vow_cons():
    assert v_c('a')==1
    assert v_c('e')==1
    assert v_c('E')==1
    assert v_c('i')==1
    assert v_c('O')==1
    assert v_c('u')==1
    assert v_c('b')==0
    assert v_c('C')==0
    
def test_gcd():
    assert hcf(2,6)==2
    assert hcf(2,3)==1
    assert hcf(20,40)==20

def test_lcm():
    assert compute_lcm(2,6)==6
    assert compute_lcm(10,30)==30

def test_fibonacci():
    assert compute_fibonacci(8)==21
    assert compute_fibonacci(0)==0
    assert compute_fibonacci(1)==1
    assert compute_fibonacci(9)==34

def test_tribonacci():
    assert printTribRec(0)==0
    assert printTribRec(6)==4
    assert printTribRec(8)==13
    assert printTribRec(9)==24

def test_factorial():
    assert compute_fact(0)==1
    assert compute_fact(-5)==-1
    assert compute_fact(4)==24

def  test_sum_fact():
    assert compute_sum_fact(-2)==0
    assert compute_sum_fact(0)==0
    assert compute_sum_fact(1)==1
    assert compute_sum_fact(6)==12
    assert compute_sum_fact(10)==18


def test_digital_root():
    assert compute_digital_root(14567)==5
    assert compute_digital_root(9999)==9
    assert compute_digital_root(7895)==2


def test_prime():
    assert compute_prime(10)==4
    assert compute_prime(15)==6
    assert compute_prime(1)==0


def test_sum_triang():
    assert compute_sum_triang(4)==20
    assert compute_sum_triang(5)==35
    assert compute_sum_triang(0)==0
    assert compute_sum_triang(-2)==0
    assert compute_sum_triang(1)==1

def test_max_single():
    assert compute_max_single(5872)==872
    assert compute_max_single(4567)==567
    assert compute_max_single(9000)==900
    assert compute_max_single(9279)==979
def test_combinations():
    assert compute_combinations(4,1)==4
    assert compute_combinations(6,4)==15

