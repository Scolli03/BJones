from shutil import copy2
import os
import sys
import time
from typing import Counter, List

#Everything before the if __name__ == '__main__' line
#is just pre-defining the functions that we want to use
#in the script.

#function to undo the entire copy process
def undo_test(root, copied):
    """Undo the test by replacing the origional file in the dump folder and deleting the copied files

    Args:
        root (string): path to restore single copy of the copied files to
        copied (list): list of paths for all the copied files
    """
    #iterate over each copied file
    for file in copied:

        #make a variable that is the file origional path by
        #combining the root path and the copied files basename
        #which is the filename itself without the full path to it
        dump_loc = os.path.join(root, os.path.basename(file))

        #if we havent already copied this file back to the dump folder
        #do so, otherwise this is one of the other copies and we can just
        #remove it
        if not os.path.exists(dump_loc):
            copy2(file, dump_loc)
        
        #remove the copied file
        os.remove(file)

#function to validate the passed in path and either
#reassing the reference variable or append to it depending
#on the refernced vairables type
def validate_and_assign(path, assign_to):
    """Validate to ensure the entered path exists

    Args:
        path (string): The Path to be validated
        assign_to (string): the variable to assing the validated path

    Returns:
        bool: verdict of the validation check
    """
    #counter to use in junction with the isdir() check
    #to prevent the user from running into a infinite loop.
    #this way the while loop stops if the user fails to enter
    #a valid path 3 times
    counter = 0

    #according to the while statement, both the path must
    #not exist and the counter variable must be less than 3.
    #since we used the 'and' operator, if either of those statements
    #are incorrect the while loop ends.
    while not os.path.isdir(path) and counter < 3:

        #prompt user that the path is not valid and reassing the path variable
        #with this attempts response
        path = input(f"The path {path} is not valid, please try again...: ")

        #increment the counter by 1
        counter += 1

    #if the counter does NOT equal 3 then the user entered a valid path 
    #before they ran out of attempts
    if counter != 3:

        #if the variable to be assigned to is a list
        #then we append the passed to it
        if type(assign_to) == list:
            assign_to.append(path)

        #if the variable is a string, then we just reassing the 
        #variable to the passed in path
        elif type(assign_to) == str:
            assign_to = path
   
    #if the counter got to 3 then the user failed to enter a valid path
    #and we inform them and upon any input we exit the script here
    else:
        input("Was not able to validate replacement path...press any key to exit scrtip")
        sys.exit()

    #in the event the path was valid and the variable reassinged or appended to
    #then we return True so the line of code that called this function can check
    #against that value
    return True


# function to copy files from dump to mulitple locations
def copy_from_dump(root, copy_folders):
    """Copies files from defualt root directory
    into three other locations. Returns original
    and copied file paths for undoing the copy process.

    Args:
        root (string): The dump folder path
        copy_folders (list): list of paths of the copy to locations

    Returns:
        [list]: [list of the copie files paths]
    """

    #create an empty list to hold the paths of the 
    #new copies
    copied_files = []

    #create a files variable that will
    #contain a list of the filenames in the 
    #root folder thats returned from the 
    #listdir() function
    files = os.listdir(root)

    #iterate over the files in the list
    for file in files:

        #since listdir() returns just the filenames
        #join the root path to the filename to get the
        #full path to the file and assign to file_fullpath
        file_fullpath = os.path.join(root, file)

        #if the current file doesnt end with the defined
        #extension then it will be skipped
        if file.lower().endswith(".jpg"):

            #if its the right file type then we
            #iterate over each of the folder locations
            #we want to copy to and copy the file there
            for folder in copy_folders:

                #create a variable that will be the full path of
                #the copied file in the current copy to folder
                copy_loc = os.path.join(folder, file)

                #call the function to copy the file from
                #its current full path to the new full path
                copy2(file_fullpath, copy_loc)

                #append the new copied files full path
                #to our list
                copied_files.append(copy_loc)

            # remove original file
            os.remove(file_fullpath)
            
    #return the list of copied files in case the user wants
    #to undo the copy process
    return copied_files


