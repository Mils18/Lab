num1 = input("Input Number = ") #input numbers (max 3 digits)
tokens = list(num1)

dict = {        #dictionary1 for 0-9
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        }
dict2 = {       #dictionary2 (EXCEPTIONAL)
        "0": "",
        "2": "twen",
        "3": "thir",
        "4": "for",
        "5": "fif",
        "6": "six",
        "7": "seven",
        "8": "eigh",
        "9": "nine",
        }

print("print input = ",num1)   #to recheck inputted numbers
print("tokens = ",tokens)      #to recheck numbers that are splitted and assigned into tokens
print("lenght of tokens = ",len(tokens))   #to recheck the lenght of tokens

def ones():                       #defining a function
    global tokens                   #to access tokens variable
    #len tokens 1
    x=len(tokens)-1                 #last number
    print(dict[tokens[x]],end=' ')  #print last number


def tens ():                        #defining a function
    global tokens                   #to access tokens variable
    #len tokens 2
    x = len(tokens)-2               #second last number
    y = len(tokens)-1               #last number

    if int(tokens[x]) == 1:         #if the second last number is 1 (10-19)
        if int(tokens[y])== 0:      #if the last number is 0 (10)
            print("ten")            #prints "ten"
        elif int(tokens[y])== 1:    #if the last number is 1 (11)
            print("eleven")         #prints "eleven"
        elif int(tokens[y])== 2:    #if the last number is 2 (12)
            print("twelve")         #prints "twelve"
        elif int(tokens[y])== 3 or int(tokens[y])==5:       #if the last number is 3 or 5(13 or 15)
            print(dict2[tokens[y]] + "teen ", end=' ')      #prints "thirteen" or "fifteen"
        else:
            print(dict[tokens[y]]+"teen") #the rest numbers (14, 16-19)

    else:        #if the second last number is 2 - 9 (20-99)
        print(dict2[tokens[x]] + "ty", end=' ')   #prints second last number + ty
        ones()   #call ones function

def hundreds ():                     #defining a function
    global tokens                   #to access tokens variable
    #len tokens 3
    z = len(tokens)-3               #third last number
    print(dict[tokens[z]] + " hundred ",end="")   #prints third last number + "hundred"
    tens()                       #call tens function

if len(tokens) == 1:    #if the inputted number is 1 digit
    ones()            #call ones function

elif len(tokens) == 2:  #if the inputted number is 2 digit
    tens()           #call tens function

elif len(tokens) == 3:  #if the inputted number is 3 digit
    hundreds()           #call hundreds function
