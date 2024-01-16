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

class Polygon:
    def __init__(self, n : int, R: float):
        if n < 3:
            raise ValueError("Polygon must have at least 3 sides")
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
    
    #method used to compare the equality of two intances of the same class
    def __eq__(self, other_polygon):
        if isinstance(other_polygon, self.__class__):
            return self.n_of_edges == other_polygon.n_of_edges and \
                   self.circumradius == other_polygon.circumradius
        else:
            return NotImplemented
                   
    def __gt__(self, other_polygon):
        if isinstance(other_polygon, Polygon): #Polygon or self.__class__ represent the class so both are valid
            return self.n_of_vertices > other_polygon.n_of_vertices
        else:
            return NotImplemented

    
polygon1 = Polygon(3, 3)
polygon2 = Polygon(5,5)

#print(polygon2.__gt__(polygon1))


#print(polygon.apothem)

#my sequence class 

class Polygons_sqc:
    
    def __init__(self, M: int, R: float ) -> None:
        if M < 3:
            raise ValueError("M must be grather than 3")
        
        self.M = M
        self.R = R
        #a poligons private attributes which is going to store the poligons created with the 
        #Polygons class

        self.polygons = [Polygon(i,R) for i in range(3, M+1)]


    def __len__(self):
        return self.M
    
    def __repr__(self) -> str:
        return f"Polygons(M ={self.M}, R = {self.R})"
    
    def __getitem__(self,s):
        return self.polygons[s]
    
    @property
    def max_efficiency_polygon_sorting(self):
        return sorted(
            self.polygons, key=lambda p: p.area / p.perimeter, reverse=True
        )        
    


polygons = Polygons_sqc(5,3)

#for p in polygons:print(p)
#Polygon(n=3, R=3)
#Polygon(n=4, R=3)
#Polygon(n=5, R=3)

#list_of_polygons = list(polygons)

#print(list_of_polygons)

print(polygons.max_efficiency_polygon_sorting)