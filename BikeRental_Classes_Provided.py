import datetime
from datetime import datetime, timedelta
    
class BikeRental:
    arrAvailableTypes = ["mountain", "road", "touring"]
    dblTotalColected = float(0)
    intTotalRented = int(0)
    
    def __init__(self,stock={"mountain": 0,"road": 0,"touring": 0}):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.stock = stock 

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock):
        blnValid = False
        if type(stock) == dict:
            for key,val in stock.items():
                if key in self.arrAvailableTypes:
                    blnValid = True
                else:
                    blnValid = False
                    raise Exception("Invalid Bike type entered, Stock has to be a dictionaty of 3 key value pairs of 'mountain', 'touring' and 'road', with value of the amount of bikes available!\n You entered: {}".format(key))


                if type(val) != int:
                    blnValid = False
                    print("Invalid input! Amount of Bikes Has to me integer. \nYou entered:{}".format(val))
                else:
                    blnValid = True


                if blnValid:
                    if val < 0:
                        blnValid = False
                        print("Invalid amount of bikes! Amount of Bikes cannot be less than 0\n You entered:{}".format(val))
                    else:
                        blnValid = True
        else:
            blnValid = False
            raise Exception("Invalid Shop Stock datatype! Stock has to be a dectionaty of 3 key value pairs of 'mountain', 'touring' and 'road', with value of the amount of bikes available!\n You entered: {}".format(stock))
        if blnValid:
            self.__stock = stock
        else:
            self.__stock = False
    
    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        totalBikes = 0
        for biketype, ammount in self.stock.items():
            totalBikes+= ammount

        print("We have currently {} bikes available to rent.".format(totalBikes))
        for biketype, amount in self.stock.items():
            print(amount,biketype,"bikes")

        return self.stock

    def rentBikeOnHourlyBasis(self, n, bikeType):
        """
        Rents a bike on hourly basis to a customer.
        """
        bikeType.lower().strip()
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        elif bikeType not in self.arrAvailableTypes:
            print("Invalid bike type".format(self.stock))
            return None

        # do not rent bike is stock is less than requested bikes
        
        elif n > self.stock[bikeType]:
            print("Sorry! We have currently have {} {} bikes available to rent.".format(self.stock[bikeType], bikeType))
            return None
        

        # rent the bikes        
        else:
            now = datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            self.intTotalRented+=n
            return now      
     
    def rentBikeOnDailyBasis(self, n, bikeType):
        """
        Rents a bike on daily basis to a customer.
        """
        bikeType.lower().strip()
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif bikeType not in self.arrAvailableTypes:
            print("Invalid bike type" )
            return None
        elif n > self.stock[bikeType]:
            print("Sorry! We have currently have {} {} bikes available to rent.".format(self.stock[bikeType], bikeType))
            return None
        
        else:
            now = datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            self.intTotalRented+=n
            return now
        
    def rentBikeOnWeeklyBasis(self, n, bikeType):
        """
        Rents a bike on weekly basis to a customer.
        """
        bikeType.strip().lower()

        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif bikeType not in self.arrAvailableTypes:
            print("Invalid bike type".format(self.stock))
            return None
        elif n > self.stock[bikeType]:
            print("Sorry! We have currently have {} {} bikes available to rent.".format(self.stock[bikeType], bikeType))
            return None
        else:
            now = datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            self.intTotalRented+=n
            return now
    
    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalTime, rentalBasis, numOfBikes, typeOFBikes = request
        bill = 0
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and numOfBikes and typeOFBikes and typeOFBikes in self.arrAvailableTypes:
            self.stock[typeOFBikes] += numOfBikes
            now = datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
            # family discount calculation
            if (3 <= numOfBikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                print("Subtotal before Discount: ${}".format(bill))
                bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            self.dblTotalColected += bill
            return bill
        
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    arrCustomerIDs = []
    def __init__(self, name, idNumber):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.strName = name
        self.idNumber = idNumber
        self.bikes = 0
        self.bikeType = ""
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    @property
    def name(self):
        return self.__strName
    @name.setter
    def strName(self, strName):
        if strName == None or strName == "":
            raise Exception("Name is required, the value of strFirstName was{}".format(strName))
        else:
            self.__strName = strName

    @property
    def idNumber(self):
        return self.__idNumber
    @idNumber.setter
    def idNumber(self, idNumber):
        blnValid = False
        while blnValid == False:
            if type(idNumber) == int:
                blnValid = True
            else:
                raise Exception("idNumber has to be numbers only!")

            if blnValid:
                if idNumber in Customer.arrCustomerIDs:
                    raise Exception("Customer with this ID Number already Exist")
                else:
                    blnValid=True
            if blnValid:
                Customer.arrCustomerIDs.append(idNumber)
                self.__idNumber = idNumber


    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
        blnValid = False
        if self.bikes == 0:
                        
            bikes = input("How many bikes would you like to rent? ")
            
            # implement logic for invalid input
            try:
                bikes = int(bikes)
                blnValid = True
            except ValueError:
                print("\t\tError!\nThat's not a positive integer!")
                blnValid = False
                # return -1
            
            if bikes < 1:
                print("\t\tError!\nInvalid input. Number of bikes should be greater than zero!")
                blnValid = False
                # return -1
            else:
                blnValid = True
                self.bikes = bikes

            if blnValid:
                if self.bikes>0:
                    bikeType = input("What type of bikes you'd like to rent? ").strip().lower()
                else:
                    bikeType = input("What type of bike you'd like to rent? ").strip().lower()
                
                if bikeType in BikeRental.arrAvailableTypes:
                    blnValid = True
                    self.bikeType = bikeType
                else:
                    print("\t\tError!\nInvalid input. You can only rent mountain, road or touring bike from us")
                    blnValid = False
        else:
            print(self.strName,"Already has", self.bikes," bikes in use. \nReturn rented inventory first")
            blnValid = False


        if blnValid:
            return self.bikes, self.bikeType
        else:
            return -1


     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        returnRequest= ()
        if self.rentalBasis and self.rentalTime and self.bikes and self.bikeType:
            returnRequest = self.rentalTime, self.rentalBasis, self.bikes,  self.bikeType
            self.rentalTime = 0
            self.rentalBasis = 0
            self.bikes = 0
            self.bikeType = 0
        else:
            returnRequest =  0,0,0,0
        
        return returnRequest


# Test Logic

# Create Shops and stock and demonstrate checking inventory
# shop1 = BikeRental({'mountain': 12, 'road': 12, 'touring': 32})
#shop2 = BikeRental()

# shop1.displaystock()

#shop1.rentBikeOnHourlyBasis(31, "mountain")
#shop2.rentBikeOnDailyBasis(-1, "road")
#shop1.rentBikeOnWeeklyBasis(11,"touring")

#shop1.displaystock()



## Create Customers
 
# customer1 = Customer("Anton", 12345)
#customer2 = Customer("Bob", 54321)
#customer3 = Customer("Kate", 43213)
#customer4 = Customer("Nick", 89432)

## Set up rental basis
# customer1.rentalBasis = 1 # hourly
#customer2.rentalBasis = 1 # hourly
#customer3.rentalBasis = 2 # daily
#customer4.rentalBasis = 2 # daily

## determine number of bikes
# customer1.bikes = 1
#customer1.bikes = 5 # eligible for family discount 30%
#customer3.bikes = 2
# customer1.bikes = 0

## detrmine rental time
# customer1.rentalTime = datetime.now() + timedelta(hours=-4)
#customer2.rentalTime = datetime.now() + timedelta(hours=-23)
#customer3.rentalTime = datetime.now() + timedelta(days=-4)
#customer4.rentalTime = datetime.now() + timedelta(days=-14)
## determine bike type
# customer1.bikeType = "mountain" 
#customer2.bikeType = "road" 
#customer3.bikeType = "touring" 
#customer4.bikeType = "road" 


## create request to return the bike
# request1 = customer1.returnBike()
#request2 = customer2.returnBike()
#request3 = customer3.returnBike()
#request4 = customer4.returnBike()
#print("req", request1)
## return the bike to shop and get a bill
# shop1.returnBike(request1) 
#shop1.returnBike(request2) 
#shop1.returnBike(request3) 
#shop1.returnBike(request4) 