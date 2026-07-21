"""
    案例：图形面积多态
"""

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return 3.14*self.r*self.r

class Rect:
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area(self):
        return self.w*self.h

class Triangle:
    def __init__(self,a,h):
        self.a = a
        self.h = h
    def area(self):
        return self.a*self.h  / 2

def print_area(shape):
    print(f"图形：{shape.area()}")

print_area(Circle(5))
print_area(Rect(3,4))
print_area(Triangle(5,5))