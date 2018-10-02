#Lambda Calculator Assignment
#Millen Dwiputra - 2201797531 - L1AC


num1 = int(input("input first number = "))  #A variable to input first number
print("Binary Operator")                    #Prints "Binary Operator"
operator = input("input with [+,-,*,/,^] = ")#shows operator available to be inputted
num2 = int(input("input second number = ")) #A variable to input second number


if operator == "+":                         #if the operator's "+"
    x = lambda num1,num2 : num1 + num2      #A lambda function to sum first number with second number
    print("RESULT = ",x(num1,num2))         #prints final result


elif operator == "-":                       #if the operator's "+"
    x = lambda num1,num2 : num1 - num2      #A lambda function to substract first number with second number
    print("RESULT",x(num1,num2))            #prints final result

elif operator == "*":                       #if the operator's "*"
    x = lambda num1,num2 : num1 * num2      #A lambda function to multiply first and second number
    print("RESULT",x(num1,num2))            #prints final result

elif operator == "/":                       #if the operator's "/"
    x = lambda num1,num2 : num1 / num2      #A lambda function to divide first number with second number
    print("RESULT",x(num1,num2))            #prints final result

elif operator == "^":                       #if the operator's "^"
    x = lambda num1,num2 : num1 ** num2     #A lambda function to power first number with second number
    print("RESULT",x(num1,num2))            #prints final result
