#vdo 14
#vdo 15
#vdo 16
#control statement (if,elif,else)

#if part

if(2>7):
    print("cat")
if(12>6):
    print("cow")

#if else part
#program to check a number even or odd
num=int(input("enter: "))
if(num%2==0):
    print("even")
else:
    print("odd")

#if else elif part
#program for checking grade

mark=int(input("enter mark: "))
if(mark>=80):
    print("A+")
elif(mark>=70):
    print("A")
elif(mark>=60):
    print("A-")
elif(mark>=50):
    print("B")
elif(mark>=40):
    print("C")
elif(mark>=33):
    print("D")
else:
    print("Fail")