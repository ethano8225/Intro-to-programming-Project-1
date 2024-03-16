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
        dealer.display(vehiclesList)

    if option=="2":
        dealer.info(vehiclesList)

    if option=="3":
        vehiclesList = dealer.removeVehicle(vehiclesList)
    
    if option=="4":
        vehiclesList = [dealer.add_new_vehicle()]

    if option=="5":
        firstselectedvehicle=int(input("First vehicle (enter a number):"))-1
        secondselectedvehicle=int(input("Second vehicle (enter a number):"))-1
        vehicleinfo1=vehiclesList[firstselectedvehicle]
        vehicleinfo2=vehiclesList[secondselectedvehicle]
        print(vehicleinfo1[0],vehicleinfo1[1],"vs.",vehicleinfo2[0],vehicleinfo2[1],) #printing the title
        vehiclemake1=vehicleinfo1[1]
        vehiclemake2=vehicleinfo2[1]
        if vehiclemake1==vehiclemake2:  
            print("The two vehicles are the same makes.")
        else:
            print("The two vehicles are different makes.")
        year1=int(vehicleinfo1[2])
        year2=int(vehicleinfo2[2])
        if year1>year2:     #comparing year of the cars
            print("The first vehicle is newer.")
        elif year1<year2:
            print("The second vehicle is newer.")
        else:
            print("They where made the same year.")
        if int(vehicleinfo1[4])>int(vehicleinfo2[4]):
            print("The first vehicle costs more.")
        else:
            print("The second vehicle costs more.")

    if option=="6":            
        minprice=int(input("Please select a minimum price: "))
        maxprice=int(input("Please select a maximum price: "))
        print("")
        count = 0
        for i in range(0,len(vehiclesList),1):
            currentvehicle=vehiclesList[i]
            currentvehicleprice=int(currentvehicle[4])
            if currentvehicleprice >= minprice and currentvehicleprice <=maxprice:
                print(currentvehicle[0],currentvehicle[1],currentvehicle[4])
                count=count+1
            else:
                continue    
        
        print("\nTotal number of vehicles:",str(count))

    if option=="7":
        carNumber = int(input("Which vehicle do you want to discount: "))-1
        discount = float(input("What percent discount (0-100): "))  
        selectedVehicle = vehiclesList[carNumber]
        print("Vehicle:",selectedVehicle[0])

        priceVehicle = selectedVehicle[4]
        print("Price:",priceVehicle)
        print("Discount:",((discount/100)*int(priceVehicle)))

        priceVehicle= int(priceVehicle)
        newPrice=int(priceVehicle-(priceVehicle*discount/100))
        print("New Price:",newPrice)
        selectedVehicle[4]=str(newPrice)



# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")