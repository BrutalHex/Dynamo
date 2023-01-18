
from .extractor import *
from .basketCalculator import *

def normalExtractionOfPriceAndCount(sentence: str):
    patterns=[] 
    result=None
    if len(sentence)==0:
        return result

    '''
    here we can add more extraction strategies.
    the current strategy works based on the regular expssions,
    hopefully, we can use polymorphism and initialize another
    objects that work differently but yield the same result.
    also, this approach has another benefit and it is priority.
    we can add strategies according to their priority to 
    the list of patterns.
    '''
    patterns.append(extractor(r'([0-9]{1,})+\sfor\s([0-9]{1,})+',r'([0-9]+)(?= for )',r'(?<=for )([0-9]+)'))
  
    for ext in patterns:
        result=ext.getPriceAndCount(sentence)
        if result is not None:
            break
    return result



pricingCriteria=''
def setPricingCriteria(input: str):
   global pricingCriteria
   pricingCriteria=input


priceList=[]
def preparePriceList():
    items = [    tuple(line.split()) for  line in pricingCriteria.splitlines()]
    items=[(item[0],item[1], ' '.join( item[2:len(item)])) if len(item)>1  else None for item in items]

    for x in items:
        if x is None:
            continue
        priceList.append(  basketCalculator( x[0],x[1]) )
   
        cobination=normalExtractionOfPriceAndCount( x[2]) 
        
        if cobination is not None:
            priceList.append(  basketCalculator( x[0],  *cobination ))


 

def calculatePrice(input: str) -> int:

    if len(priceList)==0:
        preparePriceList()

    sortedInput=list(input)
    sortedInput.sort()
    input=''.join(sortedInput)
    priceList.sort(key= lambda x: len(x.id),reverse=True)

    for a in priceList:
        input=input.replace(a.id,f'{a.price},')
 
    result=sum( [int(x) if len(x) > 0 else 0  for x in  input.split(',')])
  
    return   result 