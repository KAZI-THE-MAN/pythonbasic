#vdo 41
#lambda function/anonymous function
#named function

def function1(a,b):
    return a*a+2*a*b+b*b
print(function1(2,3))

#lambda function
print((lambda p,s: p*p+2*p*s+s*s)(2,3))

d=(lambda x: x*x*x)(2)
print(d)