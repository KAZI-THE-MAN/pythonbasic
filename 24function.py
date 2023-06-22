#vdo 37
#vdo 38
#vdo 39
#function
def add(x,y):
    sum=x+y
    print(sum)
add(2,4)

def add(x,y,z):
    sum=x+y+z
    print(sum)
add(2,4,7)


def add(x,y,z):
    sum=x+y+z
    return sum
s=add(2,4,9)
print(s)

def student(id,name):
    print(id,name)
student(11,"Kazi Mehedi")
student(12,"Kazi Maliha")

def student(*details):
    print(details)
student(11,"Kazi Mehedi",344)
student(12,"Kazi Maliha",344)


def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)
add(234+24+25+2)
add(6+3)

def student(**details):
    print(details)
student(roll=11,name="Kazi Mehedi",room=344)
student(roll=12,name="Kazi Mehediii",room=345)

