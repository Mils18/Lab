class Car:
    def __init__(self, cPrice):
        self.cPrice = cPrice

    def getCarPrice(self):
        return self.cPrice

class Bus:
    def __init__(self, bPrice):
        self.bPrice = bPrice
    def getBusPrice(self):
        return self.bPrice

class Truck:
    def __init__(self, tPrice):
        self.tPrice = tPrice
    def getTruckPrice(self):
        return self.tPrice

class Vehicle(Car,Bus,Truck):
    def __init__(self,cPrice,bPrice,tPrice):
        Car.__init__(self,cPrice)
        Bus.__init__(self,bPrice)
        Truck.__init__(self,tPrice)


cPrice = 6000
bPrice = 8000
tPrice = 10000
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

    if vehicle == 1:
        print("Fee",a.getCarPrice())

    if vehicle == 2:
        print("Fee",a.getBusPrice())

    if vehicle == 3:
        print("Fee",a.getTruckPrice())

    otherVehicle = input("\nIs there any other vehicle (Y/N)? \n")
    otherVehicle = otherVehicle.upper()

