'''----------------Import Modules----------------'''
import dealer_tool as dealer
from test1 import *
import test2
import test3
import test4
import test5
import test6
import test7

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
    if option=="1":
        exec(test1)
    """if option=="2":
        test2
    if option=="3":
        test3
    if option=="4":
       test4    
    if option=="5":
        test5
    if option=="6":            
        test6
    if option=="7":
        test7"""




# Code reaches here after the loop ends
print("\nThanks for using this tool!"+"\nCome back soon!\n")