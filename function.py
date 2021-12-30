from coffee_list import MENU, resources, deposits
from logo import logo_1, logo_2, logo_3, logo_4, logo_5
import time
import os

def system_boot():
    '''prints loading logo'''
    os.system('clear')
    print(logo_1)
    time.sleep(0.65)
    os.system('clear')
    print(logo_2)
    time.sleep(0.65)
    os.system('clear')
    print(logo_3)
    time.sleep(0.65)
    os.system('clear')
    print(logo_4)
    time.sleep(0.65)
    os.system('clear')
    print(logo_5)
    time.sleep(0.65)
    os.system('clear')

def logo():
    print('''
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    ██       ██████   █████  ██████  ██ ███    ██  ██████           
    ██      ██    ██ ██   ██ ██   ██ ██ ████   ██ ██                
    ██      ██    ██ ███████ ██   ██ ██ ██ ██  ██ ██   ███          
    ██      ██    ██ ██   ██ ██   ██ ██ ██  ██ ██ ██    ██          
    ███████  ██████  ██   ██ ██████  ██ ██   ████  ██████  ██ ██ ██                                                               
    ''')

def print_menu():
    print('''
    ┌─┐┌─┐┌─┐┬─┐┌─┐┌─┐┌─┐┌─┐    
    ├┤ └─┐├─┘├┬┘├┤ └─┐└─┐│ │    
    └─┘└─┘┴  ┴└─└─┘└─┘└─┘└─┘    
    ┬  ┌─┐┌┬┐┌┬┐┌─┐             
    │  ├─┤ │  │ ├┤              
    ┴─┘┴ ┴ ┴  ┴ └─┘             
    ┌─┐┌─┐┌─┐┌─┐┬ ┬┌─┐┌─┐┬┌┐┌┌─┐
    │  ├─┤├─┘├─┘│ ││  │  │││││ │
    └─┘┴ ┴┴  ┴  └─┘└─┘└─┘┴┘└┘└─┘
    ''')

def run_coffee(coffee_type):
        display_total(coffee_type)
        coin_collected = {
            "quaters": 0,
            "dimes": 0,
            "nickles": 0,
            "pennies": 0,        
        }
        # below method is a bit annoying, maybe implent a better UI when entering coins. 
        print('**This machine takes $0.25, $0.10, $0.05, $0.01 ONLY**')
        coin_collected["quaters"] = int(input('How many quaters would you like to insert?: '))
        coin_collected["dimes"] = int(input('How many dimes would you like to insert?: '))
        coin_collected["nickles"] = int(input('How many nickles would you like to insert?: '))
        coin_collected["pennies"]= int(input('How many pennies would you like to insert?: '))
        print('')
        customer_total = round(customer_total_calc(coin_collected["dimes"], coin_collected["nickles"], coin_collected["pennies"], coin_collected["quaters"]), 2)

        make_coffee(coffee_type, customer_total, coin_collected)       

        time.sleep(3.5)
        os.system('clear')

def resource_check(coffee_type):
    '''Check if there are enough resources available to run coffee_choice()'''
    if coffee_type == 'espresso':
        if (resources['water'] > MENU['espresso']['ingredients']['water'] 
        and resources['coffee'] > MENU['espresso']['ingredients']['coffee']):
            return True
        else:
            return False

    if coffee_type == 'latte':
        if (resources['water'] > MENU['latte']['ingredients']['water'] 
        and resources['milk'] > MENU['latte']['ingredients']['milk'] 
        and resources['coffee'] > MENU['latte']['ingredients']['coffee']):
            return True
        else:
            return False

    if coffee_type == 'cappuccino':
        if (resources['water'] > MENU['cappuccino']['ingredients']['water'] 
        and resources['milk'] > MENU['cappuccino']['ingredients']['milk'] 
        and resources['coffee'] > MENU['cappuccino']['ingredients']['coffee']):
            return True
        else:
            return False

def customer_total_calc(d, n, p, q):
    '''Calculate the total money accepted from order'''
    customer_total = (d * 0.10) + (n * 0.05) + (p * 0.01) + (q * 0.25)
    return customer_total

def report():
    '''Report current resources'''
    gross_revenue = (deposits['quaters'] * 0.25)  + (deposits['dimes'] * 0.10) + (deposits['nickles'] * 0.05) + (deposits['pennies'] * 0.01)
    return (
    f'''
 Current resources:
    Water: {resources['water']}
    Milk: {resources['milk']}
    Coffee: {resources['coffee']}
    Quaters: {deposits['quaters']}
    Dimes: {deposits['dimes']}
    Nickles: {deposits['nickles']}
    Pennies: {deposits['pennies']}
    Total amount: ${round(gross_revenue, 2)}
    ''')
      
def maint():
    '''Initialize maintenance mode, turns off console.'''
    print('Maintenance mode initialized.')
    time.sleep(0.5)
    print('System shutting down in 3.')
    time.sleep(1)
    print('System shutting down in 2.')
    time.sleep(1)
    print('System shutting down in 1.')

def check_total(coffee_type, coins):
    '''Check accepted coins and return True or False for this function to run under coffee_choice() to run'''
    if coffee_type == 'espresso': 
        if coins >= MENU['espresso']['cost']:
            return True
        elif coins <= MENU['espresso']['cost']:
            return False
    elif coffee_type == 'latte':
        if coins >= MENU['latte']['cost']:
            return True
        elif coins <= MENU['latte']['cost']:
            return False
    elif coffee_type == 'cappuccino':
        if coins >= MENU['cappuccino']['cost']:
            return True
        elif coins <= MENU['cappuccino']['cost']:
            return False

