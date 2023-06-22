#vdo 28
#series

#1+2+3+4+5+6+7+............+172
#3+6+9+....................+234
s=int(input("first number: "))
e=int(input("last number: "))
g=int(input("gap between numbers: "))
for i in range(s,e+1,g):
    print(i)

sum=0
for i in range(s,e+1,g):
    sum=sum+i
print(sum)

#2**3+3**3+4**3+.....+7**3
s=int(input("first number: "))
e=int(input("last number: "))
g=int(input("gap between numbers: "))
for i in range(s,e+1,g):
    print(i)

sum=0
for i in range(s,e+1,g):
    sum=sum+(i*i*i)
print(sum)

#2*3*4*5*......*8
s=int(input("first number: "))
e=int(input("last number: "))
g=int(input("gap between numbers: "))
for i in range(s,e+1,g):
    print(i)

mul=1
for i in range(s,e+1,g):
    mul=mul*i
print(mul)