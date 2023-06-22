#vdo 31
#list from user input

n=input("enter element: ")
list=n.split()

sum=0
for num in list:
    sum=sum+int(num)
print(sum)