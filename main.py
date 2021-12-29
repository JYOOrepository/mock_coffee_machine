from coffee import MENU, resources
import time
import os

# Flag for Maintenance mode 
maint_mode = False

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

def report():
    '''Report current resources'''
    gross_revenue = (resources['quaters'] * 0.25)  + (resources['dimes'] * 0.10) + (resources['nickles'] * 0.05) + (resources['pennies'] * 0.01)
    return (
    f'''
    Current resources:
    Water: {resources['water']}
    Milk: {resources['milk']}
    Coffee: {resources['coffee']}
    Quaters: {resources['quaters']}
    Dimes: {resources['dimes']}
    Nickles: {resources['nickles']}
    Pennies: {resources['pennies']}
    total: {gross_revenue}
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
    '''Display total due'''
    if coffee_type == 'espresso':
        print(f"Total due: {MENU['espresso']['cost']}")
    elif coffee_type == 'latte':
        print(f"Total due: {MENU['latte']['cost']}")
    elif coffee_type == 'cappuccino':
        print(f"Total due: {MENU['cappuccino']['cost']}")

def update_resources(coffee_type, collected_amount):
    #add collected money
    #subtract each required resources from resource dictionary
    print("work on this function")

#TODO
def provide_change():
    print("work on this function")
    #first find how much to provide change for.
    #create a equation that figures out exactly how many quater and how many nickles and how many pennies needed for change
    #subtract each coin for refund from resources


def make_coffee(coffee_type, collected_amount):
    '''Main function that checks which coffee was selected, check_resource(), check_total(), update_resources().'''
    enough_resource = True
    # check which coffee choice
    if coffee_type == 'espresso':
        espresso = resource_check('espresso')
        # check resource
        if espresso == True:
            check = check_total('espresso',collected_amount)
            # check money
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....')
                update_resources(coffee_type, collected_amount)
                # provide change
                if collected_amount > MENU['espresso']['cost']:
                    provide_change()
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!')
            else:
                print('Not enough coins.')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized')
            maint()

    elif coffee_type == 'latte':
        latte = resource_check('latte')
        if latte == True:
            check = check_total('latte', collected_amount)
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....')
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!')
            else:
                print('Not enough coins.')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized')
            maint()

    elif coffee_type == 'cappuccino':
        cappuccino = resource_check('cappuccino')
        if cappuccino == True:
            check = check_total('cappuccino', collected_amount)
            if check == True:
                print(f'Preparing your {coffee_type}, please wait....')
                time.sleep(3)
                print(f'Your {coffee_type} is ready. Have a nice day!')
            else:
                print('Not enough coins.')
        else:
            print('Not enough resources to make coffee, maintenance mode intialized')
            maint()
    elif coffee_type == 'off':
        maint()
        maint_mode = True
    elif selected_coffee == 'report':
        print(report())
    else:
        print("Invalid Selection.")

## ABOVE ARE ALL FUNCTIONS

## BELOW RUNS THE MACHINE

while not maint_mode:

    selected_coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()
    customer_total = 0
    display_total()


    check_total(selected_coffee, customer_total)

    make_coffee(selected_coffee, customer_total)
    
    # payment_finished = False
    # while not payment_finished:
        
    #     collected = input('Insert Coin, q, d, p: ').lower()
    #     done = input("Finished? 'y' 'n' ").lower()
    #     if done == 'y':
    #         payment_finished = True
    #     elif done == 'n':
    #         payment_finished = False
    #     if collected == 'q':
    #         customer_total += 0.25
    #     elif collected == 'd':
    #         customer_total += 0.10
    #     elif collected == 'p':
    #         customer_total += 0.01
         




# process change
# process adding coins to resources add total coins
# process 
    
    time.sleep(2)
    os.system('clear')