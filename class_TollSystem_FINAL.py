class Vehicle: #Parent Class
    # init method or constructor
    def __init__(self,cPriceM,bPriceM,tPriceM,cPriceP,bPriceP,tPriceP):
        self.cPriceM = cPriceM  #Car Price Meruya
        self.bPriceM = bPriceM  #Bus Price Meruya
        self.tPriceM = tPriceM  #Truck Price Meruya

        self.cPriceP = cPriceP  #Car Price Pondok Aren
        self.bPriceP = bPriceP  #Bus Price Pondok Aren
        self.tPriceP = tPriceP  #Truck Price Pondok Aren

    def getcPriceM(self):
        return self.cPriceM

    def getbPriceM(self):
        return self.bPriceM

    def gettPriceM(self):
        return self.tPriceM

    def getcPriceP(self):
        return self.cPriceP

    def getbPriceP(self):
        return self.bPriceP

    def gettPriceP(self):
        return self.tPriceP


class TollBooth(Vehicle): #Child Class

    def __init__(self,
                 cPriceM, bPriceM, tPriceM,
                 cPriceP, bPriceP, tPriceP,
                 countCar, countBus, countTruck):

        Vehicle.__init__(self,
                         cPriceM,bPriceM,tPriceM,
                         cPriceP,bPriceP,tPriceP)

        self.countCar = countCar        #Car Counter
        self.countBus = countBus        #Bus Counter
        self.countTruck = countTruck    #Truck Counter

    def calculationTBM(self):   #Price Calculation (Meruya)
        x = int(self.countCar) * self.cPriceM
        y = int(self.countBus) * self.bPriceM
        z = int(self.countTruck) * self.tPriceM
        totalTBM = x + y + z
        return totalTBM

    def printAllTBM(self):  #prints number of vehicles pass through Meruya Toll Booth
        timesP = 20
        print(timesP * "-")
        print("car\t\tBus\t\tTruck")
        print(timesP * "-")
        print(str(self.countCar) + "\t\t" + str(self.countBus) + "\t\t" + str(self.countTruck))
        print(timesP * "-")

    def calculationTBP(self):   #Price Calculation (Pondok Aren)
        x = int(self.countCar) * self.cPriceP
        y = int(self.countBus) * self.bPriceP
        z = int(self.countTruck) * self.tPriceP
        totalTBP = x + y + z
        return totalTBP

    def printAllTBP(self):  #prints number of vehicles pass through Pondok Aren Toll Booth
        timesP = 20
        print(timesP * "-")
        print("car\t\tBus\t\tTruck")
        print(timesP * "-")
        print(str(self.countCar) + "\t\t" + str(self.countBus) + "\t\t" + str(self.countTruck))
        print(timesP * "-")

cPriceM = 6000  #Car Price -- Meruya Toll Booth
bPriceM = 8000  #Bus Price  -- Meruya Toll Booth
tPriceM = 10000 #Truck Price -- Meruya Toll Booth

cPriceP = 18000 #Car Price -- Pondok Aren Toll Booth
bPriceP = 20000 #Bus Price -- Pondok Aren Toll Booth
tPriceP = 25000 #Truck Price -- Pondok Aren Toll Booth

countCar = 0    #Car Counter
countBus = 0    #Bus Counter
countTruck= 0   #Truck Counter


a = Vehicle(cPriceM,bPriceM,tPriceM,    #Variables to be passed to Vehicle class
            cPriceP,bPriceP,tPriceP)

