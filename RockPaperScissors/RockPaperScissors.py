#-----------------------------------------------------------------------------
#import libraries
import numpy as np
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#give points for win

win = int(input("Please enter your points to win : "))
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#results

You = 0
CPU = 0
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#run the game

while You < win or CPU < win :
    #------------------------------------------------------------------------
    #determining the winner

    if You == win :
        print(f"you win!\nYou : {You}\nCPU : {CPU}")
        break
    elif CPU == win :
        print(f"you lose!\nYou : {You}\nCPU : {CPU}")
        break
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    #select an option

    a = input("scissors ,Paper ,Stone : ")
    x = np.random.randint(0,3)
    ls = ["sang" , "scissors","s" ,"سنگ" ,"س" ,"0"]
    lk = ["kaghaz" ,"paper" ,"p" ,"k" ,"کاغذ" ,"ک" ,"1"]
    lgh = ["gheichi" ,"stone" ,"gh" ,"st" ,"قیچی" ,"ق" ,"2"]
    li = ["sang" ,"kaghaz" ,"gheichi"]
    if a in ls :
        a = "sang"
    elif a in lk :
        a = "kaghaz"
    elif a in lgh :
        a = "gheichi"
    b = li[x]
    #------------------------------------------------------------------------

    #------------------------------------------------------------------------
    #lows

    if a==b :
        You = You
        CPU = CPU
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a=="sang" and b=="gheichi" :
        You += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a == "gheichi" and b == "sang" :
        CPU += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a == "kaghaz" and b == "sang" :
        You += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a == "sang" and b == "kaghaz" :
        CPU += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a == "gheichi" and b == "kaghaz" :
        You += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    elif a == "kaghaz" and b == "gheichi" :
        CPU += 1
        print(f"CPU : {b}")
        print(f"yor points : {You}")
        print(f"cpus points : {CPU}")
    #------------------------------------------------------------------------
#-----------------------------------------------------------------------------