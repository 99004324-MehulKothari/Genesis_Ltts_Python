from strayno import compute_stray_no
from mean import compute_mean
from speed import compute_speed
from bus import compute_bus
from new_old import compute_new_old
from diff_least import compute_diff_least
from lower_mean import compute_lower_mean




def test_strayno():
    assert compute_stray_no([1,1,1,1,1,2])==2
    assert compute_stray_no([5,3,5,5,5,5])==3


def test_mean():
    assert compute_mean([1,2,3,4,5])==3
    assert compute_mean([1,3,5,7,9])==5
    assert compute_mean([3,5,1,7,9])==5
    assert compute_mean([1,1,1,1,1])==1

def test_speed():
    assert compute_speed([1,2,3,4,5],6)==2
    assert compute_speed([5,3,1,7,9],15)==3

def test_bus():
    assert compute_bus(5,2)==3
    assert compute_bus(10,3)==7
    assert compute_bus(50,27)==23

def test_new_old():
    assert compute_new_old([40,42,59,11,23],[40,42,11,23])==59
    assert compute_new_old([40,42,59,11,23],[40,42,59,23])==11
    assert compute_new_old([40,42,59,11,23],[40,42,59,11])==23


def test_diff_least():
    assert compute_diff_least([20,30,40,10])==10
    assert compute_diff_least([19,51,23,45])==4


def test_lower_mean():
    assert compute_lower_mean([1,3,5,7,9])==2
    assert compute_lower_mean([10,20,30,40,50,60,70])==3