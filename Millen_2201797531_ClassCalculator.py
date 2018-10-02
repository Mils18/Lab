#Class Calculator
#Millen Dwiputra - 2201797531 - L1AC

class Calculator :                  #defines Class as an object

    def __init__(self,num1,num2):   #defines class atributes
        self.num1 = num1            #calls itself
        self.num2 = num2            #calls itself

    #below is to define class methods
    def addition(self):                 #defines addition function
        x = self.num1 + self.num2       #Sums first number with second number
        print("RESULT = ",str(x))       #prints final Result

    def substraction(self):             #defines substration function
        x = self.num1 - self.num2       #Substracts first number with second number
        print("RESULT = ",str(x))       #prints final Result

    def multiplication(self):           #defines multiplication function
        x = self.num1 * self.num2       #multiplies first number with second number
        print("RESULT = ",str(x))       #prints final Result

    def division(self):                 #defines division function
        x = self.num1 / self.num2       #divides first number with second number
        print("RESULT = ",str(x))       #prints final Result

num1 = int(input("input 1 : "))                 #First number to input
print("Binary Operator")                        #Prints "Binary Operator"
operator = input("input with [+,-,*,/,^] = ")   #shows operator available to be inputted
num2 = int(input("input 2 : "))                 #Second number to input

c = Calculator(num1, num2)      #inputs the atributes to be passed to the parameters

if operator == "+":             #if the operator's "+"
    c.addition()                #calls addition function which is in class methods

elif operator == "-":           #if the operator's "-"
    c.substraction()            #calls substraction function which is in class methods

elif operator == "*":           #if the operator's "*"
    c.multiplication()          #calls multiplication function which is in class methods

elif operator == "/":           #if the operator's "/"
    c.division()                #calls division function which is in class methods