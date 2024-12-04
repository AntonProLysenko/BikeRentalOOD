import BikeRental_Classes_Provided
Bikeshop = BikeRental_Classes_Provided.BikeRental
Customer = BikeRental_Classes_Provided.Customer

def appStart():
    """
        Launches the app
        and calls runApp function after initialization of inventory
    """
    
    print("\n\n-------------Welcome to the Bikeshop!------------------\n\n")
    print("\nLet's establish your inventory\n")

    mountainBikes = int(input("How many MOUNTAIN bikes your have available for rent?: "))
    roadBikes = int(input("How many ROAD bikes your have available for rent?: "))
    touringBikes = int(input("How many Touring bikes your have available for rent?: "))

    bikeshop1 = Bikeshop({"mountain": mountainBikes, "road": roadBikes, "touring": touringBikes})
    runApp(bikeshop1)

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
            intCustomerID = int(input("Enter Customer's 5 digit ID: "))
           
            #If Customer Exist or New Customer
            if intCustomerID in Customer.arrCustomerIDs:
                currentCustomer = findCustomer(customers, intCustomerID)
            else:
                currentCustomer = Customer(strCustomerName, intCustomerID)
                customers.append(currentCustomer)
            
            #Gathering Rental Information
            customerRequest = currentCustomer.requestBike()
            #Showing Discount Alegibility

            if customerRequest !=-1:
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
            customerID = int(input("Enter Customer's ID Number: "))
            currentCustomer = findCustomer(customers, customerID)
            if currentCustomer != False:
                print("Current Customer:", currentCustomer.strName)
                print("Rented", currentCustomer.bikes, currentCustomer.bikeType, "bikes")
                print("Rental Time:", currentCustomer.rentalTime)

        elif menuInput == 3:
            print("\n------------------Available Inventory------------------")
            bikeshop.displaystock()

        elif menuInput == 4:
            
            print("\n------------------Daily Statistics------------------")
            print("Total Bikes Rented for Day:", bikeshop.intTotalRented)
            print("Total Revenue Collected for Day: $",bikeshop.dblTotalColected)
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

    



appStart()
    