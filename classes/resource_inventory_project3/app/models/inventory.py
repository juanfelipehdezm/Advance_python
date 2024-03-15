"""Inventory moodels"""

from app.utils.validators import validate_integer

class Resource:
    """Base calss for resources"""

    def __init__(self, name:str, manufacturer:str,total:int, allocated:int) -> None:

        self._name = name
        self._manufacturer = manufacturer

        if validate_integer("total", total, min_value=0):
            self._total = total
        
        if validate_integer("allocate", allocated, min_value=0, max_value=total):
            self._allocated = allocated

    @property
    def name(self):
        return self._name
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,new_total):
        if validate_integer("new_total",new_total,0):
            self._total = new_total
    
    @property
    def allocated(self):
        return self._allocated
    
    @allocated.setter
    def allocated(self,new_allocated):
        if validate_integer("new allocated", new_allocated, 0):
            self._allocated = new_allocated
    
    @property
    def category(self):
        return type(self).__name__.lower()
    
    @property
    def available(self):
        return self.total - self.allocated
    
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.category}-{self.manufacturer}) : total={self.total}, allocated={self.allocated}"
    

    def claim(self, num_inv_to_claim: int):
        
        if validate_integer("num", num_inv_to_claim,min_value=1):
            self._allocated += num_inv_to_claim

    def freeup(self, num_to_free: int):

        if validate_integer("num", num_to_free,min_value=1, max_value=self.allocated):
            self._allocated -= num_to_free

    def died(self, num_of_dies: int):

        if validate_integer("num", num_of_dies, max_value=self.allocated):
            self._total -= num_of_dies
            self._allocated -= num_of_dies

    def purchased(self,num_purchases: int):
        if validate_integer("num", num_purchases, min_value=1):
            self.total += 1

        
