"""
Author 		: Leeroy P. Williams
Date   		: 19.12.2018
Python Ver	: Python3
Version		: 1.4
Description	: Simple (CLI) text editor, allows for the user to write,
			  read and edit files. Whilst encrypting and decrypting
			  the documents.

Update		: Save location functionality added
"""

import re
import os
import pickle
from sys import exit

# Color Palate
white = "\33[37m"
green = "\33[32m"
red = "\33[31m"
blue = "\33[34m"
yellow = "\33[33m"

# Fonts

bold = "\33[1m"
cend = "\33[0m"
cblink = "\33[5m"

enter_symbol = green + "> " + white

def mainMenu():
	"""
		Start of the program, asks the user which mode they'd like
        to write their data in (r, w, a)
    """
	print(cblink + bold + blue + "\n\t\t\t\tWELCOME\n" + white + cend)
	print(yellow + 'Enter either "r" for reading a file, "w" for creating a new file, "a" to edit a file.\n' + white)

	choice = input(enter_symbol)

	if choice.lower() == 'r':
		read()
	elif choice.lower() == 'w':
		write()
	elif choice.lower() == 'a':
		edit()
	else:
		print(red + "NOT RECOGNIZED.\nQUITTING." + white)
		exit(0)

def savePoint():
	"""
		The location at which the documents should be saved or stored
	"""
	print("Current Directory:",os.getcwd())
	print("Do you wish to change the directory? [y/n]")
	choice = input(enter_symbol)
	if choice == 'y':
		location = os.chdir(input("Enter new directory: "))
		print(os.getcwd(), "--> loaded.")
	else:
		print("Using current directory.")

def read():
	"""
		Asks the user for the file to open in read mode.
		User is unable to make any edits to the file.
	"""
	savePoint()
	print(yellow + "Please enter the file name and I will open it.\n" + white)
	file = input(enter_symbol)

	try:
		with open(file, 'rb', encoding = None) as file_to_read:
			new_doc = pickle.load(file_to_read) # Load saved data into new_doc
			print(blue + new_doc + white)
			choice = input("\nSearch for a word in the file (y/n)?")

			#Search for file contents
			if choice == 'y' or choice == 'Y':

				word = input(green + ">" + white)
				search_file = re.compile(word)
				mod = search_file.findall(new_doc)

				if mod.group() in new_doc:
					print("Found: " + blue + mod.group() + white)
				else:
					print(red + "Not found" + white)

	except IOError as err:
		print(red + "File error", str(err) + white)

	except pickle.PickleError as perr:
		print(red + "Encrypting error", str(perr) + white)		
			
	print(yellow + '\nThose are the contents of the file.' + white)

	input()
	
def write():
	"""
		User creates a new file and writes data contents onto it.
	"""
	savePoint()
	print(yellow + "Enter file name.\n" + white)
	file = input(enter_symbol)

	try:
		with open(file, 'wb',) as file_to_write:
			print(yellow + "Enter text.\n" + white)
			paragraph = input(enter_symbol)
			pickle.dump(paragraph, file_to_write)

	except IOError as err:
		print(red + "File error", str(err) + white)

	except pickle.PickleError as perr:
		print(red + "Encrypting error", str(perr) + white)
		
	input()
	
def edit():
	"""
		User opens existing document and appends data onto it.
	"""
	savePoint()
	print(yellow + "Please enter the file name and I will open it.\n" + white)
	file = input(enter_symbol)

	try:
		with open(file, 'a', encoding = None) as file_to_read:
			file_to_read.writelines(input(enter_symbol))

	except IOError as err:
		print(red + "File error", str(err) + white)

	except pickle.PickleError as perr:
		print(red + "Encrypting error", str(perr) + white)

	input()
	
if __name__ == "__main__":
	mainMenu()
