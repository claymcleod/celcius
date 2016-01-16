from __future__ import print_function

def confirm_command(cmd):
    print("The command celcius would like to run is:")
    print()
    print(cmd)
    print()
    return confirm()

def confirm():
    answer = raw_input("Would you like to continue? (Y/n) ")
    while answer.lower() not in ['', 'n', 'y']:
        print("Please enter 'y' or 'n'")
        answer = raw_input("Would you like to continue? (Y/n) ")

    if answer.lower() in ['', 'y']:
        return True

    return False

