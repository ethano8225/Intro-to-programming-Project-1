'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")

vehicle1 =["Toyota",    "Camry",    "2018","45,000","20,000"]
vehicle2 =["Ford",      "Escape",   "2019","30,000","23,500"]
vehicle3 =["Honda",     "Accord",   "2017","60,000","16,200"]
vehicle4 =["Chevrolet", "Silverado","2020","25,000","41,000"]
vehicle5 =["BMW",       "3 Series", "2016","60,000","20,500"]
vehicle6 =["Nissan",    "Rogue",    "2019","40,000","17,800"]
vehicle7 =["Hyundai",   "Sonata",   "2018","42,000","16,500"]
vehicle8 =["Jeep",      "Wrangler", "2021","15,000","32,000"]
vehicle9 =["Ford",      "Mustang",  "2015","50,000","22,000"]
vehicle10=["Volkswagen","Golf",     "2017","38,000","17,800"]
defaultVehiclesList=[vehicle1,vehicle2,vehicle3,vehicle4,vehicle5,vehicle6,vehicle7,vehicle8,vehicle9,vehicle10]
newVehicles = []

#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    ''' BEGIN MAKING YOUR CODE HERE '''
    if option=="1":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        print("\n****TEST vehicle data and display function****")
        dealer.display(defaultVehiclesList)
    if option=="2":
        currentVehiclesList = (defaultVehiclesList + newVehicles)
        dealer.info(currentVehiclesList)
    """if option=="3":
        test3"""
    if option=="4":
        print("\n****TEST the add_new_vehicle function****")
        vehicles=add_new_vehicle(vehicles) # sends current vehicle list to add_new... function, should return same list 
        display(vehicles)                  # WITH extra vehicle added    
    """if option=="5":
        test5
    if option=="6":            
        test6"""
    if option=="7":
        from dealer_tool import dealer
        car = int(input("Which vehicle do you want to discount: "))
        vehicles = dealer.carlist(car+1)
        discount = input("What percent discount (0-100): ")   
        print(car)
        #new_discounted_price=vehicle(car). want to replace price with discounted price
        #percant_discount=discount/100
        #new_price=percant_discount * 
        #print(new_price)
        #break
        #dealer.discounted_vehicle(car,discount,test7.vehicles)
        #test7


# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")