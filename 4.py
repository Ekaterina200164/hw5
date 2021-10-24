class Shape:
    def get_area(self):
        pass
    def get_perimeter(self):
        pass
    def __str__(self):
        return " ".join([self.get_name(), " с площадью ", str(self.get_area()), " и периметром ", str(self.get_perimeter())])

class Quadrilateral(Shape):
    def get_name(self):
        return "Четырехугольник"
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    def get_perimeter(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        b = ((self.p2[0]-self.p3[0])**2 + (self.p2[1]-self.p3[1])**2)**(1/2)
        c = ((self.p3[0]-self.p4[0])**2 + (self.p3[1]-self.p4[1])**2)**(1/2)
        d = ((self.p4[0]-self.p1[0])**2 + (self.p4[1]-self.p1[1])**2)**(1/2)
        perimeter = a + b + c + d
        return perimeter
    def get_area(self):
        area = abs(1/2*(self.p1[0]*self.p2[1] + self.p2[0]*self.p3[1] + self.p3[0]*self.p4[1]  + self.p4[0] * self.p1[1] - self.p2[0]*self.p1[1] - self.p3[0]*self.p2[1] - self.p1[0]*self.p4[1] - self.p4[0] * self.p3[1]))
        return area
    
class Square(Quadrilateral):
    def get_name(self):
        return "Квадрат"
    def get_area(self):
	    return (self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2
    def get_perimeter(self):
        return 4*((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)

class Rhombus(Quadrilateral):
    def get_name(self):
        return "Ромб"
    def get_perimeter(self):
        return 4*((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
    def get_area(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        d = ((self.p1[0]-self.p3[0])**2 + (self.p1[1]-self.p3[1])**2)**(1/2)
        area = d*(a**2-1/4*d**2)**(1/2)
        return area

    
class Triangle(Shape):
    def get_name(self):
        return "Треугольник"
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def get_perimeter(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        b = ((self.p2[0]-self.p3[0])**2 + (self.p2[1]-self.p3[1])**2)**(1/2)
        c = ((self.p3[0]-self.p1[0])**2 + (self.p3[1]-self.p1[1])**2)**(1/2)
        perimeter =  a + b + c
        return perimeter
    def get_area(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        b = ((self.p2[0]-self.p3[0])**2 + (self.p2[1]-self.p3[1])**2)**(1/2)
        c = ((self.p3[0]-self.p1[0])**2 + (self.p3[1]-self.p1[1])**2)**(1/2)
        p =  (a + b + c)/2
        return (p*(p-a)*(p-b)*(p-c))**(1/2)

class Ellipse(Shape):
    def get_name(self):
        return "Эллипс"
    def __init__(self, p1, p2, p3):
        self.p1 = p1 #Центр
        self.p2 = p2 #Кооринаты а
        self.p3 = p3 #Координаты b
    def get_area(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        b = ((self.p1[0]-self.p3[0])**2 + (self.p1[1]-self.p3[1])**2)**(1/2)
        return 3.14*a*b
    def get_perimeter(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        b = ((self.p1[0]-self.p3[0])**2 + (self.p1[1]-self.p3[1])**2)**(1/2)
        return 2*3.14*((a**2+b**2)/2)**(1/2)

class Circle(Ellipse):
    def get_name(self):
        return "Круг"
    def get_area(self):
        a = ((self.p1[0]-self.p2[0])**2 + (self.p1[1]-self.p2[1])**2)**(1/2)
        return 3.14*a**2
    def get_perimeter(self):
        b = ((self.p1[0]-self.p3[0])**2 + (self.p1[1]-self.p3[1])**2)**(1/2)
        return 2*3.14*b

print(Quadrilateral((1, 2), (1, 4), (3, 0), (1, -1)))
print(Square((1, 1), (1, 4), (4, 4), (4, 1)))
print(Rhombus((1,3), (2,5), (3,3), (2,1)))
print(Triangle((1,2), (3,2), (3,6)))
print(Ellipse((5,3), (5,1), (9,3)))
print(Circle((5,3), (2,3), (8,3)))
