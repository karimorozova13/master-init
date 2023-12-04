from random import randrange

class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x)==int or type(x)==float):
            self.__x=x
            
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y)==int or type(y)==float):
            self.__y = y
    def __str__(self) -> str:
        return f"Point({self.__x},{self.__y})"
           
        
        
class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        elif index== 1:
            self.coordinates.y = value
        else:
            raise IndexError('Out of range')
        
    def __getitem__(self,index ):
        if index==0:
            return self.coordinates.x
        elif index==1:
            return self.coordinates.y
        else:
            raise IndexError('Out of range')
    
    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    def __call__(self,val=1):
        return (self.coordinates.x * val, self.coordinates.y * val)
    
    def __add__(self,vector):
        new_coor = Point(vector.coordinates.x + self.coordinates.x,vector.coordinates.y + self.coordinates.y)
        return Vector(new_coor)
    
    def __sub__(self,vector):
        new_coor = Point(self.coordinates.x - vector.coordinates.x,self.coordinates.y - vector.coordinates.y)
        return Vector(new_coor)
    
    def __mul__(self,vector):
        scalar = (vector.coordinates.x * self.coordinates.x) + (vector.coordinates.y * self.coordinates.y)
        return scalar
    
    def len(self):
        return (self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
    
    def __eq__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self == vector_len

    def __ne__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self != vector_len

    def __lt__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self < vector_len
        
    def __gt__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self > vector_len
        
    def __le__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self <= vector_len

    def __ge__(self, vector):
        len_self =(self.coordinates.x ** 2  + self.coordinates.y ** 2) ** 0.5
        vector_len = (vector.coordinates.x ** 2  + vector.coordinates.y ** 2) ** 0.5
        return len_self >= vector_len
    
class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        self.max_vectors= max_vectors
        self.max_points= max_points
    def __next__(self):
        if self.current_index < self.max_vectors:
            self.current_index +=1
            return Vector(Point(randrange(0, self.max_points), randrange(0,self.max_points)))
        raise StopIteration

class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors= max_vectors
        self.max_points= max_points
    def __iter__(self):
        return Iterable(self.max_vectors,self.max_points)     
      
        
        
vector1 = Vector(Point(1, 10))
vector2 = Vector(Point(10, 10))

vector3 = vector2 + vector1
vector4 = vector2 * vector1
ran = RandomVectors()
for r in ran:
    print(r)

# print(vector1.len())  # Vector(11,20)
# print(vector2.len())  # Vector(9,0)
