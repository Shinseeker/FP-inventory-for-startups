#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final Project for IS210."""

import sys, os, pickle

ITEMS = {}

menu_actions  = {}  
 
clear = 'cls'
# clear = 'clear'


def main_menu():
    """Function for the menu."""
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
    """function that executes the menu."""
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
    """function that adds items into the inventory."""
    print "Add an item.\n"
    global ITEMS
    PID = raw_input('\nEnter product ID: ')
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
    """A function that removes an item."""
    print "Remove an item.\n"
    global ITEMS
    REMOVE = raw_input('\nEnter the item you wish to delete: ')
    if REMOVE in ITEMS:
        del ITEMS[REMOVE]
        print REMOVE,':', 'Has been removed from the the inventory'
    else:
        print '---------------------------''\n'
        print REMOVE.upper(), ':', 'Does not exist in the inventory!'
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def search_item_menu():
    """A function that searchs for one item."""
    print "Hello would you like to search for an existing item?\n"
    SEARCH = raw_input('\nWhat item are you looking for? ')
    print '---------------------------''\n'
    if SEARCH in ITEMS:
        print SEARCH, ITEMS[SEARCH]
    else:
        print SEARCH , 'This item does not exist in the inventory!'
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return


def view_item():
    """A function that displays all items."""
    print "Hello would you like to view all  \n"
    print '-------------------------------''\n'
    print ITEMS
    print '-------------------------------''\n'
    print "9. Back"
    print "0. Quit" 
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 

def back():
    """Function that goes back the main."""
    menu_actions['main_menu']()

 
#save menu to file successfully
def exit():
    """Exits the program and saves the data."""
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
    try:
        ITEMS = pickle.load(open("inventory", 'rb'))
        print "Successfully loaded"
        print ITEMS
    except (IOError, EOFError):
        ITEMS = {}
    main_menu()
