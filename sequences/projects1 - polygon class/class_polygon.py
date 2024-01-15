#PROJECT 

"""
We need to create a Polygon class with the following properties:

* number of vertices `n` - passed to the initializer
* circumradius `R` - passed to the initializer
* number of edges
* number of sides
* interior angle (in degrees)
* side length
* apothem
* surface area
* perimeter
* supports equality based on number of vertices and circumradius
* supports `>` based on number of vertices

"""

import math

class polygon:
    def __init__(self, n : int, R: float):
        self.n = n
        self.R = R
    
    def __repr__(self):
        return f'Polygon(n={self.n}, R={self.R})'
    
    @property #decorator to set a property of the class https://www.geeksforgeeks.org/python-property-decorator-property/
    def n_of_vertices(self):
        return f"The number of vertices is: {self.n}"
    
    @property
    def n_of_edges(self):
        return f"The number of edges is the same as the number of vertices: {self.n}"
    
    @property
    def circumradius(self):
        return f"The circunradious is : {self.R}"

    @property
    def interior_angle(self):
        return round((self.n - 2) * 100 / self.n,3)
    
    @property
    def side_length(self):
        return round(2 * self.R * math.sin(math.pi / self.n),3)
    
    @property
    def apothem(self):
        return round(self.R * math.cos(math.pi / self.n),3)
    
    @property
    def area(self):
        return round(self.n / 2 * self.side_length * self.apothem,3)
    
    @property
    def perimeter(self):
        return round(self.n * self.side_length,3)
    

    
polygon = polygon(3, 3.4)

print(polygon.__repr__)

