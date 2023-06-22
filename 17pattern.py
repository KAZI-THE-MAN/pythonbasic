#vdo 29
#pattern

s=int(input("first number: "))
e=int(input("last number: "))
g=int(input("gap between numbers: "))
for i in range(s,e+1,g):
    print(i*"*")


s=int(input("first number: "))
e=int(input("last number: "))
g=int(input("gap between numbers: "))
for i in range(s,e+1,g):
    print(i*"*")

s=int(input("first number: "))
e=int(input("last number: "))
i=s
while(i<=e):
    print(((e-i)*" ")+(i*"*"))
    i=i+1

