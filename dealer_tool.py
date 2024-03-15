'''----------------FILE FOR ALL OF THE FUNCTIONS NEED----------------'''
from test7 import *
def display_menu():
    """display the menu of options"""
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Search; 7-Discount")


#### To complete (all functions below)


def carlist():
    vehicle1=["Toyota","Camry","2018","45,000","20,000"]
    vehicle2=["Ford","Escape","2019","30,000","23,500"]
    vehicle3=["Honda","Accord","2017","60,000","16,200"]
    vehicle4=["Chevrolet","Silverado","2020","25,000","41,000"]
    vehicle5=["BMW","3 Series","2016","60,000","20,500"]
    vehicle6=["Nissan","Rogue","2019","40,000","17,800"]
    vehicle7=["Hyundai","Sonata","2018","42,000","16,500"]
    vehicle8=["Jeep","Wrangler","2021","15,000","32,000"]
    vehicle9=["Ford","Mustang","2015","50,000","22,000"]    
    vehicle10=["Volkswagen","Golf","2017","38,000","17,800"]
    vehicles=[vehicle1,vehicle2,vehicle3,vehicle4,vehicle5,vehicle6,vehicle7,vehicle8,vehicle9,vehicle10]
    return(vehicles) 


def discounted_vehicle(car_that_customer_want_discount, percent_discount, vehicleslist):
    if percent_discount < 0 or percent_discount > 100:
        print("Invalid discount!")
    else:
        vehicle = vehicleslist[int(car_that_customer_want_discount)-1]
        new_discounted_price = float(vehicle[4])*float(percent_discount/100)
        return new_discounted_price
    return 0


def display(vehicles_list):
    print("Make","Model","Year","Mileage","Price($)",sep="\t\t")
    i = 0

    while i < len(vehicles_list):
        vehicle = vehicles_list[i]
        print(vehicle[0],vehicle[1],vehicle[2],vehicle[3],vehicle[4],sep='\t\t')
        i = i+1  #probaby shjould be -1 but i dont wanna change without confimring with ethan.

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

