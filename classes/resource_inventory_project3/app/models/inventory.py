"""Inventory moodels"""

from app.utils.validators import validate_integer

class Resource:
    """
    **Summary:**

    This class serves as the base class for representing resources within a system. It defines common attributes and methods for managing the total quantity, allocated quantity, and availability of a resource.

    **Attributes:**

    * `name (str)`: The name of the resource.
    * `manufacturer (str)`: The manufacturer of the resource.
    * `total (int)`: The total quantity of the resource available. (must be non-negative)
    * `allocated (int)`: The quantity of the resource currently allocated. (must be non-negative and less than or equal to total)
    * `category (str)`: The resource category derived from the class name (lowercase). (read-only)
    * `available (int)`: The quantity of the resource currently available for allocation (calculated property). (read-only)

    **Methods:**

    * `__init__(self, name: str, manufacturer: str, total: int, allocated: int) -> None`  
    Initializes a `Resource` object with the given name, manufacturer, total quantity, and allocated quantity.
    * `claim(self, num_inv_to_claim: int) -> None`: Allocates a specified number of resources to the allocated pool. (argument must be a positive integer)
    * `freeup(self, num_to_free: int) -> None`: Releases a specified number of resources from the allocated pool back to the available pool. (argument must be a positive integer, and cannot exceed the currently allocated amount)
    * `died(self, num_of_dies: int) -> None`: Reduces the total and allocated quantities by a specified number, representing resource loss. (argument must be a non-negative integer, and cannot exceed the currently allocated amount)
    * `purchased(self, num_purchases: int) -> None`: Increases the total quantity of the resource by a specified number, representing a purchase. (argument must be a positive integer)

    **Notes:**

    * The `validate_integer` function (assumed to exist elsewhere) is used internally to validate integer arguments and raise appropriate exceptions for invalid values.

    **Str and Repr:**

    * `__str__(self) -> str`: Returns the resource name.
    * `__repr__(self) -> str`: Returns a detailed string representation of the resource, including name, category, manufacturer, total quantity, and allocated quantity.
"""

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

        
