#vdo 32
#matrix

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
k=m[1][2]
print(k)

m[1][2]=56
print(m)

for row in m:
    for col in row:
        print(col)