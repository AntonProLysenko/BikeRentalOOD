import BikeRental_Classes_Provided
Bikeshop = BikeRental_Classes_Provided.BikeRental
Customer = BikeRental_Classes_Provided.Customer

def appStart():
    print("-------------Welcome to the Bikeshop!------------------\n\n")
    print("\nLet's establish your inventory\n")

    mountainBikes = int(input("How many MOUNTAIN bikes your have available for rent?: "))
    roadBikes = int(input("How many ROAD bikes your have available for rent?: "))
    touringBikes = int(input("How many Touring bikes your have available for rent?: "))

    bikeshop1 = Bikeshop({"mountain": mountainBikes, "road": roadBikes, "touring": touringBikes})

appStart()
    