if __name__ == '__main__':
    # set defualt dump folder
    root = r"Copy_Files\dump_folder"

    # provide user with defualt dump and ask if they would like to change it.
    # if the user presses Enter without typing anything then the input funtion will
    # return an empty string "" otherwise input will return the value the user
    # typed in. Assinging a variable to the input function call
    # we store what the user types into the variable.
    user_defined_root = input(
        f"The current dump folder is {root}.\nPress Enter key to accept this folder or enter new dump folder path: ")

    # if the user did enter a new path, validate it and assing the
    # new value to our root variable with our validate_and_assing function
    # otherwise we do nothing and root stays the default value
    if user_defined_root != "":
        validate_and_assign(user_defined_root, root)

    # The default copy to locations
    folders = [r"Copy_Files\Folder_1",
               r"Copy_Files\Folder_2",	r"Copy_Files\Folder_3"]

    # print out this statement followed by printing each of the
    # defualt folders on a new line that is tabbed in
    print(f"The following folders are the copy directories\n")

    for f in folders:
        print(f"\t{f}\n")

    # create a variable for the input message because we may need to change it
    # depending on what the user enters.
    message = """Enter new paths one at a time to add to current list of folders\n
								or multiple paths separated by a comma to replace current list: """

    # ask user if they would like to change the copy to locations
    # forcing the return value to lowercase with .lower() allows us
    # to ignore capitalization as "Y" is not the same as "y"
    change_folders = input(
        "Would you like to change the copy folders, Y/N?").lower()

    # if the user enters anything other than "y" this whole part
    # gets skipped and the default folders are used.
    if change_folders == "y":

        # create the variable to check against for the while loop
        accepted = False

        # This loop will continue forever unless the value of
        # accepted is changed to True
        while not accepted:

            # .split() allows us to split a continuous line of text
            # on a specified character and palce the resulting string
            # fragments into a list
            new_folder_s = input(message).split(",")

            # the length of the list can be gotten by passing the
            # list variable into the len() function. If the length
            # is greater than 1, then the user entered multiple paths
            # separated by commas.
            if len(new_folder_s) > 1:

                # we need to validate each of the entered paths
                for f in new_folder_s:
                    validated = validate_and_assign(f, folders)

                # if all paths are valid, we can just reassign
                # our folders variable to the new list. This will
                # replace the current value of the folders variable
                folders = new_folder_s

                # at this point we may exit the while loop by
                # making the condition check of the while loop
                # no longer valid
                accepted = True

            # if the length of the input list is equal to 1
            # then we must clear our current list so as not
            # to include any of the default folders since
            # we are not reassigning the variable. Then we
            # can validate, append, and prompt additional paths                
            elif len(new_folder_s) == 1:
                
                # clear defaults by setting current list to
                # an empty one
                folders = []

                # since the validate_and_assign function returns True if the path(s)
                # are valid. We can just use the function call in
                # the "if" statement rather than assing the function
                # to a variable and checking that.
                if validate_and_assign(new_folder_s[0], folders):
                    folders.append(new_folder_s[0])
                    message = "Enter another path or press Enter to continue."

            #if the user just pressed enter then they
            #are finished entering paths and we can leave 
            #the loop by changing the check condition
            elif new_folder_s == "":
                accepted = True

    #just a final input from the user to start the copy process
    input("Press any key to copy files")

    #pass our dump folder and list of copy locations to the
    #copy_from_dump function
    copied = copy_from_dump(root, folders)

    #in case this was a test or the user decides they want to
    #undo what the script just did they type the word undo into 
    #the prompt and the function will undo the copy process
    final_check = input(
        "Type \"undo\" to undo the recent run, or press Enter to exit script").lower()

    #the the user typed undo...run the undo_test function.
    if final_check == "undo":
        undo_test()

    #Thats it! This is where the script finishes.
