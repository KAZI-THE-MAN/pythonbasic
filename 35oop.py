#vdo 51
#vdo 52
#oop
"""
class student:
    roll=""
    cgpa=""
Jessy=student()
Jessy.roll=101
Jessy.cgpa=3.78
#print(isinstance(Jessy,student))
print(f"Jessy's roll: {Jessy.roll}, cgp: {Jessy.cgpa}")


Jerry=student()
Jerry.roll=102
Jerry.cgpa=3.80
print(f"Jerry's roll: {Jerry.roll}, cgp: {Jerry.cgpa}")

"""

class student:
    roll=" "
    cgpa=" "

    def set_value(self,roll,cgpa):
        self.roll=roll
        self.cgpa=cgpa

    def display(self):
              print(f" roll: {self.roll}, cgp: {self.cgpa}")


Jessy=student()
Jessy.set_value(101,3.75)
Jessy.display()


Jerry=student()
Jerry.set_value(102,3.8)
Jerry.display()