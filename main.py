from function import make_coffee, display_total, customer_total_calc, system_boot
import time
import os
import pyfiglet

# Flag for Maintenance mode 
maint_mode = False

## BELOW RUNS THE MACHINE

while not maint_mode:
    system_boot()
    
    name = input("what is your name?: ")
    print(f"{pyfiglet.figlet_format('Hello')} {pyfiglet.figlet_format(name)}\n")


    selected_coffee = input('\nWhat would you like today? (espresso/latte/cappuccino): ').lower()
    coin_collected = {
        "quaters": 0,
        "dimes": 0,
        "nickles": 0,
        "pennies": 0,        
    }
    display_total()
    quaters_collected = input('How many quaters would you like to insert?')
    dimes_collected = input('How many dimes would you like to insert?')
    nickles_collected = input('How many nickles would you like to insert?')
    pennies_collected = input('How many pennies would you like to insert?')

    customer_total = customer_total_calc(coin_collected["dimes"], coin_collected["nickles"], coin_collected["pennies"], coin_collected["quaters"])

    make_coffee(selected_coffee, customer_total, coin_collected)       

    time.sleep(2)
    os.system('clear')