from module.basketCalculator import *

def test_getPrice():
    id="A"
    price='1000'
    count=5
    sample=basketCalculator(id,price,count)
    assert sample.getPrice('AAAAA',count)==int(price)

    assert sample.getPrice('B',count)==0
    assert sample.getPrice(id,100)==0