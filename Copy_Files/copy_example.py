from shutil import copy2
import os

#function to copy files from dump to mulitple locations
def copy_from_dump():
	"""
	Copies files from defualt root directory
	into three other locations.
	"""

	#get contents of dump folder HINT(os module)
	root = r"dump_folder"
	folder1 = r"Folder_1"
	folder2 = r"Folder_2"
	folder3 = r"Folder_3"
	files = os.listdir(root)

	#iterate over files in specified folder HINT:(for loop) the os module
	for file in files:
		file_fullpath = os.path.join(root,file)
		#specify type of file your looking for
		if file.lower().endswith(".jpeg"):			
			#copy file to 3 different locations
			copy2(file_fullpath,os.path.join(folder1,file))
			copy2(file_fullpath,os.path.join(folder2,file))
			copy2(file_fullpath,os.path.join(folder3,file))
			#remove original file
			os.remove(file)

def print_name(name):
	print(name)

print("This was run in example.py before main check")

if __name__ == '__main__':
	
	copy_from_dump()