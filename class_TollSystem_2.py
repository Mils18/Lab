class Vehicle:
    def __init__(self,cPrice,bPrice,tPrice):
        self.cPrice = cPrice
        self.bPrice = bPrice
        self.tPrice = tPrice

    def getcPrice(self):
        return self.cPrice

    def getbPrice(self):
        return self.bPrice

    def gettPrice(self):
        return self.tPrice

class TollBooth(Vehicle):
    def __init__(self,cPrice,bPrice,tPrice,countCar,countBus,countTruck):
        Vehicle.__init__(self,cPrice,bPrice,tPrice)
        self.countCar = countCar
        self.countBus = countBus
        self.countTruck = countTruck

    def printCalculation(self):
        x = int(self.countCar) * self.cPrice
        y = int(self.countBus) * self.bPrice
        z = int(self.countTruck) * self.tPrice
        totalTB = x + y + z
        return totalTB

    def printAllTB(self):
        timesP = 20
        print(timesP * "-")
        print("car\t\tBus\t\tTruck")
        print(timesP * "-")
        print(str(self.countCar) + "\t\t" + str(self.countBus) + "\t\t" + str(self.countTruck))
        print(timesP * "-")




cPrice = 6000
bPrice = 8000
tPrice = 10000

countCar = 0
countBus = 0
countTruck = 0

a = Vehicle(cPrice,bPrice,tPrice)

otherVehicle = "Y"
timesE = 55
timesS = 15

print(timesE*"=",
      "\n",timesS*" ","Toll Payment Systems"
      "\n",timesS*" "," PT Jasa Marga, Tbk."
      "\n"+timesE*"=")

while otherVehicle != "N":
    vehicle = int(input("Category of Vehicles"
                        "\n1. Car"
                        "\n2. Bus"
                        "\n3. Truck"))
    #car
    if vehicle == 1:
        print("Fee",a.getcPrice())
        countCar += 1

    #bus
    if vehicle == 2:
        print("Fee",a.getbPrice())
        countBus += 1

    #truck
    if vehicle == 3:
        print("Fee",a.gettPrice())
        countTruck += 1

    if vehicle == 4:
        print(countCar,countBus,countTruck)

    otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")
    otherVehicle = otherVehicle.upper()

# totalTB = 0
b = TollBooth(cPrice,bPrice,tPrice,countCar,countBus,countTruck)


b.printAllTB()
print("Total revenue: Rp.",b.printCalculation())