m1 = TollBooth(cPriceM, bPriceM, tPriceM,   #Meruya --Toll booth 1
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

m2 = TollBooth(cPriceM, bPriceM, tPriceM,   #Meruya --Toll booth 2
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

m3 = TollBooth(cPriceM, bPriceM, tPriceM,   #Meruya --Toll booth 3
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

m4 = TollBooth(cPriceM, bPriceM, tPriceM,   #Meruya --Toll booth 4
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

m5 = TollBooth(cPriceM, bPriceM, tPriceM,   #Meruya --Toll booth 5
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

p1 = TollBooth(cPriceM, bPriceM, tPriceM,   #Pondok Aren --Toll Booth 1
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

p2 = TollBooth(cPriceM, bPriceM, tPriceM,   #Pondok Aren --Toll Booth 2
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

p3 = TollBooth(cPriceM, bPriceM, tPriceM,   #Pondok Aren --Toll Booth 3
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

p4 = TollBooth(cPriceM, bPriceM, tPriceM,   #Pondok Aren --Toll Booth 4
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)

p5 = TollBooth(cPriceM, bPriceM, tPriceM,   #Pondok Aren --Toll Booth 5
              cPriceP, bPriceP, tPriceP,
              countCar, countBus, countTruck)



timesE = 55 #to multiply "=" sign
timesS = 15 #to multiply space
print(timesE*"=",   #prints header
      "\n",timesS*" ","Toll Payment Systems"
      "\n",timesS*" "," PT Jasa Marga, Tbk."
      "\n"+timesE*"=")

otherTollGate = "Y"
while otherTollGate != "N":   #keep looping if other toll gate doesn't equal "N"
    tollGate = input("1. Meruya\n"              #Asks for which toll gate
                     "2. Pondok Aren\n"
                     "(Input With String)\n"
                     "Location of Toll Gate : ")
    tollGate = tollGate.upper()

    if tollGate == "MERUYA":    #if toll gate equals "Meruya"
        otherTollBooth = "Y"
        while otherTollBooth != "N":    #keep looping if other toll booth doesn't equal "N"
            tollBooth = int(input("1. Booth 1\n"    #Asks for which toll booth
                              "2. Booth 2\n"
                              "3. Booth 3\n"
                              "4. Booth 4\n"
                              "5. Booth 5\n"
                              "Which Toll booth : "))

            otherVehicle = "Y"
            while otherVehicle != "N":  #keep looping if other other vehicle doesn't equal "N"
                vehicle = int(input("Category of Vehicles"  #Asks for which vehicle
                                    "\n1. Car"
                                    "\n2. Bus"
                                    "\n3. Truck"))
                #carMeruya
                if vehicle == 1:    #if vehicle equals one
                    print("Fee",a.getcPriceM())
                    if tollBooth == 1:
                        m1.countCar += 1    #incereases vehicle's counter
                    elif tollBooth == 2:
                        m2.countCar += 1
                    elif tollBooth == 3:
                        m3.countCar += 1
                    elif tollBooth == 4:
                        m4.countCar += 1
                    elif tollBooth == 5:
                        m5.countCar += 1

                #busMeruya
                elif vehicle == 2:   #if vehicle equals two
                    print("Fee",a.getbPriceM())
                    if tollBooth == 1:
                        m1.countBus += 1    #incereases vehicle's counter
                    elif tollBooth == 2:
                        m2.countBus += 1
                    elif tollBooth == 3:
                        m3.countBus += 1
                    elif tollBooth == 4:
                        m4.countBus += 1
                    elif tollBooth == 5:
                        m5.countBus += 1

                #truckMeruya
                if vehicle == 3:    #if vehicle equals three
                    print("Fee", a.gettPriceM())
                    if tollBooth == 1:
                        m1.countTruck += 1  #incereases vehicle's counter
                    elif tollBooth == 2:
                        m2.countTruck += 1
                    elif tollBooth == 3:
                        m3.countTruck += 1
                    elif tollBooth == 4:
                        m4.countTruck += 1
                    elif tollBooth == 5:
                        m5.countTruck += 1
                otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")  #asks for other vehicle
                otherVehicle = otherVehicle.upper()
            otherTollBooth = input("\nIs there any other toll booth (Y/N)? \n") #asks for other toll booth
            otherTollBooth = otherTollBooth.upper()

    elif tollGate == "PONDOK AREN": #if toll gate equals "Pondok Aren"
        otherTollBooth = "Y"
        while otherTollBooth != "N":    #keep looping if other  toll booth doesn't equal "N"
            tollBooth = int(input("1. Booth 1\n"    #asks for which toll booth
                                  "2. Booth 2\n"
                                  "3. Booth 3\n"
                                  "4. Booth 4\n"
                                  "5. Booth 5\n"
                                  "Which Toll booth : "))

            otherVehicle = "Y"
            while otherVehicle != "N":  #keep looping if other vehicle doesn't equal "N"
                vehicle = int(input("Category of Vehicles"
                                    "\n1. Car"
                                    "\n2. Bus"
                                    "\n3. Truck"))
                # carMeruya
                if vehicle == 1:            #if vehicle equals one
                    print("Fee", a.getcPriceP())
                    if tollBooth == 1:
                        p1.countCar += 1    #incereases vehicle's counter
                    elif tollBooth == 2:
                        p2.countCar += 1
                    elif tollBooth == 3:
                        p3.countCar += 1
                    elif tollBooth == 4:
                        p4.countCar += 1
                    elif tollBooth == 5:
                        p5.countCar += 1

                # busMeruya
                if vehicle == 2:            #if vehicle equals two
                    print("Fee", a.getbPriceP())
                    if tollBooth == 1:
                        p1.countBus += 1    #incereases vehicle's counter
                    elif tollBooth == 2:
                        p2.countBus += 1
                    elif tollBooth == 3:
                        p3.countBus += 1
                    elif tollBooth == 4:
                        p4.countBus += 1
                    elif tollBooth == 5:
                        p5.countBus += 1

                # truckMeruya
                if vehicle == 3:         #if vehicle equals three
                    print("Fee", a.gettPriceP())
                    if tollBooth == 1:
                        p1.countTruck += 1  #incereases vehicle's counter
                    elif tollBooth == 2:
                        p2.countTruck += 1
                    elif tollBooth == 3:
                        p3.countTruck += 1
                    elif tollBooth == 4:
                        p4.countTruck += 1
                    elif tollBooth == 5:
                        p5.countTruck += 1

                otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")  #asks for other vehicle
                otherVehicle = otherVehicle.upper()
            otherTollBooth = input("\nIs there any other toll booth (Y/N)? \n") #asks for other toll booth
            otherTollBooth = otherTollBooth.upper()
    otherTollGate = input("\nIs there any other toll Gate (Y/N)? \n")   #asks for other toll gate
    otherTollGate = otherTollGate.upper()

#PRINTS EVERYTHING
print("Location: Meruya\nBooth: 01")
m1.printAllTBM()
print("Total revenue: \tRp.",m1.calculationTBM())
print()

print("Location: Meruya\nBooth: 02")
m2.printAllTBM()
print("Total revenue: \tRp.",m2.calculationTBM())
print()

print("Location: Meruya\nBooth: 03")
m3.printAllTBM()
print("Total revenue: \tRp.",m3.calculationTBM())
print()

print("Location: Meruya\nBooth: 04")
m4.printAllTBM()
print("Total revenue: \tRp.",m4.calculationTBM())
print()

print("Location: Meruya\nBooth: 05")
m5.printAllTBM()
print("Total revenue: \tRp.",m5.calculationTBM())
print()

print("Location: Pondok Aren\nBooth: 01")
p1.printAllTBP()
print("Total revenue: \tRp.",p1.calculationTBP())
print()

print("Location: Pondok Aren\nBooth: 02")
p2.printAllTBP()
print("Total revenue: \tRp.",p2.calculationTBP())
print()

print("Location: Pondok Aren\nBooth: 03")
p3.printAllTBP()
print("Total revenue: \tRp.",p3.calculationTBP())
print()

print("Location: Pondok Aren\nBooth: 04")
p4.printAllTBP()
print("Total revenue: \tRp.",p4.calculationTBP())
print()

print("Location: Pondok Aren\nBooth: 05")
p5.printAllTBP()
print("Total revenue: \tRp.",p5.calculationTBP())

grandTotalRevenue = int(m1.calculationTBM())+ int(m2.calculationTBM())+int(m3.calculationTBM())+int(m4.calculationTBM())+int(m5.calculationTBM()+
                    int(p1.calculationTBP())+ int(p2.calculationTBP())+int(p3.calculationTBP())+int(p4.calculationTBP())+int(p5.calculationTBP()))
print("Grand total revenue: Rp.",grandTotalRevenue)
