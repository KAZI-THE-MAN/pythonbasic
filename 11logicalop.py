#vdo 19
#logical operator

num1=int(input("enter: "))
num2=int(input("enter: "))
num3=int(input("enter: "))

if(num1>num2 and num1>num3):
    print(num1,"is the biggest value")
elif(num2>num1 and num2>num3):
    print(num2,"is the biggest value")
else:
    print(num3, "is the biggest value")