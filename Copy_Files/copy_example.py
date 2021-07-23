from shutil import copy2
import os
import sys
import time

def undo_test(root, copied):
	for file in copied:
		dump_loc = os.path.join(root,os.path.basename(file))
		if not os.path.exists(dump_loc):
			copy2(file, dump_loc)
		os.remove(file)

def validate_input(user_path):
	#boolean to determine if user enters correct input
	valid = False

	#check if input folder is real folder
	if not os.path.isdir(user_path):
		print(f"The entered path:{user_path} is not valid, PLease try again.")
	else:
		root = user_path
		valid = True

	return valid

#function to copy files from dump to mulitple locations
def copy_from_dump():
	"""
	Copies files from defualt root directory
	into three other locations. Returns original
	and copied file paths for undoing the copy process.
	"""

	copied_files = []
	
	files = os.listdir(root)

	#iterate over files in specified folder HINT:(for loop) the os module
	for file in files:
		file_fullpath = os.path.join(root,file)
		#specify type of file your looking for
		if file.lower().endswith(".jpg"):
			
			#copy file to 3 different locations
			for folder in folders:
				copy_loc = os.path.join(folder,file)
				copy2(file_fullpath, copy_loc)
				copied_files.append(copy_loc)
			#remove original file
			os.remove(file_fullpath)


	return root, copied_files


if __name__ == '__main__':
	#set defualt dump folder
	root = r"Copy_Files\dump_folder"

	user_defined_root = input(f"The current dump folder is {root}.\nPress any key to accept this folder or enter new dump folder path: ")

	if user_defined_root != "":
		while not validate_input(user_defined_root)

	folders = [r"Copy_Files\Folder_1",	r"Copy_Files\Folder_2",	r"Copy_Files\Folder_3"]

	print("The following folders are the copy directories")

	for folder in folders:
		print(folder)

	change_folders = ""
	while change_folders != "Y" or change_folders != "N":
		change_folders = input("Are the current copy folders correct Y/N?")
		if change_folders != "Y" or change_folders != "N":
			print("That is not a valid input, please enter \"Y\" or \"N\"")
			change_folders = ""

	if change_folders == "Y":
		new_folder = input("Enter first new ouput folder: ")


	input("Press any key to copy files")

	root, copied = copy_from_dump()

	undo_test()