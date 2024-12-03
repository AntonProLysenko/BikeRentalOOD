import BikeRental_Classes_Provided
Bikeshop = BikeRental_Classes_Provided.BikeRental
Customer = BikeRental_Classes_Provided.Customer

def appStart():
    print("\n\n-------------Welcome to the Bikeshop!------------------\n\n")
    print("\nLet's establish your inventory\n")

    mountainBikes = int(input("How many MOUNTAIN bikes your have available for rent?: "))
    roadBikes = int(input("How many ROAD bikes your have available for rent?: "))
    touringBikes = int(input("How many Touring bikes your have available for rent?: "))

    bikeshop1 = Bikeshop({"mountain": mountainBikes, "road": roadBikes, "touring": touringBikes})
    runApp(bikeshop1)

def runApp(bikeshop):
    customers = []
    blnRun = True
    while blnRun:
        print("\n\n-------------Bikeshop Menu------------------")
        print("Press 1 for NEW CUSTOMER RENTAL")
        print("Press 2 for RENTAL RETURN")
        print("Press 3 to SHOW AVAILABLE INVENTORY")
        print("Press 4 to SEE DAILY STATISTICS")
        print("Pess 5 to EXIT")
        menuInput = int(input(""))

        
        if menuInput == 1:
            print("\n------------------New Customer------------------")
            customer = Customer("Anton", 12345)
            customers.append(customer)
            customer = Customer("Bob", 12343)
            customers.append(customer)
        elif menuInput == 2:
            print("\n------------------Rental Return------------------")
            customerID = int(input("Enter Customer's ID Number: "))
            findCustomer(customers, customerID)
        elif menuInput == 3:
            print("\n------------------Available Inventory------------------")
            bikeshop.displaystock()
        elif menuInput == 4:
            print("\n------------------Daily Statistics------------------")
            print("Total Bikes Rented for Day:", bikeshop.intTotalRented)
            print("Total Revenue Collected for Day: $",bikeshop.dblTotalColected)
        elif menuInput == 5:
            print("\nGood Bye! \nSee you Tommorow!")
            blnRun = False

def findCustomer(listOfCustomers, id):
    for customer in listOfCustomers:
        if id == customer.idNumber:
            print(customer.name)
            return customer
    



appStart()
    