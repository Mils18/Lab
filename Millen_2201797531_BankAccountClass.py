account = list()        #An empty list for atm holder name
balance = list()        #An empty list for atm holder balance
x1 = list()             #An empty list to match

class Atm:
    def __init__(self, firstName, lastName):    #defines class atributes
        self.firstName = firstName
        self.lastName = lastName

    def register(self):     #to register a new account
        global account
        global balance
        balance.append(0)
        account.append(self.firstName + " " + self.lastName)
        print ("Congratulations",self.firstName + " " + self.lastName, "!!! Your Account has been registered with account number \'00"+str(len(account))+"\'\n")

    def showAcc(self):      #to show registered accounts
        x = 1               #declares account number
        for i in range (len(account)):
            print ("\nAccount Number : 00"+str(x), "\nName : " ,account[i], "\nBalance : Rp. " , balance[i],"\n")
            x+=1            #account number +1
        print()

    def deposit(self):      #to deposit money
        global account
        global balance
        print("Please enter your account number")
        a = int(input("ex [001, 002, 003] : "))
        b = int(input ("Amounts : Rp. "))
        a1 = a - 1                  #declares account's index
        x = str(balance[a1])        #to show previous balance
        balance[a1] += b            #adds money
        print("Previous Balance : Rp.", x, "\nCurrent Balance : Rp.", balance[a1])
        print ()

    def withdraw(self):             #to withdraw money
        global account
        global balance
        print("Please enter your account number")
        a = int(input("ex [001, 002, 003] : "))
        b = int(input ("Amounts : Rp. "))
        a1 = a - 1                  #declares account's index

        if balance[a1] >= b:        #If the balance is sufficient
            x = str(balance[a1])    #to show previous balance
            balance[a1] -= b
            print("Previous Balance : Rp.", x, "\nCurrent Balance : Rp.", balance[a1])
        else:                       #If the balance is insufficient
            print("Insufficient balance in account number \'00"+str(a)+"\'")
        print ()

    def transfer(self):     #to transfer from one account to another
        global account
        global balance
        global x1
        a = int(input("Sender account number : "))
        b = int(input("Receiver account number : "))
        print()

        a1 = a - 1  #declares account's index
        b1 = b - 1  #declares account's index

        for x in range (len(account)):  #Loops from index 0 to lenght of account -1
            x1.append(x)                #appends to x1 list

        if a1 in x1 and b1 in x1:       #Check if accounts are registered
            c = int(input("Amounts : Rp. "))
            if balance[a1] >= c:        #If the balance of sender is sufficient
                balance[a1] -= c        #substracts sender's balance
                balance[b1] += c        #adds receiver's balance
            else:                       #If the balance of sender is insufficient
                print("Insufficient balance in account number \'00"+str(a)+"\'")
        else:                           #If there's unregistered account
            print("Invalid Account Number")
        print()

    def delete(self):
        global account
        global balance
        a = int(input("Account number to delete :"))

        b = input ("are you sure? [Y/N] :")
        b = b.upper()               #Uppercases b input for Yes or No

        a1 = a - 1                  #declares account number
        if b == "Y":                #If it is a Yes
            del account[a1]         #removes account's name
            del balance[a1]         #removes account's balance
            print('account number \'00'+str(a)+'\' has been deleted\n')
        elif b =="N":               #If it is a No
            print ("\n")
        else :
            print ("Invalid Key\n")

###
num1 = 0            #declares num1 equals one
while num1 != 7:    #keeps looping while num1 isn't "7"
    print ("ATM\n1. Create A New Account\n2. Show Registered Accounts\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Delete Account\n7. Exit")
    #prints menu options
    num1 = int(input("choose :"))                                                       #to input num1 to choose menu 1-7
    print()                                                                             #prints enter
    if len(account) == 0 and num1 > 1 and num1 < 7:                                     #if the account hasn't been created yet
        print("There's no bank account\nPlease create a new one by choosing \'1\'\n")   #prints "there's no bank account"

    elif num1 == 1:                                                                     #If num1 equals one
        firstName = input("Input first name :")                                         #to input first name
        lastName = input("Input last name :")                                           #to input last name
        c = Atm(firstName, lastName)                                                    #atributes to be passed to the parameters
        c.register()                                                                    #calls register function

    elif num1 == 2:     #If num1 equals two
        c.showAcc()     #calls showAcc function

    elif num1 == 3:     #If num1 equals three
        c.deposit()     #calls deposit function

    elif num1 == 4:     #If num1 equals four
        c.withdraw()    #calls withdraw function

    elif num1 == 5:     #If num1 equals five
        c.transfer()    #calls transfer function

    elif num1 == 6:     #If num1 equals six
        c.delete()      #calls delete function

    elif num1 == 7:     #If num1 equals seven
        print ("Thank you for using this ATM")  #prints "thank you" and break

    else :
        print ("INVALID NUMBER\nPlease input with \'1 - 7 \'\n") #prints "invalid" if num1 smaller than one or bigger than 7

