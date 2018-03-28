#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author          :SimplyPancake
#python_version  :2.7.6
#================================================================
				#SETUP
#================================================================
# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print"""

___       __________________________ ______
__ |     / /__(_)__  __/__    |__  /____  /____
__ | /| / /__  /__  /_ __  /| |_  __ \_  /_  _ \
__ |/ |/ / _  / _  __/ _  ___ |  /_/ /  / /  __/
____/|__/  /_/  /_/    /_/  |_/_.___//_/  \___/


v1.0
"""
    print "Please choose the Wi-Fi:"
    print "\n99. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Install
def installW():
    os.system('./install.py')
    return


# Run
def runW():
    os.system('cd InSc && python insRH.py')
    return

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': installW,
    '2': runW,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
