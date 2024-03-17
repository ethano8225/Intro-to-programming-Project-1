'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

v1 =["Toyota",    "Camry",    "2018","45000","20000"]
v2 =["Ford",      "Escape",   "2019","30000","23500"]
v3 =["Honda",     "Accord",   "2017","60000","16200"]
v4 =["Chevrolet", "Silverado","2020","25000","41000"]
v5 =["BMW",       "3 Series", "2016","60000","20500"]
v6 =["Nissan",    "Rogue",    "2019","40000","17800"]
v7 =["Hyundai",   "Sonata",   "2018","42000","16500"]
v8 =["Jeep",      "Wrangler", "2021","15000","32000"]
v9 =["Ford",      "Mustang",  "2015","50000","22000"]
v10=["Volkswagen","Golf",     "2017","38000","17800"]
vehiclesList=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10]

#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    """ BEGIN MAKING YOUR CODE HERE """
    
    if option=="1":
        dealer.display(vehiclesList)                        # display info of vehicles

    if option=="2":
        dealer.info(vehiclesList)                           # calls info function from dealer, displays required info

    if option=="3":
        vehiclesList = dealer.removeVehicle(vehiclesList)   # removes user-selected car
    
    if option=="4":
        vehiclesList = [dealer.add_new_vehicle()]           # adds a new vehicle to the list

    if option=="5":
        dealer.compareVehicles(vehiclesList)                # compares two user selected vehicles

    if option=="6":            
        dealer.searchFunc(vehiclesList)                     # searches for vehicles in a certain price range

    if option=="7":
        dealer.discountedCar(vehiclesList)                  # discounts a user-selected car



# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")