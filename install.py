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

Please run Wif-Able installer with administrator priveleges!
With installing this script people who use your network give permission to use their devices as crypto-miners.
"""
    print "Please choose the menu you want to start:"
    print "1.   Install Wif-Able"
    print "2.   Run Wif-Able(!not running will not make you money!)"
    print "3.   Switch between AP mode and CLient mode"
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
    #Here we go!!
    # https://www.youtube.com/watch?v=5hO4kLHZQIY
    # http://ozzmaker.com/add-colour-to-text-in-python/

    os.system('clear')
    print "\033[0;37;41m Updating dependencies... This might take a while..."
    os.system('sudo apt-get update')
    os.system('clear')
    os.system('sudo apt-get install hostapd bridge-utils -y')
    os.sytem('sudo systemctl stop hostapd')
    return


# Run
def runW():
    print "Make sure Wif-Able is installed first!"
    os.system('sudo ./runcrypto.sh')
    return

def swapW():
    print "Swapping between AP mode and Client mode!"
    os.system('sudo swapwifi')

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
    '3': swapW,
    '99': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
