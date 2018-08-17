"""
Author 		: Leeroy P. Williams
Date   		: 06/06/18
Code_Base	: Python3
Version		: 1.1
Description	: Simple (CLI) text editor, allows for the user to write,
			  read and edit files.
"""

import os
import pickle
from sys import exit


def mainMenu():
	"""
		Start of the program, asks the user which mode they'd like
        to write their data in (r, w, a)
    """
	print("\n\t\t\t\tWelcome.")
	print('''=> Enter either "r" for reading a file, "w" for creating a new file "a" for opening previous work and continuing in it.''')

	choice = input('-> ')

	if choice.lower() == 'r':
		read()
	elif choice.lower() == 'w':
		write()
	elif choice.lower() == 'a':
		edit()
	else:
		print("Not recognized.\nQuitting the program.")
		exit(0)
			


def read():
	"""
		Asks the user for the file to open in read mode.
		User is unable to make any edits to the file.
	"""
	print("Please enter the file name and I will open it.\n")
	file = input('-> ')

	try:
		with open(file, 'rb', encoding = None) as file_to_read:
			new_doc = pickle.load(file_to_read) # Load saved data into new_doc
			print(new_doc)

	except IOError as err:
		print("File error", str(err))

	except pickle.PickleError as perr:
		print("Pickling error", str(perr))		
			
	print('\nThose are the contents of the file.')

def write():
	"""
		User creates a new file and writes data contents onto it.
	"""
	print("Please enter the file name and I will open it.\n")
	file = input('-> ')

	try:
		with open(file, 'wb',) as file_to_write:
			paragraph = input('-> ')
			pickle.dump(paragraph, file_to_write)

	except IOError as err:
		print("File error", str(err))

	except pickle.PickleError as perr:
		print("Pickling error", str(perr))

def edit():
	"""
		User opens existing document and appends data onto it.
	"""
	print("Please enter the file name and I will open it.\n")
	file = input('-> ')

	try:
		with open(file, 'a', encoding = None) as file_to_read:
			file_to_read.writelines(input('->\n '))

	except IOError as err:
		print("File error", str(err))

	except pickle.PickleError as perr:
		print("Pickling error", str(perr))

if __name__ == "__main__":
	mainMenu()