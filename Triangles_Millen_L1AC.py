for x in range (1,6):       #loop for 5 rows
    print("*"*x)            #prints "*" multiply by x(ascending 1-5) --> next row (enter)
print("\n")                 #prints double enter for the next triangle

s = 4                       #assigning var s = 4
for x in range (1,6):       #loop for 5 rows
    print(s*" "+x*"*")      #prints "space" multiply by s and "*" multiply by x(ascending 1-5) --> next row (enter)
    s -= 1                  #var s decreasing by 1
print("\n")                 #prints double enter for the next triangle

s = 5                       #assigning var s = 5
for x in range (1,6):       #loop for 5 rows
    print(s * "*")          #prints "*" multiply by s --> next row (enter)
    s-=1                    #var s decreasing by 1
print("\n")                 #prints double enter for the next triangle

s = 5                       #assigning var s = 5
for x in range (0,5):       #loop for 5 rows
    print(x * " " + s * "*")#prints "space" multiply by x and "*" multiply by s --> next row (enter)
    s-=1                    #var s decreasing by 1
print("\n")                 #prints double enter for the next triangle

s = 4                       #assigning var s = 4
for x in range(0, 5):       #loop for 5 rows
    y = x * 2 + 1           #var y = x*2+1
    print(s * str(" ") + y * str("*"))#prints "space" multiply by s and "*" multiply by x --> next row (enter)
    s -= 1                  #var s decreasing by 1
print("\n")                 #prints double enter for the diamond

s = 4                       #assigning var s = 4
for x in range(0, 5):       #loop for 5 rows
    y = x * 2 + 1           #var y = x*2+1
    print(s * str(" ") + y * str("*"))#prints "space" multiply by s and "*" multiply by x --> next row (enter)
    s -= 1                  #var s decreasing by 1
s = 7                       #assigning var s = 7
for x in range(1, 5):       #loop for 4 rows
    print(x * " " + s * ("*"))#prints "space" multiply by x and "*" multiply by s --> next row (enter)
    s -= 2                  #var s decreasing by 2