def display_total(coffee_type):
    '''Display total due with full statement "total due:....."'''
    if coffee_type == 'espresso':
        print(f"Total due: {MENU['espresso']['cost']}0")
    elif coffee_type == 'latte':
        print(f"Total due: {MENU['latte']['cost']}0")
    elif coffee_type == 'cappuccino':
        print(f"Total due: {MENU['cappuccino']['cost']}0")

def update_resources(coffee_type, coin_collected):
    # update quaters to deposits
    #BUG DOES NOT UPDATE coffee_list.py, need to pickle or json, data stored until reset.
    deposits["quaters"] += coin_collected["quaters"]
    # update dimes to deposits
    #BUG DOES NOT UPDATE coffee_list.py, need to pickle or json, data stored until reset.
    deposits["dimes"] += coin_collected["dimes"]
    # update nickles to deposits
    #BUG DOES NOT UPDATE coffee_list.py, need to pickle or json, data stored until reset.
    deposits["nickles"] += coin_collected["nickles"]
    # update pennies to deposits
    #BUG DOES NOT UPDATE coffee_list.py, need to pickle or json, data stored until reset.
    deposits["pennies"] += coin_collected["pennies"]
    #subtract each required resources from resource dictionary
    #BUG DOES NOT UPDATE coffee_list.py, need to pickle or json, data stored until reset.
    if coffee_type == "espresso":
        resources["water"] -= MENU['espresso']['ingredients']["water"]
        resources["coffee"] -= MENU['espresso']['ingredients']["coffee"]
    elif coffee_type == "latte":
        resources["water"] -= MENU['latte']['ingredients']["water"]
        resources["coffee"] -= MENU['latte']['ingredients']["coffee"]
        resources["milk"] -= MENU['latte']['ingredients']["milk"]
    elif coffee_type == "cappuccino":
        resources["water"] -= MENU["cappuccino"]['ingredients']["water"]
        resources["coffee"] -= MENU["cappuccino"]['ingredients']["coffee"]
        resources["milk"] -= MENU["cappuccino"]['ingredients']["milk"]

def provide_change(coffee_type, collected_amount):
    '''Calculates the change needed to provide and subtracts available coins to provide change to user'''
    total_change = collected_amount - MENU[coffee_type]['cost']
    # goes through coins and provide change based on what's available. 
    c = (total_change * 10) * 10
    quaters = c // 25
    deposits["quaters"] -= quaters #1 become 0
    if deposits["quaters"] < 0:
        c = abs(deposits["quaters"])
        deposits["quaters"] = 0
        c = c % 10
        deposits["dimes"] -= c
        if deposits["dimes"] < 0:
            c = abs(deposits["dimes"])
            deposits['dimes'] = 0
            c = c % 5
            deposits["nickles"] -= c
            if deposits["nickles"] < 0:
                c = abs(deposits["nickles"]) 
                deposits["nickles"] = 0
                c = c % 1
                deposits["pennies"] -= c
    return total_change
    
def make_coffee(coffee_type, collected_amount, coin_collected):
    '''Main function that checks which coffee was selected, check_resource(), check_total(), update_resources(), and provide_change() if needed.'''
    # check which coffee choice
    if coffee_type == 'espresso':
        espresso = resource_check('espresso')
        # check resource
        if espresso == True:
            check = check_total('espresso',collected_amount)
            # check money
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....\n')
                update_resources(coffee_type, coin_collected)
                # provide change
                if collected_amount > MENU['espresso']['cost']:
                    print(f"Your total change: ${round(provide_change(coffee_type, collected_amount), 3)} will be dispensed now.\n")
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!')
            else:
                balance_due = MENU[coffee_type]["cost"] - collected_amount
                print(f'Not enough coins. You are ${balance_due} short. Money refunded.\n')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized\n')
            maint()
            maint_mode = True
    elif coffee_type == 'latte':
        latte = resource_check('latte')
        # check resource
        if latte == True:
            check = check_total('latte',collected_amount)
            # check money
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....\n')
                update_resources(coffee_type, coin_collected)
                # provide change
                if collected_amount > MENU['latte']['cost']:
                    print(f"Your total change: ${round(provide_change(coffee_type, collected_amount), 3)} will be dispensed now.\n")
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!\n')
            else:
                balance_due = MENU[coffee_type]["cost"] - collected_amount
                print(f'Not enough coins. You are ${balance_due} short. Money refunded.\n')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized\n')
            maint()
            maint_mode = True
    elif coffee_type == 'cappuccino':
        cappuccino = resource_check('cappuccino')
        # check resource
        if cappuccino == True:
            check = check_total('cappuccino',collected_amount)
            # check money
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....\n')
                update_resources(coffee_type, coin_collected)
                # provide change
                if collected_amount > MENU['cappuccino']['cost']:
                    print(f"Your total change: ${round(provide_change(coffee_type, collected_amount), 2)} will be dispensed now.\n")
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!\n')
            else:
                balance_due = MENU[coffee_type]["cost"] - collected_amount
                print(f'Not enough coins. You are ${balance_due} short. Money refunded.\n')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized\n')
            maint()
            maint_mode = True
    elif coffee_type == 'off':
        maint()
        maint_mode = True
    elif coffee_type == 'report':
        print(report())
        report_exit = input("To Exit, type 'exit'")
        if report_exit == 'exit':
            os.system('clear')
    else:
        print("Invalid Coffee Selection, try again.\n")
