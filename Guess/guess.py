import numpy as np
g = np.random.randint(0,1000)

rg = 8
print("your remaining guesses : 8")
a = int(input("please guess a number between one and one thousnd : "))
for i in range(8) :
    if a == g :
        print(f"you win!\nnumber was {g}")
        break
    elif a > g :
        rg -= 1
        print("your guess is more than the desired number")
        a = int(input("please guess a number between one and one thousnd : "))
    elif a < g :
        rg -= 1
        print("your guess is less than the desired number")
        a = int(input("please guess a number between one and one thousnd : "))
    print(f"your remaining guesses : {rg}")
    if rg == 0 and a == g :
        print(f"you win!\nnumber was {g}")
    elif rg == 0 and a != g :
        print(f"you lose!\ndesired number was {g}")