#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os, pickle

ITEMS = {}

menu_actions  = {}  
 
clear = 'cls'
# clear = 'clear'


def main_menu():
    os.system(clear)
    print "Welcome,\n"
    print "Please choose the menu you want to start"
    print "Your options are:"
    print
    print "1. Add a new item into the database"
    print "2. Delete an item from the database"
    print "3. Search for an existing item by name"
    print "4. Display all "
    print "\n0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
 
    return


def exec_menu(choice):
    os.system(clear)
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

def add_item():
    print "Hello would you like to add an item?\n"
    global ITEMS
    PID = input('\nEnter product ID: ')
    PRODUCT = raw_input('\nEnter new item: ')
    MANU = raw_input('\nEnter the manufacturer: ')
    SNUMBER = raw_input('\nEnter the serial number: ')
    PRICE = raw_input('\nEnter the price of the item: ')
    INSTALL = raw_input('\nINSTALLATION FEE: ')
    ITEMS[PID] = [PRODUCT, MANU, SNUMBER, PRICE, INSTALL]
    print "9. Back"
    print "0. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
 

def remove_item():
    print "Hello would you like to remove an item?\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def search_item_menu():
    print "Hello would you like to search for an existing item?\n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return

def view_item():
    print "Hello would you like to view all  \n"
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 

def back():
    menu_actions['main_menu']()
 
#save menu to file successfully
def exit():
    global ITEMS
    try:
        inventory = open('inventory', 'wb')
        pickle.dump(ITEMS, inventory)
    except (IOError, EOFError):
        sys.exit()
 

menu_actions = {
    'main_menu': main_menu,
    '1': add_item,
    '2': remove_item,
    '3': search_item_menu,
    '4': view_item,
    '9': back,
    '0': exit,
}
 

if __name__ == "__main__":
    global ITEMS
    ITEMS = pickle.load(open("inventory", 'rb'))
    print "Successfully loaded"
    print ITEMS
    main_menu()
