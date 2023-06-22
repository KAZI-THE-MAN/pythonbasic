#vdo 45
#recursion
#factorial of any number
def recursion(x):
      if x==1:
          return 1
      else:
          return x*recursion(x-1)
b=recursion(25)
print(b)

