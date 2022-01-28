# Need input as to whether they want to park
# DEF to remove tickets / remove parking spaces
# payment for parking // need to check if true/false {DICT}
    # store $cost per hour for parking
# input from USER for time in parkinggarage


# **********************************      START      *****************************************



class Garage():


    #main leavegarage function
    def __init__(self):
        self.current_dictionary = {}
        self.ticket_num = list(range(1, 101))
        self.parkingspaces_num = self.ticket_num
        self.car_number = 0
        #Asking user if they want to park, and adding car/ticket to dict & list
        self.ticket_dictionary()
        print(self.ticket_status)
        if self.ticket_status == 1:
            self.take_ticket()
        elif self.ticket_status == 0:
            print('Please leave or try again. ')
            self.ticket_dictionary()
            return
        else:
            print('You have not followed instructions, please try again. ')
            self.ticket_dictionary()
            return

        #this is to check how long they want to say, payment,  if payment was legit
        # done = False
        # while not done:
        self.pay_for_parking()
        if self.parking_payment == 'yes':
            ticket_payment = 'True'
            self.current_dictionary [self.car_number] = ticket_payment
            print('Congratulations! Your have completed your payment. You  have 15mins to leave or risk road rage from the person behind you. ')
            done = True
        elif self.parking_payment == 'no':
            ticket_payment = 'False'
            self.current_dictionary[self.car_number] = ticket_payment
            print('Your car will be impounded and you may be arrested. Please press any key to continue to payment and avoind night in jail. ')
            done = False
        else:
            ticket_payment = 'False'
            self.current_dictionary[self.car_number] = ticket_payment
            print('Please follow instructions. Your response made no sense. ')
            done = False
        if self.current_dictionary[self.car_number] == 'True':
            print('Thank you, have a nice day!')
            self.return_ticket()
            print(f'Display for next customer: we currently have {len(self.ticket_num)} spaces left. Drive Safely and remember, remember to keep your PythON and not PythOFF ')
            return

    #dictionary that starts by asking for whether you want to proceed and the adding to dictionary
    def ticket_dictionary(self):
        self.ticket_status = input('Would you like to take a ticket? (Yes = 1 / No = 0 / Quit) ')
        while True:
            try:
                self.ticket_status = int(self.ticket_status)
                break
            except ValueError:
                break
            except self.ticket_status.lower() == 'quit':
                break
        self.car_number += 1
        ticket_payment = 'False'
        car_make = input('What is the Make of your car? ')
        car_model = input('What is the Model of your car? ')
        car_year = input('What is the Year of your car? ')
        car_class = input('What is the Class of your car? (SUV/Coupe/Hot-Hatch)')
        self.current_dictionary[self.car_number] = ticket_payment, car_make , car_model, car_year, car_class
        print(self.current_dictionary)


    #function to take tickets, remove parking spaces,                 -----> Call this after ticket_dictionary (for self.ticket_status)
    def take_ticket(self):
        self.ticket_number = self.ticket_num[0:(len(self.ticket_num) - self.ticket_status)]
        self.parkingspaces_number = self.parkingspaces_num[0:(len(self.parkingspaces_num) - self.ticket_status)]

    #only if a ticket has been taken, otherwise it will go beyond     -----> Call this after ticket_dictionary (for self.ticket_status)
    def return_ticket(self):
        self.ticket_number = self.ticket_num[0:(len(self.ticket_num) + 1)]
        self.parkingspaces_num = self.parkingspaces_num[0:(len(self.parkingspaces_num) + 1)]
            



    # check for length of stay via input, 
    def pay_for_parking(self):
        self.parking_rate = 15
        self.parking_rate_info = print(f'The Hourly rate at this parking garage is ${self.parking_rate} ')
        self.parking_hours = input('How many hours would you like to park your car for? ')
        self.parking_hours_confirmation = print(f'Per your inputted length of stay, your total will be ${self.parking_rate * float(self.parking_hours)} ')
        print('Please insert your Credit Card or insert bills (smaller than $20). Please press any key to continue. ')
        self.parking_payment = input('Have you completed this transaction? (Yes / No) ').lower()
        if self.parking_payment == 'yes':
            ticket_payment = 'True'
            self.current_dictionary [self.car_number] = ticket_payment
        elif self.parking_payment == 'no':
            ticket_payment = 'False'
            self.current_dictionary[self.car_number] = ticket_payment
            return
        else:
            return
x = Garage()


# **********************************      END      *****************************************




# self.ticket_num = list(range(1, 100))
# parkingspaces_num = self.ticket_num
# self.ticket_status = int(input('Would you like to take a ticket? (Yes = 1 / No = 0) '))
# self.ticket_num = self.ticket_num[0:(len(self.ticket_num) - self.ticket_status)]
# parkingspaces_num = parkingspaces_num[0:(len(parkingspaces_num) - self.ticket_status)]
# print(self.ticket_num)
# print(parkingspaces_num)


# current_dictionary = {}
# self.ticket_num = list(range(1, 100))
# parkingspaces_num = self.ticket_num
# car_number = 0

# self.ticket_status = int(input('Would you like to take a ticket? (Yes = 1 / No = 0) '))
# car_number = self.ticket_status
# ticket_payment = 'False'
# car_make = input('What is the Make of your car? ')
# car_model = input('What is the Model of your car? ')
# car_year = input('What is the Year of your car? ')
# car_class = input('What is the Class of your car? (SUV/Coupe/Hot-Hatch)')
# current_dictionary[car_number] = ticket_payment, car_make, car_model, car_year, car_class

# print(current_dictionary)
