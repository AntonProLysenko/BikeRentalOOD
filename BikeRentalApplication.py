import BikeRental_Classes_Provided
Bikeshop = BikeRental_Classes_Provided.BikeRental
Customer = BikeRental_Classes_Provided.Customer

import datetime
from datetime import datetime, timedelta

def appStart():
    """
        Launches the app
        and calls runApp function after initialization of inventory
    """
    
    print("\n\n-------------Welcome to the Bikeshop!------------------\n\n")
    print("\nLet's establish your inventory\n")
    #Gathering Inital inventory with validation
  
    bikeshop = None
    while not bikeshop or bikeshop.stock == False:
        try:
            mountainBikes = input("\nHow many MOUNTAIN bikes your have available for rent?: ")
            roadBikes = input("How many ROAD bikes your have available for rent?: ")
            touringBikes = input("How many Touring bikes your have available for rent?: ")

            if int(mountainBikes)>= 0 and int(roadBikes) >= 0 and int(touringBikes)>=0:
                bikeshop = Bikeshop({"mountain": int(mountainBikes), "road": int(roadBikes), "touring": int(touringBikes)})
                break
            else:
                print("Invalid input of bike amount")
            if bikeshop.stock == False:
                print("Invalid amount of bikes entered. Re-enter your inventory inventory.")
        except Exception as e:
            print("Error: {}".format(e))
    runApp(bikeshop)




def runApp(bikeshop):
    """
    Runs The app after initialization of inventory until Exit option is clicked
    """

    customers = []#List of customers Rented from shop, needed for finding customer during return
    blnRun = True
    while blnRun:
        # Main Menu
        print("\n\n-------------Bikeshop Menu------------------")
        print("Press 1 for NEW CUSTOMER RENTAL")
        print("Press 2 for RENTAL RETURN")
        print("Press 3 to SHOW AVAILABLE INVENTORY")
        print("Press 4 to SEE DAILY STATISTICS")
        print("Pess 5 to EXIT")
        menuInput = int(input(""))

        
        if menuInput == 1:
            print("\n------------------New Customer------------------")
            #Gathering Customer's info
            strCustomerName = input("Enter Customer's Name: ")
            intCustomerID = (input("Enter Customer's 5 digit ID: "))
            
            #Input Validation
            while len(strCustomerName)<=0:
                print("Invalid Customer Name")
                intCustomerID = (input("Enter Customer's 5 digit ID: "))

            while len(intCustomerID) !=5:
                 print("Invalid Customer ID")
                 intCustomerID = (input("Enter Customer's 5 digit ID: "))
            else:
                intCustomerID = int(intCustomerID)

            #If Customer Exist or New Customer
            if intCustomerID in Customer.arrCustomerIDs:
                currentCustomer = findCustomer(customers, intCustomerID)
            else:
                currentCustomer = Customer(strCustomerName, intCustomerID)
                customers.append(currentCustomer)
            
            #Gathering Rental Information
            customerRequest = currentCustomer.requestBike()

            if customerRequest !=-1:
                #Showing Discount Alegibility
                if customerRequest[0]>=3 and customerRequest[0]<=5:
                    print("\nWoohoo! Tou are aligible for Family Discount!\n")
                print("How would you like to rent the bike?")
                print("Press 1 for Hourly ($5/hour)")
                print("Press 2 for Daily ($20/day)")
                print("Press 3 for Weekly ($60/week)")
                rentalBasis = int(input("Enter the number corresponding to your choice: "))
                if rentalBasis in [1, 2, 3]:  # Validation
                    currentCustomer.rentalBasis = rentalBasis
                    if rentalBasis == 1:
                        currentCustomer.rentalTime = bikeshop.rentBikeOnHourlyBasis(customerRequest[0], customerRequest[1])
                    elif rentalBasis == 2:
                        currentCustomer.rentalTime = bikeshop.rentBikeOnDailyBasis(customerRequest[0], customerRequest[1])
                    elif rentalBasis == 3:
                        currentCustomer.rentalTime = bikeshop.rentBikeOnWeeklyBasis(customerRequest[0], customerRequest[1])
                else:
                    print("Invalid choice. Please start the rental process again.")


        elif menuInput == 2:
            print("\n------------------Rental Return------------------")
            intCustomerID = (input("Enter Customer's 5 digit ID: "))
            while len(intCustomerID) !=5:
                print("Invalid Customer ID")
                intCustomerID = (input("Enter Customer's 5 digit ID: "))
            else:
                intCustomerID = int(intCustomerID)

            currentCustomer = findCustomer(customers, intCustomerID)
            if currentCustomer != False:
                print("\n--------Invoice---------\n")
                print("Current Customer:", currentCustomer.strName)
                print("Rented", currentCustomer.bikes, currentCustomer.bikeType, "bikes")
                print("Rental Time:", currentCustomer.rentalTime)
                request = currentCustomer.returnBike()
                bikeshop.returnBike(request)

        elif menuInput == 3:
            print("\n------------------Available Inventory------------------")
            bikeshop.displaystock()

        elif menuInput == 4:
            
            print("\n------------------Daily Statistics------------------")
            print("Total Bikes Rented for Day:", bikeshop.intTotalRented)
            print("Total Revenue Collected for Day: $",bikeshop.dblTotalColected)
            #for testing purposes added functional to increase rent day to make sure thar invioce is calculated right
            for customer in customers:
                increaseRentDay(customer)
            
        elif menuInput == 5:
            #Exits the app
            print("\nGood Bye! \nSee you Tommorow!")
            blnRun = False

def findCustomer(listOfCustomers, id):
    foundCustomer = None
    for customer in listOfCustomers:
        if id == customer.idNumber:
            print("\nExisting Customer",customer.name, "ID:", customer.idNumber)
            foundCustomer = customer
    if foundCustomer == None:
        print("\n\nCustomer not Found!\n\n")
        return False
    else:
        return foundCustomer

    
def increaseRentDay(customer):
    print(customer.strName,customer.rentalTime, customer.bikes)
    if customer.rentalTime:
        customer.rentalTime += timedelta(days=-1)


appStart()


    