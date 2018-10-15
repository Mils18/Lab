# Class Quiz -- Hotel Operating System
# Millen Dwiputra -- 2201797531
# ITP Lab -- L1AC

import datetime
class Room:
    def __init__(self,deluxeP,suitesP,pSuitesP):    #initializes attributes
        self.deluxeP = deluxeP  #deluxe price
        self.suitesP = suitesP  #suites price
        self.pSuitesP = pSuitesP    #presidential suites price

    def getDeluxePrice(self):
        return self.deluxeP

    def getSuitesPrice(self):
        return self.suitesP

    def getPSuitesPrice(self):
        return self.pSuitesP

class Hotel(Room):      #define a Hotel class which inherits from Room class
    def __init__(self): #initializes
        Room.__init__(self,deluxeP,suitesP,pSuitesP)    #initializes parent's atributes
        self.deluxeList = []        #A list for deluxe customer's name
        self.deluxeTimeInList = []  #A list for deluxe check in time
        self.deluxeTimeOutList = [] #A list fot deluxe check out time

        self.suitesList = []        #A list for suites customer's name
        self.suitesTimeInList = []  #A list for suites check in time
        self.suitesTimeOutList = [] #A list fot suites check out time

        self.pSuitesList = []       #A list for presidential suites customer's name
        self.pSuitesTimeInList = [] #A list for presidential suites check in time
        self.pSuitesTimeOutList = []#A list fot presidential suites check out time

        self.revenue = []           #A list for revenue after customer's checked out


    def printAll(self):             #define a function
        for i in range(len(self.deluxeList)):       #prints deluxe customer's name with check in time
            print("DELUXE ROOM")
            print(self.deluxeList[i])
            print(self.deluxeTimeInList[i])
            print()
        if len(self.deluxeList) == 2:               #informs that it is fully booked if there are 2 customers
            print("DELUXE ROOM IS FULLY BOOKED\n")

        for i in range(len(self.suitesList)):       #prints suites customer's name with check in time
            print("SUITES ROOM")
            print(self.suitesList[i])
            print(self.suitesTimeInList[i])
            print()
        if len(self.suitesList) == 2:
            print("SUITES ROOM IS FULLY BOOKED\n")  #informs that it is fully booked if there are 2 customers

        for i in range(len(self.pSuitesList)):      #prints presidential suites customer's name with check in time
            print("PRESIDENTIAL SUITES ROOM")
            print(self.pSuitesList[i])
            print(self.pSuitesTimeInList[i])
            print()
        if len(self.pSuitesList) == 2:              #informs that it is fully booked if there are 2 customers
            print("PRESIDENTIAL SUITES ROOM IS FULLY BOOKED\n")

    def deluxeCalculation(self,name1):          #define a function to calculate revenue of deluxe room
        z = self.deluxeList.index(name1)        #to make sure a specific index by its name
        calculateTime = self.deluxeTimeOutList[z] - self.deluxeTimeInList[z]    #determines how long they stayed
        calculateTime = str(calculateTime)
        d = datetime.datetime.strptime(calculateTime, "%H:%M:%S")
        calculatePrice = int(d.second)*self.deluxeP     #every second times to deluxe price
        self.revenue.append(calculatePrice)             #appends calculated deluxe price to revenue list

    def suitesCalculation(self,name2):          #define a function to calculate revenue of suites room
        z = self.suitesList.index(name2)        #to make sure a specific index by its name
        calculateTime = self.suitesTimeOutList[z] - self.suitesTimeInList[z]    #determines how long they stayed
        calculateTime = str(calculateTime)
        d = datetime.datetime.strptime(calculateTime, "%H:%M:%S")
        calculatePrice = int(d.second)*self.suitesP     #every second times to deluxe price
        self.revenue.append(calculatePrice)         #appends calculated deluxe price to revenue list

    def pSuitesCalculation(self,name3):         #define a function to calculate revenue of presidential suites room
        z = self.pSuitesList.index(name3)       #to make sure a specific index by its name
        calculateTime = self.pSuitesTimeOutList[z] - self.pSuitesTimeInList[z]  #determines how long they stayed
        calculateTime = str(calculateTime)
        d = datetime.datetime.strptime(calculateTime, "%H:%M:%S")
        calculatePrice = int(d.second) * self.pSuitesP  #every second times to deluxe price
        self.revenue.append(calculatePrice)          #appends calculated deluxe price to revenue list


#   ---------------MAIN------------------
deluxeP = 1000000
suitesP = 3000000
pSuitesP = 5000000
#arguments to be passed

a = Room(deluxeP,suitesP,pSuitesP)          #An object of Room class
b = Hotel()                                 #An object of Hotel class

