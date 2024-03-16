'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

vehicle1 =["Toyota",    "Camry",    "2018","45000","20000"]
vehicle2 =["Ford",      "Escape",   "2019","30000","23500"]
vehicle3 =["Honda",     "Accord",   "2017","60000","16200"]
vehicle4 =["Chevrolet", "Silverado","2020","25000","41000"]
vehicle5 =["BMW",       "3 Series", "2016","60000","20500"]
vehicle6 =["Nissan",    "Rogue",    "2019","40000","17800"]
vehicle7 =["Hyundai",   "Sonata",   "2018","42000","16500"]
vehicle8 =["Jeep",      "Wrangler", "2021","15000","32000"]
vehicle9 =["Ford",      "Mustang",  "2015","50000","22000"]
vehicle10=["Volkswagen","Golf",     "2017","38000","17800"]
defaultVehiclesList=[vehicle1,vehicle2,vehicle3,vehicle4,vehicle5,vehicle6,vehicle7,vehicle8,vehicle9,vehicle10]
newVehicles = []

#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    """ BEGIN MAKING YOUR CODE HERE """
    if option=="1":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        dealer.display(currentVehiclesList)
    if option=="2":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        dealer.info(currentVehiclesList)
    """if option=="3":
        test3"""
    if option=="4":
        print("\n****TEST the add_new_vehicle function****")
        vehicles=dealer.add_new_vehicle(vehicles) # sends current vehicle list to add_new... function, should return same list 
        dealer.display(vehicles)                  # WITH extra vehicle added    
    if option=="5":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        firstselectedvehicle=int(input("first vehicle (enter a number):"))-1
        secondselectedvehicle=int(input("second vehicle (enter a number):"))-1
        vehicleinfo1=currentVehiclesList[firstselectedvehicle]
        vehicleinfo2=currentVehiclesList[secondselectedvehicle]
        print(vehicleinfo1[0],vehicleinfo1[1],"vs",vehicleinfo2[0],vehicleinfo2[1],) #printing the title
        vehiclemake1=vehicleinfo1[1]
        vehiclemake2=vehicleinfo2[1]
        if vehiclemake1==vehiclemake2:  
            print("the two vehicles are the same makes")
        else:
            print("the two vehicles are different makes")
        year1=int(vehicleinfo1[2])
        year2=int(vehicleinfo2[2])
        if year1>year2:     #comparing year of the cars
            print("the first vehicle is newer.")
        elif year1<year2:
            print("the second vehicle is newer.")
        else:
            print("they where made the same year.")
        if int(vehicleinfo1[4])>int(vehicleinfo2[4]):
            print("the first vehicle costs more")
        else:
            print("the second vehicle costs more")

    if option=="6":            
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        minprice=int(input("please select a minimum price: "))
        maxprice=int(input("please select a maximum price: "))
        for i in range(0,len(currentVehiclesList),1):
            currentvehicle=currentVehiclesList[i]
            currentvehicleprice=int(currentvehicle[4])
            if currentvehicleprice >= minprice and currentvehicleprice <=maxprice:
                print(currentvehicle)
            else:
                continue    

    if option=="7":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        carNumber = int(input("Which vehicle do you want to discount: "))-1
        discount = int(input("What percent discount (0-100): "))  
        selectedVehicle = currentVehiclesList[carNumber]
        priceVehicle = selectedVehicle[4]
        priceVehicle= int(priceVehicle)
        newprice=int(priceVehicle-(priceVehicle*discount/100))
        selectedVehicle[4]=str(newprice)
        print(currentVehiclesList[carNumber])


# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")