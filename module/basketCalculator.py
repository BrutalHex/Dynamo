class basketCalculator:
    def __init__(self,id: str,price: str,count=1):
            self.id=''.join([id for i in range(count)])
            self.price=price
            self.count=count
    
    def getPrice(self,id: str,count: int) -> int:  
         if count==self.count and id==self.id : 
                return int(self.price)
         else:
            return 0