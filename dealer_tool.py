'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)


def display(vehicles_list):
    print("Car #"+"\t"+"Make","Model","Year","Mileage","Price($)",sep="\t\t")
    print("---------------------------------------------------------------------------------")
    i = 0
    while i < len(vehicles_list):    # while loop prints all vehicles in list
        vehicle = vehicles_list[i]   
        if len(vehicle[0]) > 8 and len(vehicle[1]) >= 8:                                  #must check the length of the each string to allow for 
            print(str(i+1),vehicle[0],vehicle[1],vehicle[2]+"\t\t"+vehicle[3]+"\t\t"+vehicle[4],sep="\t") #good looking formatting
        elif len(vehicle[0]) > 8 and len(vehicle[1]) < 8:
            print(str(i+1)+"\t"+vehicle[0]+"\t"+vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        elif len(vehicle[0]) <= 8 and len(vehicle[1]) >= 8:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1]+"\t"+vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        else:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep='\t\t')
        i = i+1
    return 0


def info(vehicles_list):
    print("#Vehicles",str(len(vehicles_list)),"\n")
    lessthan10,tento20,twentyTo30,thirtyTo40,fourtyup = 0,0,0,0,0 #to count how many cars are in each group
    for i in vehicles_list:
        if int(i[4]) < 10000:                               #for loop goes through every car and catagorizes them,
            lessthan10 = lessthan10+1                       #saving the number of cars in each group
        elif int(i[4]) >= 10000 and int(i[4]) < 20000:      
            tento20 = tento20+1
        elif int(i[4]) >= 20000 and int(i[4]) < 30000:
            twentyTo30 = twentyTo30+1
        elif int(i[4]) >= 30000 and int(i[4]) < 40000:
            thirtyTo40 = thirtyTo40+1
        elif int(i[4]) >= 40000:
            fourtyup = fourtyup+1

                                                                        # then print the percentage in each group
    print("<10,000 : ",100*(lessthan10/len(vehicles_list)),"%",sep="")  # when compared to the total amount of cars
    print("10,000s : ",100*(tento20/len(vehicles_list)),"%",sep="")
    print("20,000s : ",100*(twentyTo30/len(vehicles_list)),"%",sep="")
    print("30,000s : ",100*(thirtyTo40/len(vehicles_list)),"%",sep="")
    print(">=40,000 : ",100*(fourtyup/len(vehicles_list)),"%\n",sep="")

    total = 0
    i = 0
    while i < len(vehicles_list):           # go through every vehicle, get the price 
        vehicle = vehicles_list[i]          # count the total price of every divided by the 
        price = int(vehicle[4])             # amount of cars in the list
        total = total + price
        i = i + 1
    print("Mean Price:",str(total/len(vehicles_list)))

def removeVehicle(defaultVehiclesList,newVehicles):
    i = 0
    while i != 1:           #error check at bottom to ask what car wants to be removed again if invalid number is given
        carID = int(input("Which vehicle do you want to remove (enter a number): "))
        if carID <= len(defaultVehiclesList):
            defaultVehiclesList.remove(defaultVehiclesList[carID-1])
            i = 1
        elif (carID-len(defaultVehiclesList)) <= len(newVehicles):
            newVehicles.remove(newVehicles[carID-1-len(defaultVehiclesList)])
            i = 1
        elif carID > len(defaultVehiclesList) or carID > len(newVehicles):
            print("You entered an invalid number.")

def add_new_vehicle():
    Make = input("Enter Make: ")
    Model = input("Enter Model: ")                           #Ask for a description of the car that needs to be added
    Year = input("Enter Year: ")
    Mileage = input("Enter Mileage: ")
    Price = input("Enter Price: ")
    new_car = [Make,Model,Year,Mileage,Price]
    
    return new_car #Vehicle added to the newVehicles list when it is passed back
