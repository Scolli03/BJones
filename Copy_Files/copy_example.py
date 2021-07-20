from shutil import copy2
import os

#function to copy files from dump to mulitple locations
def copy_from_dump():
	"""
	Copies files from defualt root directory
	into three other locations.
	"""

	#get contents of dump folder HINT(os module)
	root = r"C:\Users\shainc\Desktop\gom_scripts_shared"
	folder1 = "C:/folder1"
	folder2 = "C:/folder2"
	folder3 = "C:/folder3"
	files = os.listdir(root)

	#iterate over files in specified folder HINT:(for loop) the os module
	for file in files:
		file_fullpath = os.path.join(root,file)
		#specify type of file your looking for
		if file.endswith(".jpeg"):			
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
	print("this was run after main check")
	#copy_from_dump()