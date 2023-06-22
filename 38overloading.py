#vdo 56
#overloading

class phone:
    def __init__(self):
        print("I am in super class")
class samsung(phone):
    pass

s=samsung()

class phone:
    def __init__(self):
        print("I am in super class")
class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I am in subclass class")


s=samsung()


