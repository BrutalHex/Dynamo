import re

class extractor:
    def __init__(self, mainPattern,countPattern,pricePattern):
         self.mainPattern=mainPattern
         self.countPattern=countPattern
         self.pricePattern=pricePattern

    def getPriceAndCount(self,sentence: str) :
            
            if re.match(self.mainPattern,sentence):
                price=re.search(self.pricePattern,sentence).group()
            
                count=re.search(self.countPattern,sentence).group()

                return (int(price),int(count))
            return None