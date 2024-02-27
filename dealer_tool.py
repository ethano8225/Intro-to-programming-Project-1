'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)




def display(vehicles_list):
    
    print("\tMake\tModel\tYear\tMileage\tPrice($)")



        # We probably need to write a program that loops here to iterate through every
        # variable in the vehicles_list, and display them during that process
    return 


def info(vehicles_list):

    
    
    
    return #more info on the selected cars?


def add_new_vehicle(vehicles_list):

    #Ask for a description of the car that needs to be added
    new_car = [input("What is the make"),input("What is the model"),input("What year"),input("What is the mileage"),input("What is the price")]
    vehicles_list += new_car #adds a new car to the end of the list
    

    return vehicles_list #Vehicle added to the list.