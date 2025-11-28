c = input("please enter your Hexadecimal color code : #")
if len(c)==3 :
    c = 2*c[0]+2*c[1]+2*c[2]
cal = str(hex(int("ffffff", 16) - int(c, 16))[2:])
print(cal if len(cal)==6 else (6-len(cal))*"0"+cal)