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

        
class CPU(Resource):

    """
    **Summary:**

    This class represents a Central Processing Unit (CPU) resource, inheriting from the base `Resource` class. It extends the resource concept with CPU-specific attributes like core count, socket type, and power consumption.

    **Attributes:**

    * Inherits all attributes from the `Resource` class (name, manufacturer, total, allocated).
    * `cores (int)`: The number of CPU cores. (must be between 2 and 64, inclusive)
    * `socket (str)`: The CPU socket type.
    * `power_watts (int)`: The power consumption of the CPU in watts. (must be between 10 and 1000 watts, inclusive)

    **Methods:**

    * Inherits all methods from the `Resource` class.

    **Notes:**

    * The `validate_integer` function (assumed to exist elsewhere) is used internally to validate integer arguments and raise appropriate exceptions for invalid values.

    **Str Repr:**

    * `__repr__(self) -> str`: Returns a detailed string representation of the CPU resource, including category, name, socket type, and core count.

    """

    def __init__(self, name: str, manufacturer: str, total: int, allocated: int,
                       cores: int, socket:str, power_watts: int) -> None:
        
        super().__init__(name, manufacturer, total, allocated)

        if validate_integer("cores",cores, min_value=2, max_value=64):
            self._cores = cores

        self._socket = socket

        if validate_integer("power_watts", power_watts, min_value=10, max_value=1000):
            self._power_watts = power_watts


    @property
    def cores(self):
        return self._cores
    
    @property
    def socket(self):
        return self._socket
    
    @property
    def power_watts(self):
        return self._power_watts
    
    def __repr__(self) -> str:
        return f"{self.category}: {self.name} ({self.socket} - x{self.cores})"
    

class Storage(Resource):
    """
    **Summary:**

    This class represents a storage resource, inheriting from the base `Resource` class. It adds a storage-specific attribute, `capacity_gb`, for representing storage capacity in gigabytes.

    **Attributes:**

    * Inherits all attributes from the `Resource` class (name, manufacturer, total, allocated).
    * `capacity_gb (int)`: The storage capacity in gigabytes. (must be at least 250GB).

    **Methods:**

    * Inherits all methods from the `Resource` class.

    **Notes:**

    * The `validate_integer` function (assumed to exist elsewhere) is used internally to validate the `capacity_gb` argument and raise a `ValueError` for invalid values.

    **Str Repr:**

    * `__repr__(self) -> str`: Returns a string representation of the storage resource, indicating its category and capacity in gigabytes.

    """
    
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_gb:int) -> None:
        super().__init__(name, manufacturer, total, allocated)

        if validate_integer("capacity_gb", capacity_gb, min_value=250):
            self._capacity_gb = capacity_gb

        
    @property
    def capacity_gb(self):
        return self._capacity_gb
    
    def __repr__(self):
        return f"({self.category}: {self.capacity_gb})"
        
