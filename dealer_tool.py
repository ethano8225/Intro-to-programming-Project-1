'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)

def discounted_vehicle(car_that_customer_want_discount, percent_discount, vehicleslist):
    if percent_discount < 0 or percent_discount > 100:
        print("Invalid discount!")
    else:
        vehicle = vehicleslist[int(car_that_customer_want_discount)-1]
        new_discounted_price = float(vehicle[4])*float(percent_discount/100)
        return new_discounted_price
    return 0


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
    
    
    
    return 0#more info on the selected cars?


def add_new_vehicle(vehicles_list):

    #Ask for a description of the car that needs to be added
    new_car = [input("What is the make"),input("What is the model"),input("What year"),input("What is the mileage"),input("What is the price")]
    vehicles_list += new_car #adds a new car to the end of the list
    
    return vehicles_list #Vehicle added to the list.

