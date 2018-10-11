class Vehicle:
    def __init__(self,cPriceM,bPriceM,tPriceM,cPriceP,bPriceP,tPriceP):
        self.cPriceM = cPriceM
        self.bPriceM = bPriceM
        self.tPriceM = tPriceM

        self.cPriceP = cPriceP
        self.bPriceP = bPriceP
        self.tPriceP = tPriceP

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


class TollBooth(Vehicle):
    def __init__(self,
                 cPriceM,bPriceM,tPriceM,
                 cPriceP,bPriceP,tPriceP,
                 countCarM,countBusM,countTruckM
                 ,countCarP,countBusP,countTruckP):

        Vehicle.__init__(self,
                         cPriceM,bPriceM,tPriceM,
                         cPriceP,bPriceP,tPriceP)

        self.countCarM = countCarM
        self.countBusM = countBusM
        self.countTruckM = countTruckM

        self.countCarP = countCarP
        self.countBusP = countBusP
        self.countTruckP = countTruckP

    def calculationTBM(self):
        x = int(self.countCarM) * self.cPriceM
        y = int(self.countBusM) * self.bPriceM
        z = int(self.countTruckM) * self.tPriceM
        totalTBM = x + y + z
        return totalTBM

    def printAllTBM(self):
        timesP = 20
        print("Location: Meruya")
        print(timesP * "-")
        print("car\t\tBus\t\tTruck")
        print(timesP * "-")
        print(str(self.countCarM) + "\t\t" + str(self.countBusM) + "\t\t" + str(self.countTruckM))
        print(timesP * "-")

    def calculationTBP(self):
        x = int(self.countCarP) * self.cPriceP
        y = int(self.countBusP) * self.bPriceP
        z = int(self.countTruckP) * self.tPriceP
        totalTBP = x + y + z
        return totalTBP

    def printAllTBP(self):
        timesP = 20
        print("Location: Pondok Aren")
        print(timesP * "-")
        print("car\t\tBus\t\tTruck")
        print(timesP * "-")
        print(str(self.countCarP) + "\t\t" + str(self.countBusP) + "\t\t" + str(self.countTruckP))
        print(timesP * "-")


# class TollGate(TollBooth):
#     def __init__(self,cPriceM,bPriceM,tPriceM,
#                  cPriceP,bPriceP,tPriceP,
#                  countCarM,countBusM,countTruckM,
#                  countCarP,countBusP,countTruckP):
#
#         TollBooth.__init__(self,
#                                 cPriceM,bPriceM,tPriceM,
#                                 cPriceP,bPriceP,tPriceP,
#                                 countCarM,countBusM,countTruckM,
#                                 countCarP,countBusP,countTruckP)
#
#     def printMeruya(self):
#         TollBooth.printAllTBM()

    # def calculationTBM(self):
    #     x = int(self.countCarM) * self.cPriceM
    #     y = int(self.countBusM) * self.bPriceM
    #     z = int(self.countTruckM) * self.tPriceM
    #     totalTBM = x + y + z
    #     return totalTBM


    # def printAllTBM(self):
    #     timesP = 20
    #     print(timesP * "-")
    #     print("car\t\tBus\t\tTruck")
    #     print(timesP * "-")
    #     print(str(self.countCarM) + "\t\t" + str(self.countBusM) + "\t\t" + str(self.countTruckM))
    #     print(timesP * "-")




cPriceM = 6000
bPriceM = 8000
tPriceM = 10000

cPriceP = 18000
bPriceP = 20000
tPriceP = 25000

countCarM = 0
countBusM = 0
countTruckM = 0
countCarP = 0
countBusP = 0
countTruckP = 0

a = Vehicle(cPriceM,bPriceM,tPriceM,cPriceP,bPriceP,tPriceP)# totalTB = 0

# meruya = TollGate(cPriceM,bPriceM,tPriceM,cPriceP,bPriceP
#                   ,tPriceP,countCarM,countBusM,countTruckM
#                   ,countCarP,countBusP,countTruckP)
#
# pondokAren = TollGate(cPriceM,bPriceM,tPriceM,cPriceP,bPriceP
#                     ,tPriceP,countCarM,countBusM,countTruckM
#                     ,countCarP,countBusP,countTruckP)


otherTollGate = "Y"
timesE = 55
timesS = 15


print(timesE*"=",
      "\n",timesS*" ","Toll Payment Systems"
      "\n",timesS*" "," PT Jasa Marga, Tbk."
      "\n"+timesE*"=")

while otherTollGate != "N":
    tollGate = input("1. Meruya\n"
                     "2. Pondok Aren\n"
                     "Location of Toll Gate : ")
    tollGate = tollGate.upper()
    otherVehicle = "Y"
    if tollGate == "MERUYA":
        while otherVehicle != "N":
            vehicle = int(input("Category of Vehicles"
                                "\n1. Car"
                                "\n2. Bus"
                                "\n3. Truck"))
            #carMeruya
            if vehicle == 1:
                print("Fee",a.getcPriceM())
                countCarM += 1

            #busMeruya
            if vehicle == 2:
                print("Fee",a.getbPriceM())
                countBusM += 1

            #truckMeruya
            if vehicle == 3:
                print("Fee",a.gettPriceM())
                countTruckM += 1

            if vehicle == 4:
                print(countCarM,countBusM,countTruckM)

            otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")
            otherVehicle = otherVehicle.upper()

    elif tollGate == "PONDOK AREN":
        while otherVehicle != "N":
            vehicle = int(input("Category of Vehicles"
                                "\n1. Car"
                                "\n2. Bus"
                                "\n3. Truck"))

            #carPondokAren
            if vehicle == 1:
                print("Fee",a.getcPriceP())
                countCarP += 1

            #busPondokAren
            if vehicle == 2:
                print("Fee",a.getbPriceP())
                countBusP += 1

            #truckPondokAren
            if vehicle == 3:
                print("Fee",a.gettPriceP())
                countTruckP += 1

            if vehicle == 4:
                print(countCarP,countBusP,countTruckP)

            otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")
            otherVehicle = otherVehicle.upper()

    otherTollGate = input("\nIs there any other toll gate (Y/N)? \n")
    otherTollGate = otherTollGate.upper()


b = TollBooth(cPriceM,bPriceM,tPriceM,
             cPriceP,bPriceP,tPriceP,
             countCarM,countBusM,countTruckM
             ,countCarP,countBusP,countTruckP)
b.printAllTBM()
print("Total revenue: Rp.",b.calculationTBM())
print()
b.printAllTBP()
print("Total revenue: Rp.",b.calculationTBP())
grandTotalRevenue = int(b.calculationTBM())+ int(b.calculationTBP())

print("Grand total revenue: Rp.",grandTotalRevenue)

# print()
#
# pondokAren.printAllTB()
# print("Total revenue: Rp.",pondokAren.calculationTB())
#




