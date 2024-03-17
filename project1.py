'''----------------Import Modules----------------'''
import dealer_tool as dealer
# By Ethan O'Connor and Ryan Blanchette
'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

v1 =["Toyota",    "Camry",    "2018","45000","20000"] #must run this here (or a function that does a similar job)
v2 =["Ford",      "Escape",   "2019","30000","23500"] #to set up the default car list
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
    # By Ethan O'Connor and Ryan Blanchette
    if option=="1":
        dealer.display(vehiclesList)                        # display info of vehicles

    if option=="2":
        dealer.info(vehiclesList)                           # calls info function from dealer, displays required info

    if option=="3":
        while True:                                                         # error check at bottom to ask what car wants to be...
            carID = int(input("Which vehicle do you want to remove (enter a number): "))  #...removed again if invalid number is given
            if carID <= len(vehiclesList):                                  # carID is in the list
                vehiclesList = dealer.removeVehicle(vehiclesList,carID)     # removes user-selected car
                break
            elif carID > len(vehiclesList) or carID < 0:         # carID is not in list
                print("You entered an invalid number.")
                continue
    
    if option=="4":
        vehiclesList = vehiclesList+[dealer.add_new_vehicle()]           # adds a new vehicle to the list

    if option=="5":
        while True:            #error check to make sure the number provided makes sense, if so,
            firstVehicle=int(input("First vehicle (enter a number): "))-1 #continue running the program
            if firstVehicle<=len(vehiclesList):
                break
            else:
                print("Invalid input, retry.")
                continue
        while True:
            secondVehicle=int(input("Second vehicle (enter a number): "))-1
            if secondVehicle<=len(vehiclesList):
                break
            else:
                print("Invalid input, retry.")
                continue
        vehicleInfo1=vehiclesList[firstVehicle]                 # set vehicleInfo to the selected numbers
        vehicleInfo2=vehiclesList[secondVehicle]
        dealer.compareVehicles(vehicleInfo1,vehicleInfo2)       # calls func with both vehicles info

    if option=="6":
        minprice=int(input("Please select a minimum price: "))
        maxprice=int(input("Please select a maximum price: ")) # get the min and max prices
        print("")            
        dealer.searchFunc(vehiclesList,minprice,maxprice)      # searches for vehicles in a certain price range

    if option=="7":
        while True:         #error checking to see if number inputted is invalid
            carNumber = int(input("Which vehicle do you want to discount: "))-1
            if carNumber>len(vehiclesList):
                print("Invalid car number. Retry.")
                continue
            elif carNumber>=0 and carNumber<len(vehiclesList):
                break
        while True:         #same here, error checking to see if number is invalid
            discount = float(input("What percent discount (0-100): "))
            if 0<=discount<=100:
                break
            elif discount>100 or discount<0:
                print("Invalid discount amount. Retry.")
                continue
        vehiclesList[carNumber] = dealer.discountedCar(vehiclesList,carNumber,discount)                  # discounts a user-selected car



# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")