timesE = 68 #to multiply "=" sign
timesS = 15 #to multiply space
print(timesE*"=",   #prints header
      "\n",timesS*" ","Welcome To The Hotel California"
      "\n"+timesE*"=")

num=0
while num !=6:  #keeps looping if num not equals six
    num = int(input("\nPlease input with a number:\n"
                    "1. Check in\n"
                    "2. Check out\n"
                    "3. Show booked room\n"
                    "4. Check Availability\n"
                    "5. Revenue\n"
                    "6. Exit Program\n"))

    if num == 1:    #CHECK IN
        room = int(input("\nPlease input with a number:\n"
                     "1. Deluxe\n"
                     "2. Suites\n"
                     "3. Presidential Suites\n"))

        if room == 1:   #DELUXE ROOM
            if int(len(b.deluxeList)) < 2:      #If there is unbooked room
                print("DELUXE ROOM")
                name1 = input("Input name :")
                checkInTime = datetime.datetime.now().replace(microsecond=0)
                b.deluxeList.append(name1)
                b.deluxeTimeInList.append(checkInTime)

            else:                               #If there is no more room left
                print("Sorry deluxe room is fully booked\n")

        if room == 2:   #SUITES ROOM
            if int(len(b.suitesList)) < 2:      #If there is unbooked room
                print("SUITES ROOM")
                name2 = input("Input name :")
                checkInTime = datetime.datetime.now().replace(microsecond=0)
                b.suitesList.append(name2)
                b.suitesTimeInList.append(checkInTime)

            else:                               #If there is no more room left
                print("Sorry suites room is fully booked\n")

        if room == 3:  # PRESIDENTIAL SUITES ROOM
            if int(len(b.pSuitesList)) < 2:     #If there is unbooked room
                print("PRESIDENTIAL SUITES ROOM")
                name3 = input("Input name :")
                checkInTime = datetime.datetime.now().replace(microsecond=0)
                b.pSuitesList.append(name3)
                b.pSuitesTimeInList.append(checkInTime)

            else:                               #If there is no more room left
                print("Sorry Presidential suites room is fully booked\n")


    elif num ==2:   #CHECK OUT
        room = int(input("Please input with a number:\n"
                     "1. Deluxe\n"
                     "2. Suite\n"
                     "3. Presidential Suite\n"))

        if room == 1:       #DELUXE ROOM
            print("DELUXE ROOM")
            name1 = input("Input name :")   #input customer's name to be checked out
            checkOutTime = datetime.datetime.now().replace(microsecond=0)
            b.deluxeTimeOutList.append(checkOutTime)
            b.deluxeCalculation(name1)
            z = b.deluxeList.index(name1)
            #clears everything, so it can be booked by the others
            b.deluxeList.pop(z)
            b.deluxeTimeInList.pop(z)
            b.deluxeTimeOutList.pop(z)

        if room == 2:       #SUITES ROOM
            print("SUITES ROOM")
            name2 = input("Input name :")   #input customer's name to be checked out
            checkOutTime = datetime.datetime.now().replace(microsecond=0)
            b.suitesTimeOutList.append(checkOutTime)
            b.suitesCalculation(name2)
            z = b.suitesList.index(name2)
            # clears everything, so it can be booked by the others
            b.suitesList.pop(z)
            b.suitesTimeInList.pop(z)
            b.suitesTimeOutList.pop(z)

        if room == 3:        #PRESIDENTIAL SUITES ROOM
            print("PRESIDENTIAL SUITES ROOM")
            name3 = input("Input name :")   #input customer's name to be checked out
            checkOutTime = datetime.datetime.now().replace(microsecond=0)
            b.pSuitesTimeOutList.append(checkOutTime)
            b.pSuitesCalculation(name3)
            z = b.pSuitesList.index(name3)
            # clears everything, so it can be booked by the others
            b.pSuitesList.pop(z)
            b.pSuitesTimeInList.pop(z)
            b.pSuitesTimeOutList.pop(z)


    elif num == 3:  #Shows booked rooms
        b.printAll()

    elif num ==4:   #Shows Room Availibility
        x = 2 - int(len(b.deluxeList))
        print("there is/are",str(x),"deluxe room(s) left")

        y = 2 - int(len(b.suitesList))
        print("there is/are",str(y),"suites room(s) left")

        z = 2 - int(len(b.pSuitesList))
        print("there is/are",str(z),"presidential suites room(s) left")

    elif num ==5:    #Shows grand revenue of the hotel
        grandrevenue = 0
        for i in range(len(b.revenue)):
            grandrevenue += b.revenue[i]
        print("It uses the actual time, just pretend every second is 1 day")
        print("GRAND REVENUE = Rp.", str(grandrevenue))








