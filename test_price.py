from module.pricing import *
from supermarket import *

def test_answer():
    assert calculatePrice("") == 0
    assert calculatePrice("A")== 50
    assert calculatePrice("AB")== 80
    assert calculatePrice("CDBA")==115
    assert calculatePrice("AA")==100
    assert calculatePrice("AAA")==130
    assert calculatePrice("AAAA")==180
    assert calculatePrice("AAAAA")==230
    assert calculatePrice("AAAAAA")==260
    assert calculatePrice("AAAB")==160
    assert calculatePrice("AAABB")==175
    assert calculatePrice("AAABBD")==190
    assert calculatePrice("DABABA")==190

def test_incremental():
    items=''
    assert calculatePrice(items) == 0
    items+="A"  
    assert calculatePrice(items)== 50 
    items+="B" 
    assert calculatePrice(items)== 80 
    items+="A"  
    assert calculatePrice(items)==130
    items+="A"  
    assert calculatePrice(items)==160
    items+="B"  
    assert calculatePrice(items)==175