#vdo 46
#read file

# r for only read ,w for  only write , r+ for both read and write
r=open("30text.txt","r")
x=r.read() # for read
print(x)
print(r.readable()) # to check readable or not
c=len(x)
print(c)

r.close()