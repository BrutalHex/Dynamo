from module.pricing import *
from functools import reduce
import re
str='''
    A     50       3 for 130
    B     30       2 for 45
    C     20
    D     15
'''




def normalExtractionOfPriceAndCount(sentence):
    patterns=[] 
    result=None
    if len(sentence)==0:
        return result

    patterns.append(extractor(r'([0-9]{1,})+\sfor\s([0-9]{1,})+',r'([0-9]+)(?= for )',r'(?<=for )([0-9]+)'))
  
    for ext in patterns:
        result=ext.getPriceAndCount(sentence)
        if result is not None:
            break
    return result

class extractor:
    def __init__(self, mainPattern,countPattern,pricePattern):
         self.mainPattern=mainPattern
         self.countPattern=countPattern
         self.pricePattern=pricePattern

    def getPriceAndCount(self,sentence):
            
            if re.match(self.mainPattern,sentence):
                price=re.search(self.pricePattern,sentence).group()
            
                count=re.search(self.countPattern,sentence).group()

                return (int(price),int(count))
            return None



class basketCalculator:
    def __init__(self,id,price,count=1):
            self.id=''.join([id for i in range(count)])
            self.price=price
            self.count=count
    
    def getPrice(self,id,count):  
      
         if count==self.count and id==self.id : 
                return int(self.price)
         else:
            return 0

priceList=[]
def preparePriceList():
    items = [    tuple(line.split()) for  line in str.splitlines()]
    items=[(item[0],item[1], ' '.join( item[2:len(item)])) if len(item)>1  else None for item in items]

    for x in items:
        if x is None:
            continue
        priceList.append(  basketCalculator( x[0],x[1]) )
   
        cobination=normalExtractionOfPriceAndCount( x[2]) 
        
        if cobination is not None:
            priceList.append(  basketCalculator( x[0],  *cobination ))


 

def calculatePrice(input):

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
         


 
 
 
 





 