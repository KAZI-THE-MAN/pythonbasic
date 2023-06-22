#vdo 43
#list comprehensions

"""
#map

def double_of_cube(x):
    return 2*(x*x*x)
list1=[2,4,6,8,9]

result=list(map(double_of_cube,list1))
print(result)

"""
list1=[2,4,6,8,9]
result=[2*(x*x*x) for x in list1]
print(result)


"""
#filter

def check(x):
    return x%3==0
list1=[2,4,6,8,9]

result=list(filter(check,list1))
print(result)

list1=[2,4,6,8,9]
"""
list1=[2,4,6,8,9]
result=[x for x in list1 if x%3==0]
print(result)