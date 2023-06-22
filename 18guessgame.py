#vdo 30
#guessing game
from random import randint
n=int(input("how many times you want to try: "))
for i in range(1,n+1):
    guessnumber=int(input("your guessnumber: "))
    randomnumber=randint(1,30)

    if guessnumber==randomnumber:
        print("you choose the correct number at the ",i," no. time")
        break
    else:
        print("you choose the wrong number at the ", i, "no. time")
        print("the random number was",randomnumber)
print("END - no chance more")