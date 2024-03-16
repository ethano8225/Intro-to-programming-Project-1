'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)


def display(vehicles_list):
    print("Car #"+"\t"+"Make","Model","Year","Mileage","Price($)",sep="\t\t")
    print("---------------------------------------------------------------------------------")
    i = 0

    while i < len(vehicles_list):    # This is terrible code but the seperator \t is not working nicely when just used as
        vehicle = vehicles_list[i]   # the seperator, so i must test for different lengths and adjust accordingly
        if len(vehicle[0]) > 8 and len(vehicle[1]) >= 8:
            print(str(i+1),vehicle[0],vehicle[1],vehicle[2]+"\t\t"+vehicle[3]+"\t\t"+vehicle[4],sep="\t")
        elif len(vehicle[0]) > 8 and len(vehicle[1]) < 8:
            print(str(i+1)+"\t"+vehicle[0]+"\t"+vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        elif len(vehicle[0]) <= 8 and len(vehicle[1]) >= 8:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1]+"\t"+vehicle[2],vehicle[3],vehicle[4],sep="\t\t")
        else:
            print(str(i+1)+"\t"+vehicle[0],vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep='\t\t')
        i = i+1

        # We probably need to write a program that loops here to iterate through every
        # variable in the vehicles_list, and display them during that process
    return 0


def info(vehicles_list):
    print("#Vehicles",str(len(vehicles_list)),"\n")
    lessthan10 = 0
    tento20 = 0
    twentyTo30 = 0
    thirtyTo40 = 0
    fourtyup = 0
    for i in vehicles_list:
        if int(i[4]) < 10000:
            lessthan10 = lessthan10+1
        elif int(i[4]) >= 10000 and int(i[4]) < 20000:
            tento20 = tento20+1
        elif int(i[4]) >= 20000 and int(i[4]) < 30000:
            twentyTo30 = twentyTo30+1
        elif int(i[4]) >= 30000 and int(i[4]) < 40000:
            thirtyTo40 = thirtyTo40+1
        elif int(i[4]) >= 40000:
            fourtyup = fourtyup+1


    print("<10,000 : ",100*(lessthan10/len(vehicles_list)),"%",sep="")
    print("10,000s : ",100*(tento20/len(vehicles_list)),"%",sep="")
    print("20,000s : ",100*(twentyTo30/len(vehicles_list)),"%",sep="")
    print("30,000s : ",100*(thirtyTo40/len(vehicles_list)),"%",sep="")
    print(">=40,000 : ",100*(fourtyup/len(vehicles_list)),"%\n",sep="")

    total = 0
    i = 0
    while i < len(vehicles_list):
        vehicle = vehicles_list[i]
        price = int(vehicle[4])
        total = total + price
        i = i + 1
    print("Mean Price:",str(total/len(vehicles_list)))

def add_new_vehicle(vehicles_list):

    #Ask for a description of the car that needs to be added
    new_car = [input("What is the make"),input("What is the model"),input("What year"),input("What is the mileage"),input("What is the price")]
    vehicles_list += new_car #adds a new car to the end of the list
    
    return vehicles_list #Vehicle added to the list.
