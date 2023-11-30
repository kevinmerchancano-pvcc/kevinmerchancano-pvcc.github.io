# Name: Kevin Merchancano
# Prog Purpuse: This program finds the cots of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables ##########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variable
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

##############  define program funtions ###############
def main():
    
    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more_tickets = False
            print("Thanks you for your order. Enjpy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sale_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax
    
def display_results():
    print('------------------------------')
    print('**** CINEMA HOUSE MOVIES ****')
    print('your neighborhood movie house')
    print('------------------------------')
    print('Tickets      $ ' + format(subtotal,'12,.3f'))
    print('Sales Tax    $ ' + format(sales_tax,'12,.3f'))
    print('Total        $ ' + format(total,'12,.3f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

##########  call on main program to execute ############
main()

