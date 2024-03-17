'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")

# By Ethan O'Connor and Ryan Blanchette
#### To complete (all functions below)


def display(vehicles_list):
    print("Car #"+"\t"+"Make","Model","Year","Mileage","Price($)",sep="\t\t")
    print("---------------------------------------------------------------------------------")
    i = 0
    while i < len(vehicles_list):                                                                         # while loop prints all vehicles in list
        vehicle = vehicles_list[i]   
        if len(vehicle[0]) > 8 and len(vehicle[1]) >= 8:                                                  # must check the length of the each string to allow for 
            print(str(i+1),vehicle[0],vehicle[1],vehicle[2]+"\t\t"+vehicle[3]+"\t\t"+vehicle[4],sep="\t") # good looking formatting
        elif len(vehicle[0]) > 8 and len(vehicle[1]) < 8:                                                   
            print(str(i+1)+"\t"+vehicle[0]+"\t"+vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        elif len(vehicle[0]) <= 8 and len(vehicle[1]) >= 8:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1]+"\t"+vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        else:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep='\t\t')
        i = i+1


def info(vehicles_list):
    print("#Vehicles",str(len(vehicles_list)),"\n")
    
    lessthan10,tento20,twentyTo30,thirtyTo40,fourtyup = 0,0,0,0,0         #to count how many cars are in each group
    for car in vehicles_list:
        if int(car[4]) < 10000:                                           #for loop goes through every car and catagorizes them,
            lessthan10 = lessthan10+1                                     #saving the number of cars in each group
        elif int(car[4]) >= 10000 and int(car[4]) < 20000:      
            tento20 = tento20+1
        elif int(car[4]) >= 20000 and int(car[4]) < 30000:
            twentyTo30 = twentyTo30+1
        elif int(car[4]) >= 30000 and int(car[4]) < 40000:
            thirtyTo40 = thirtyTo40+1
        elif int(car[4]) >= 40000:
            fourtyup = fourtyup+1
    
    print("<10,000 : ",100*(lessthan10/len(vehicles_list)),"%",sep="")    # then print the percentage in each group
    print("10,000s : ",100*(tento20/len(vehicles_list)),"%",sep="")       # when compared to the total amount of cars
    print("20,000s : ",100*(twentyTo30/len(vehicles_list)),"%",sep="")
    print("30,000s : ",100*(thirtyTo40/len(vehicles_list)),"%",sep="")
    print(">=40,000 : ",100*(fourtyup/len(vehicles_list)),"%\n",sep="")

    total = 0
    i = 0
    while i < len(vehicles_list):           # go through every vehicle, get the price 
        vehicle = vehicles_list[i]          # count the total price of every car divided by 
        price = int(vehicle[4])             # the amount of cars in the list
        total = total + price
        i = i + 1
    print("Mean Price:",str(total/len(vehicles_list)))

def removeVehicle(vehiclesList,carID):
    del vehiclesList[carID-1] #delete the car from the list
    return vehiclesList       #return the updated list

def add_new_vehicle():
    Make = input("Enter Make: ")
    Model = input("Enter Model: ")                          #Ask for a description of the car that needs to be added
    Year = input("Enter Year: ")
    Mileage = input("Enter Mileage: ")
    Price = input("Enter Price: ")
    new_car = [Make,Model,Year,Mileage,Price]
    
    return new_car                                          #Vehicle added to the vehiclesList list when it is passed back

def compareVehicles(vehicleInfo1,vehicleInfo2):
    print(vehicleInfo1[0],vehicleInfo1[1],"vs.",vehicleInfo2[0],vehicleInfo2[1],) #printing the title

    vehiclemake1=vehicleInfo1[1]
    vehiclemake2=vehicleInfo2[1]                            #set vehicle make to the make of each car, test if they are the same
    if vehiclemake1==vehiclemake2:                          #or different
        print("The two vehicles are the same makes.")
    else:
        print("The two vehicles are different makes.")

    year1=int(vehicleInfo1[2])
    year2=int(vehicleInfo2[2])
    if year1>year2:                                         #comparing year of the cars
        print("The first vehicle is newer.")
    elif year1<year2:
        print("The second vehicle is newer.")
    else:
        print("They where made the same year.")             #comparing cost of the cars
    if int(vehicleInfo1[4])>int(vehicleInfo2[4]):
        print("The first vehicle costs more.")
    elif int(vehicleInfo1[4])<int(vehicleInfo2[4]):
        print("The second vehicle costs more.")
    else:
        print("The vehicles cost the same.")

def searchFunc(vehiclesList,minprice,maxprice):
    count = 0
    for i in range(0,len(vehiclesList),1):                  #check to see which cars match the price range
        currentvehicle=vehiclesList[i]                      #and print them accordingly
        currentvehicleprice=int(currentvehicle[4])
        if currentvehicleprice >= minprice and currentvehicleprice <=maxprice:
            print(currentvehicle[0],currentvehicle[1],currentvehicle[4])
            count=count+1                                   #increase the count to print number of cars
        else:
            continue    
    print("\nTotal number of vehicles:",str(count))         #print number of cars

def discountedCar(vehiclesList,carNumber,discount):
    selectedVehicle = vehiclesList[carNumber] #set vehicle to the selected vehicle
    print("Vehicle:",selectedVehicle[0])

    priceVehicle = selectedVehicle[4] #set priceVehicle to the price
    print("Price:",priceVehicle)
    print("Discount:",((discount/100)*int(priceVehicle)))

    priceVehicle= int(priceVehicle)
    newPrice=int(priceVehicle-(priceVehicle*discount/100)) #set newPrice to the discount
    print("New Price:",newPrice)
    selectedVehicle[4]=str(newPrice) #change the price of the vehicle
    return selectedVehicle