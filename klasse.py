#klasse
'''
class Point: #En klasse sørger for at vi kan lagre interne gjenstander, i motsetning til funksjon lagrer classe de interne verdier. 
    x = 10
    y = 12
    
    
Point.x = 11 # Kan endre på verdier i klassen


Point.z = 13 # Kan legge nye verdier i en klassen

point = Point()
point.z = 11 
numbers = list()
list.append
'''

'''
class Point:
    def __init__(self) -> None:
        self.x = 4
        self.y = 5
        self.z = 11

    def areal(self):
        return self.x * self.y 


point = Point()

print(point.x, point.y, point.z)
'''
'''
class Point:
    def __init__(self):
        self.x = 4
        self.y = 5

    def __str__(self):
        return f'x:\t{self.x}\ny:\t{self.y}'
    
    def __len__(self):
        return 0
'''       

class Point:
    def __init__(self):
        self.x = 4
        self.y = 5

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
    def __len__(self):
        return 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

point_one = Point(x=5, y=6)
point_two = Point(x=4, y=7)

point_three = point_one + point_two
print(point_three)
