from shutil import copy2
import os
import sys
import time
from typing import List

def undo_test(root, copied):
	for file in copied:
		dump_loc = os.path.join(root,os.path.basename(file))
		if not os.path.exists(dump_loc):
			copy2(file, dump_loc)
		os.remove(file)

def validate_and_assign(path,assign_to):

	while not os.path.isdir(path):
		input(f"The path {path} is not valid, please try again...: ")

	if type(assign_to) == list:
		assign_to.append(path)
	elif type(assign_to) == str:
		assign_to = path
	else:
		return False

	return True
		
		

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

	user_defined_root = input(f"The current dump folder is {root}.\nPress Enter key to accept this folder or enter new dump folder path: ")

	if user_defined_root != "":
		validated = validate_and_assign(user_defined_root,root)
		if not validated:
			input("Was not able to validate replacement path...press any key to exit scrtip")
			sys.exit()

	folders = [r"Copy_Files\Folder_1",	r"Copy_Files\Folder_2",	r"Copy_Files\Folder_3"]

	seporator = "\n\t"	

	print(f"The following folders are the copy directories\n")

	for f in folders:
		print(f"\t{f}\n")	

	
	message = """Enter new paths one at a time to add to current list of folders\n
								or multiple paths separated by a comma to replace current list: """
	change_folders = input("Would you like to change the copy folders, Y/N?").lower()
	accepted = False
	while not accepted:		
		if change_folders == "y":
			new_folder_s = input(message).split(",")
			if len(new_folder_s) > 1:
				for f in new_folder_s:
					validated = validate_and_assign(f,folders)
					if not validated:
						
				folders = new_folder_s
				accepted = True
			elif len(new_folder_s) == 1:
				validated = validate_and_assign(new_folder_s[0],folders)
				if validated:
					folders.append(new_folder_s)
					message = "Enter another path or press Enter to continue."
			elif new_folder_s == "":
				accepted = True






	input("Press any key to copy files")

	root, copied = copy_from_dump()

	undo_test()
