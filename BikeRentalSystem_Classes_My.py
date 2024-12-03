

#---------------------------------------------------------
# Bike Rental System 
# By Anton Lysenko
#---------------------------------------------------------



class Customer: 
    def __init__(self, strName):
        self.intRentedInventory = 0
        self.intRentDuration = 0
        self.strRentedPeriod = None
        self.strName = strName
        self.objRentedFrom = None
    
    @property
    def strName(self):
        return self.__strName


    @strName.setter
    def strName(self, strName):
        if strName == None or strName == "":
            raise Exception(f"Name is required, the value of strFirstName was{strName}")
        elif Customer.containsNumbers(strName):
            raise Exception(f"First Name cannot contain any Numbers, the value of strFirstName was{strName}")
        else:
            self.__strName = strName

    @property
    def intRentedInventory(self):
        return self.__intRentedInventory
    
    @intRentedInventory.setter
    def intRentedInventory(self, intRentedInventory):
        if type(intRentedInventory) is not int:
            raise Exception("Type Error! \n Rented inventory has to be an integer, entered value of intRentedInventory was {var}, type {type}". format(var = intRentedInventory, type = type(intRentedInventory)))
        elif intRentedInventory < 0:
            raise Exception(f"Error! \n Rented inventory cannot be less than 0, entered value of intRentedInventory was {intRentedInventory}")
        else:
            self.__intRentedInventory = intRentedInventory      

    @property
    def strRentedPeriod(self):
        return self.__strRentedPeriod

    @strRentedPeriod.setter
    def strRentedPeriod(self, strRentedPeriod):
        acceptadValues = ["hourly", "daily", "weekly"]

        if strRentedPeriod == None:
             self.__strRentedPeriod = strRentedPeriod
        elif strRentedPeriod.lower() not in acceptadValues:
            self.__strRentedPeriod = None
            raise Exception("Rented Period Value unacceptable!, you entered {input}".format(input = strRentedPeriod))
        else:
             self.__strRentedPeriod = strRentedPeriod
            


    def showAvailableBikes(self, bikeshop):
        bikeshop.showAvailableBikes()

        
    def rentBike(self, bikeshop, strPeriodType, rentDuration, intNumberOfBikes):
        dblBillEstimate = float(0)
        if self.intRentedInventory == None or self.intRentedInventory == 0:

            dblBillEstimate = bikeshop.reserveBike(strPeriodType, rentDuration, intNumberOfBikes)
    
            if dblBillEstimate:
                self.intRentedInventory += intNumberOfBikes
                self.strRentedPeriod = strPeriodType
                self.intRentDuration = rentDuration

                self.objRentedFrom = bikeshop
                print("Succesfully rented {amount} bikes for {length} {periodType} by {name} \n EstimetedBill Total: ${total}".format(amount = intNumberOfBikes, length = rentDuration, periodType = strPeriodType, name = self.strName, total = dblBillEstimate))
        else:
            print(self.strName, "Already has", self.intRentedInventory, "bikes in use")

    def returnBike(self):
        dblBillTotal = float(0)

        if self.intRentedInventory > 0:
            dblBillTotal =  self.objRentedFrom.returnBike(self.strRentedPeriod, self.intRentDuration, self.intRentedInventory)
            self.intRentedInventory = 0  
            self.strRentedPeriod = None
            self.intRentDuration = 0
            print("{customerName} sucessfully returned their rented inventory \n They have to pay ${billTotal}". format(customerName = self.__strName, billTotal = dblBillTotal))
            return dblBillTotal
        else: 
            print("Nothing was rented by {customerName}". format(customerName = self.__strName))
        

    def containsNumbers(str):
        containNums = False
        for char in str:
            if char.isdigit():
                containNums = True
                break
        return containNums
	









class BikeShop:

    def __init__(self, name, intInitialInventory):
        self.name = name
        self.intTotalInventory = intInitialInventory
        self.intAvailableInventory = intInitialInventory




    def showAvailableBikes(self):
        print(self.name, " have ", self.intAvailableInventory, " bikes available for rent")





    def reserveBike(self, strPeriodType, rentDuration, intNumberOfBikes):
        if intNumberOfBikes > self. intAvailableInventory:
            print("Unfortunately {name} doest't have {requestedAmount} bikes available rn \n They only have {availableAmount} ".format(name = self.name, requestedAmount = intNumberOfBikes, availableAmount = self.intAvailableInventory))
            return False
        else:
            self.intAvailableInventory -= intNumberOfBikes
            print("Generating bill")
            return self.generateBill(intNumberOfBikes, rentDuration, strPeriodType)
    
    
    def returnBike(self, strPeriodType, rentDuration, intNumberOfBikes):
        self.intAvailableInventory += intNumberOfBikes

        print("Generating Final bill")
        return self.generateBill(intNumberOfBikes, rentDuration, strPeriodType)




    def generateBill(self, inventoryAmount,rentDuration, rentedPeriod):

        dblBillTotal = 0
        dblPeriodPrice = 0
        dblFamilyDiscount = 30/100

        if rentedPeriod.lower() == "hourly":
            dblPeriodPrice = 5
        elif rentedPeriod.lower() == "daily":
            dblPeriodPrice = 20
        elif rentedPeriod.lower() == "weekly":
            dblPeriodPrice = 60
        else:
            raise Exception("Unknown rentedPeriod, you entered: {input}". format(input = rentedPeriod))

        dblBillTotal = inventoryAmount* dblPeriodPrice * rentDuration
        print("Total: $", dblBillTotal)
        if inventoryAmount>=3:
            if inventoryAmount <=5:
                print("Family Discount %",dblFamilyDiscount*100," applied: -${discount}".format(discount =  dblBillTotal* dblFamilyDiscount) )
                dblBillTotal -= dblBillTotal* dblFamilyDiscount
        print("Final Total: $", dblBillTotal)
        return dblBillTotal






#---------------------------------------------------------
# Instances
#---------------------------------------------------------
bobsBikeShop = BikeShop("Bob's Bike Shop", 12)
anton = Customer("Anton Lysenko")
nick = Customer("Nickolas Cage")
jakesTwoWheels = BikeShop("Jake's Two Wheel Shop", 11)



#---------------------------------------------------------
# Execution
#---------------------------------------------------------
print("------------------Availability Check------------------")
bobsBikeShop.showAvailableBikes()
anton.showAvailableBikes(bobsBikeShop)
jakesTwoWheels.showAvailableBikes()
anton.showAvailableBikes(jakesTwoWheels)

print("")
print("------------------Returning Bike------------------")
anton.returnBike()

print("")
print("------------------Renting 2 bikes for 1 week------------------")
anton.rentBike(bobsBikeShop, "weekly", 1, 2)
anton.showAvailableBikes(bobsBikeShop)


print("")
print("------------------Renting bikes By different------------------")
anton.rentBike(bobsBikeShop, "daily", 1, 11)
nick.rentBike(bobsBikeShop, "daily", 1, 4)
anton.returnBike()



nick.rentBike(jakesTwoWheels, "daily", 1, 12)