#vdo 24
#vdo 25
#list

pl=["python","c","c++","c#","php"]
print(pl)
print(pl[2])
print(pl[2:])
print(pl[:-2])

print("python" in pl)
print("python" not in pl)

print(pl+["swift","js"])
print(pl)

print(len(pl))

pl.append("mojo")#add item at the last
print(pl)

pl.insert(1,"perl")#insert item at the mentioned position
print(pl)

pl.remove("mojo")#remove selected item
print(pl)

pl.pop() #remove last item
print(pl)

pl.sort()
print(pl)

pl.reverse()
print(pl)

pl2=pl.copy()
print(pl2)

s=pl2.index("c++")#position of selected item
print(s)

pl2.append("c++")
print(pl2)

p=pl2.count("c++")#how many c++ at the list
print(p)

print(pl2)
pl2.clear()
print(pl2)

