'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


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
    
    lessthan10,tento20,twentyTo30,thirtyTo40,fourtyup = 0,0,0,0,0       #to count how many cars are in each group
    for i in vehicles_list:
        if int(i[4]) < 10000:                                           #for loop goes through every car and catagorizes them,
            lessthan10 = lessthan10+1                                   #saving the number of cars in each group
        elif int(i[4]) >= 10000 and int(i[4]) < 20000:      
            tento20 = tento20+1
        elif int(i[4]) >= 20000 and int(i[4]) < 30000:
            twentyTo30 = twentyTo30+1
        elif int(i[4]) >= 30000 and int(i[4]) < 40000:
            thirtyTo40 = thirtyTo40+1
        elif int(i[4]) >= 40000:
            fourtyup = fourtyup+1
    print("<10,000 : ",100*(lessthan10/len(vehicles_list)),"%",sep="")  # then print the percentage in each group
    print("10,000s : ",100*(tento20/len(vehicles_list)),"%",sep="")     # when compared to the total amount of cars
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

def removeVehicle(vehiclesList):
    while True:                                             #error check at bottom to ask what car wants to be removed again if invalid number is given
        carID = int(input("Which vehicle do you want to remove (enter a number): "))
        if carID <= len(vehiclesList):                       #carID is in the list
            vehiclesList = (vehiclesList[:(carID-1)] + vehiclesList[carID:])
            return vehiclesList
        elif carID > len(vehiclesList) or carID < 0:         #carID is not in list
            print("You entered an invalid number.")

def add_new_vehicle():
    Make = input("Enter Make: ")
    Model = input("Enter Model: ")                          #Ask for a description of the car that needs to be added
    Year = input("Enter Year: ")
    Mileage = input("Enter Mileage: ")
    Price = input("Enter Price: ")
    new_car = [Make,Model,Year,Mileage,Price]
    
    return new_car                                          #Vehicle added to the vehiclesList list when it is passed back

def compareVehicles(vehiclesList):
    firstVehicle=int(input("First vehicle (enter a number):"))-1
    secondVehicle=int(input("Second vehicle (enter a number):"))-1
    vehicleInfo1=vehiclesList[firstVehicle]                 #set vehicleInfo to each selected option
    vehicleInfo2=vehiclesList[secondVehicle]

    print(vehicleInfo1[0],vehicleInfo1[1],"vs.",vehicleInfo2[0],vehicleInfo2[1],) #printing the title

    vehiclemake1=vehicleInfo1[1]
    vehiclemake2=vehicleInfo2[1]                            #set vehicle make to the make of each car, test if they are the same
    if vehiclemake1==vehiclemake2:                          #or different
        print("The two vehicles are the same makes.")
    else:
        print("The two vehicles are different makes.")

    year1=int(vehicleInfo1[2])
    year2=int(vehicleInfo2[2])
    if year1>year2:     #comparing year of the cars
        print("The first vehicle is newer.")
    elif year1<year2:
        print("The second vehicle is newer.")
    else:
        print("They where made the same year.")
    if int(vehicleInfo1[4])>int(vehicleInfo2[4]):
        print("The first vehicle costs more.")
    elif int(vehicleInfo1[4])<int(vehicleInfo2[4]):
        print("The second vehicle costs more.")
    else:
        print("The vehicles cost the same")

def searchFunc(vehiclesList):
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

def discountedCar(vehiclesList):
    carNumber = int(input("Which vehicle do you want to discount: "))-1
    while 0>carNumber or len(vehiclesList)-1<carNumber:
        if 0<=carNumber<=len(vehiclesList)-1:
            break
        else:
            print("vehicle not found")
            carNumber = int(input("Which vehicle do you want to discount: "))-1  
    discount = float(input("What percent discount (0-100): "))  
    while 0>discount or 100<discount:
        if 0<=discount<=100:
            break
        else:
            print("invalid discount")
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