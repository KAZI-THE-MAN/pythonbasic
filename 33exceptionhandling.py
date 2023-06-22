#vdo 48
#vdo 49
#exception handling
try:#wrong area
    list=[10,0,30,40]
    d=list[2]/list[3]
    print(d)
except (ZeroDivisionError,IndexError):#types of error
    print("it,s an error")
finally:#must print area
    print("done")

