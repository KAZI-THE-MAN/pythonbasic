#vdo 57
#example of inheritence

class shape:
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def area(self):
        print("I am the area method of shape class")

class triangle(shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print("area of triangle: ",area)

class rectangle(shape):
    def area(self):
        area=self.dim1*self.dim2
        print("area of rectangle: ",area)
t1 = triangle(20,30)
t1.area()

t2=rectangle(20,30)
t2.area()
