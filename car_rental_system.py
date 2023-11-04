print("-------------Welcome to Car Rental Management System-------------")

global credit
global car_list
car_list=["BMW","HONDA","SUZUKI"]

global check_list
check_list = []
def main_user():
    def search_cars():
        pass
    def car_work():
        credit=int(input("Please enter your credits/money before going on to main procedures ($): "))
        print("1.) Display Cars ")
        print("2.) Buy Cars ")
        print("3.)Exit")
        c = int(input("Now select a option from above : "))
        if c==1:
            print("These are the car brands available : ")
            for i in range(0,len(car_list)):
                print(f"{i}.){car_list[i]}") 
            car_work()
        elif c==2:
            print("1.) Buy From A Specific Brand\n")
            print("2.) Rent a car for a limited time\n")
            g = int(input("SELECT A OPTION FROM ABOVE : "))
            if g==1:
                for i in range(0,len(car_list)):
                    print(f"{i}.){car_list[i]}")     
                carchoice = int(input("Enter a car brand name to see the models available for that specific car"))
                if carchoice==0:
                    print("These are the models available under BMW : ")
                    print("1.)BMW X5 , cost = 10 Lakhs")
                    print("2.)BMW X1 , cost = 50 Lakhs")
                    print("3.)BMW M4 , cost = 90 Lakhs")
                    print("4.)BMW 7 Series , cost = 45 Lakhs")
                    f=int(input("Enter the car model you want to buy : "))
                    if f==1:
                        if 1000000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the BMW X5 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-1000000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==2:
                        if 5000000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the BMW X1 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-5000000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==3:
                        if 9000000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the BMW M4 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-9000000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==4:
                        if 4500000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the BMW 7 Series , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-4500000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                elif carchoice==1:
                    print("These are the models available under HONDA : ")
                    print("1.)HONDA CITY 4th Gen , cost = 9 Lakhs")
                    print("2.)HONDA AMAZE, cost = 11 Lakhs")
                    print("3.)HONDA Jazz, cost = 8 Lakhs")
                    f=int(input("Enter the car model you want to buy : "))
                    if f==1:
                        if 900000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda City 4th Gen model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-900000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==2:
                        if 1100000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Amaze model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-1100000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==3:
                        if 800000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Jazz model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-800000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                elif carchoice==2:
                    print("These are the models available under SUZUKI : ")
                    print("1.)Suzuki SWIFT , cost = 5 Lakhs")
                    print("2.)Suzuki BREZZA , cost = 7 Lakhs")
                    print("3.)Suzuki BALENO, cost = 10 Lakhs")
                    f=int(input("Enter the car model you want to buy : "))
                    if f==1:
                        if 500000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda City 4th Gen model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-500000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==2:
                        if 700000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Amaze model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-700000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==3:
                        if 1000000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Jazz model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-1000000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                else:
                    print("entered wrong option,please enter again\n")
                    car_work()
            elif g==2:
                for i in range(0,len(car_list)):
                    print(f"{i}.){car_list[i]}")     
                carchoice = int(input("Enter a car brand name to see the models available for that specific car"))
                if carchoice==0:
                    print("These are the models available under BMW : ")
                    print("1.)BMW X5 , cost = 50k for renting for a day")
                    print("2.)BMW X1 , cost = 20k for renting for a day")
                    print("3.)BMW M4 , cost = 10k for renting for a day")
                    print("4.)BMW 7 Series , cost = 40k for renting for a day")
                    f=int(input("Enter the car model you want to RENT : "))
                    if f==1:
                        if 50000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the BMW X5 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-50000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                    if f==2:
                        if 20000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the BMW X1 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-20000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                    if f==3:
                        if 10000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the BMW M4 model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-10000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                    if f==4:
                        if 40000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the BMW 7 series , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-40000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                elif carchoice==1:
                    print("These are the models available under HONDA : ")
                    print("1.)HONDA CITY 4th Gen , cost = 5k for renting for a day")
                    print("2.)HONDA AMAZE, cost = 7k for renting for a day")
                    print("3.)HONDA Jazz, cost = 4k for renting for a day")
                    f=int(input("Enter the car model you want to buy : "))
                    if f==1:
                        if 5000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the Honda City 4th Gen model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-5000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                    if f==2:
                        if 7000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the Honda Amaze model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-7000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                    if f==3:
                        if 4000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are renting the Honda Jazz model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully rented the car")
                                credit=credit-4000
                                print(f"Your balance credit ($) after renting is {credit}")
                                car_work()
                elif carchoice==2:
                    print("These are the models available under SUZUKI : ")
                    print("1.)Suzuki SWIFT , cost = 5 Lakhs")
                    print("2.)Suzuki BREZZA , cost = 7 Lakhs")
                    print("3.)Suzuki BALENO, cost = 10 Lakhs")
                    f=int(input("Enter the car model you want to buy : "))
                    if f==1:
                        if 500000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda City 4th Gen model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-500000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==2:
                        if 700000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Amaze model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-700000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                    if f==3:
                        if 1000000>credit:
                            print("Insufficient funds , please enter again :")
                            car_work()
                        else:
                            u=input("You are buying the Honda Jazz model , please enter (y/n) for confirmation : ")
                            if u=='y':
                                print("Succesfully brought the car")
                                credit=credit-1000000
                                print(f"Your balance credit ($) is {credit}")
                                car_work()
                else:
                    print("entered wrong option,please enter again\n")
                    car_work()
        elif c==3:
            exit()
        else:
            print("Wrong option")
            car_work()
    print("Hello! Choose one of the options below ;\n",end=' ')
    print("1.) Existing User (IF ALDREADY LOGIN DONE)\n")
    print("2.) New Login\n")
    n = int(input("Enter any choice (1-2)"))
    if n == 2:
        uservar = ""
        uservar = input("Enter your Username : ")
        if (uservar.isalnum()):
            pass
        else:
            print("Entered username is invalid")
            main_user()
        pw = ""
        pw = input("Enter the password : ")
        if (pw.isalnum()):
            pass
        else:
            print("Entered password is invalid")
            main_user()
        check_list.append([uservar,pw]) #Appending the username and password in a nested list
        #print(check_list)
        main_user()
    if n == 1:
        if check_list == []:
            print("Invalid , Please go to New Login")
            main_user()
        tempuser = input("Enter your username : ") #user name input
        temppw = input("Enter your password : ") #password input
        rec = [tempuser,temppw] #-->1)adding username and password in a list
        for i in check_list:
            if i == rec:  #-->2)Checking if the nested list is equal to the entered credentials.
                car_work() #If ok,moving on to the main car functions
            else:
                print("Entered credentials are invalid please login again\n")
                main_user()




def main_login():
    print("1.) USER Login \n")
    print("2.) EXIT\n")
    ch=int(input("ENTER THE NUMBER : "))
    if ch==1:
        main_user()
    elif ch==2:
        exit()
main_login()






      
