from timer import compute_time
from dates import compute_dates
from ip import compute_ip
from isogram import compute_isogram
from mexicanwave import compute_mexicanwave
from large_single import compute_large_single
from words import compute_words
from hex import compute_hex
from accu import compute_accu
from large_shuffle import compute_large_shuffle


def test_time():
    assert compute_time("5:70:65")=="6:11:5"
    assert compute_time("8:247:125")=="12:9:5"

def test_dates():
    assert compute_dates("45/8/2018")=="14/9/2018"
    assert compute_dates("45/2/2019")=="17/3/2019"

def test_ip():
    assert compute_ip("12.34.56.78")==12345678

def test_isogram():
    assert compute_isogram("education")==1
    assert compute_isogram("Geeks")==0

def test_mexicanwave():
    assert compute_mexicanwave("xyz")==["Xyz","xYz","xyZ"]
    assert compute_mexicanwave("geeks")==["Geeks","gEeks","geEks","geeKs","geekS"]


def test_large_single():
    assert compute_large_single(97492)==9792
    assert compute_large_single(492846)==92846

def test_words():
    assert compute_words("Hello Mehul Here")==3
    assert compute_words("Cricket is a lovely game to play")==7

def test_hex():
    assert compute_hex([255,0,255])=="0xFF00FF"
    assert compute_hex("0xFF00FF")==[255,0,255]

def test_acu():
    assert compute_accu("abcd")=="A-Bb-Ccc-Dddd"
    assert compute_accu("ksdlf")=="K-Ss-Ddd-Llll-Fffff"
    

def test_large_shuffle():
    assert compute_large_shuffle(41926)==96421
    assert compute_large_shuffle(182959)==998521