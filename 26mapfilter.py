#vdo 42
#map

def double_of_cube(x):
    return 2*(x*x*x)
list1=[2,4,6,8,9]

result=list(map(double_of_cube,list1))
print(result)

#filter

def check(x):
    return x%3==0
list1=[2,4,6,8,9]

result=list(filter(check,list1))
print(result)

result1=list(filter((lambda x: x%2==0),list1))
print(result1)