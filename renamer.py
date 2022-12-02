#Bulk file rename

#imports
import os

#main renamer function
def main():
    #await user input as directory path
    dir_name = input("Please enter a directory path:");
    #check if it is a directory
    if (not(os.path.isdir(dir_name))):
        print("Directory not exists.")
        return
    #input the name that all the files will start with
    root_name = input("Please enter a root file name:\n")
    #iterate through all the files
    for count, filename in enumerate(os.listdir(dir_name)):
        #get the file extension
        ext = filename.split(".")
        extension = "." + ext[-1]
        #in order to name files as xxx001 instead of xxx1
        #also, converts the count to string for the renaming
        if (count < 10):
            count = "00" + str(count)
        elif (count < 100):
            count = "0" + str(count)
        else:
            count = str(count)
        #make the new file name
        new_filename = root_name + count + extension
        src = dir_name + filename
        dst = dir_name + new_filename
        #rename the file
        os.rename(src, dst)

#Driver Code
if __name__ == '__main__':

    #Calling main() function
    main()
