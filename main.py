from function import  display_total, customer_total_calc, system_boot, logo, print_menu, report, maint, make_coffee, run_coffee
import os
import pyfiglet

# Flag for Maintenance mode 
maint_mode = False

system_boot()

while not maint_mode:
    logo()

    name = input("what is your name?: ").lower()

    if name == 'off':
        maint()
        maint_mode = True
    elif name == 'report':
        print(report())
        report_exit = input("To Exit, type 'exit'")
        if report_exit == 'exit':
            os.system('clear')
    else:
        os.system('clear')

        print(f"{pyfiglet.figlet_format('Hello')} {pyfiglet.figlet_format(name)}\n")
        print_menu()

        selected_coffee = input('\nWhat would you like today? (Choose from selection above): ').lower()
        
        if selected_coffee == 'off':
            maint()
        elif selected_coffee == 'report':
            print(report())
            report_exit = input("To Exit, type 'exit'")
            if report_exit == 'exit':
                os.system('clear')
        elif selected_coffee == 'espresso':
            run_coffee(selected_coffee)
        elif selected_coffee == 'latte':
            run_coffee(selected_coffee)
        elif selected_coffee == 'cappuccino':
            run_coffee(selected_coffee)
        else:
            print('Incorrect Selection. Please select from the three options above.')
            selected_coffee = input('\nWhat would you like today? (Choose from selection above): ').lower()
            run_coffee(selected_coffee)