#vdo 53
#vdo 54
#constructor

class student:
    roll=" "
    cgpa=" "

    def __init__(self,roll,cgpa):
        self.roll=roll
        self.cgpa=cgpa

    def display(self):
        print(f" roll: {self.roll}, cgp: {self.cgpa}")

Jessy=student(101,3.75)
Jessy.display()

Jerry=student(102,3.8)
Jerry.display()



class Triangle:
    base=" "
    height=" "

    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        self.area_t=0.5*self.base*self.height
        print(f"area is {self.area_t}")

t1=Triangle(10,20)
t1.area()

t2=Triangle(20,30)
t2.area()
