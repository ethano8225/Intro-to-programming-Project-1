'''----------------Import Modules----------------'''
import dealer_tool as dealer

'''----------------Main program starts here----------------'''
print("\n==================================")
print("Dealership Vehicle Management Tool")
print("==================================")
print("")


#This While loop will keep asking for user inputs until the they simply press enter.
while True:
    dealer.display_menu()  
    option=input("Command (Enter to exit): ")
    
    if option=="":
        break
    ''' BEGIN MAKING YOUR CODE HERE '''
    #if option=="1":
        #test1()
    """if option=="2":
        test2
    if option=="3":
        test3
    if option=="4":
       test4    
    if option=="5":
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