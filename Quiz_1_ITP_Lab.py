
temp = 5
top = []
middle = []
bottom= []
stop = False
def put(x,y):
    if x == "top":
        if len(top) == 15:
            print("Already full.")
        else:
            top.append(y)
    elif x == "middle":
        if len(top) == 15:
            print("Already full.")
        else:
            middle.append(y)
    elif x == "bottom":
        if len(top) == 15:
            print("Already full.")
        else:
            bottom.append(y)


def take(x, y):
    if x == "top":
        for i in top:
            top.pop()
    elif x == "middle":
        middle.pop(x)
    elif x == "bottom":
        bottom.pop(x)

def lights(x):
    if x == "on":
        return True
    elif x =="off":
        return False

def tempChange(x):
    global temp
    temp = x
    return temp

def checkcontents(x):
    if x =="top":
        print(top)
    elif x =="middle":
        print(middle)
    elif x =="bottom":
        print(bottom)

while stop == False:
    x = int(input("Input a number\n1. Add item to Fridge\n2. Remove item from fridge\n3.Change the temparature\n4.Lights management\n5. Check contents\n "))
    if x == 1:
        x = input("Input which part of the fridge to open:\ntop/middle/bottom \n ")
        x = x.lower()
        y =input("Item to put: ")
        y =y.lower()
        put(x,y)
    elif x==2:
        x = input("Input which part of the fridge to open:\ntop/middle/bottom \n ")
        x =x.lower()
        y = input("Input item to take")
        y= y.lower()
        take(x,y)

    elif x ==3:
        x = input("Input number for temperature change")
        tempChange(x)

    elif x ==4:
        x = input("Type in on or off: ")
        x = x.lower()
        lights(x)
    elif x ==5:
        x = input("Input which part of the fridge to open:\ntop/middle/bottom \n ")
        checkcontents(x)

    x =input("Action again[y/n]")
    if x == y:
        stop == False
    else:
        stop == True



