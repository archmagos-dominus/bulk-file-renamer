#Bulk file rename

#imports
import os

#rename function
def main():
    #await user input as directory path
    dirname = input("Please enter a directory path:");
    #check if it is a directory
    if (not(os.path.isdir(dirname))):
        print("Directory not exists.")
        return
    #input the name that all the files will start with
    name = input("Please enter a root file name:\n")
    #iterate through all the files
    for count, filename in enumerate(os.listdir(dirname)):
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
        tmp = name + count + extension
        src = dirname + filename
        dst = dirname + tmp
        #rename the file
        os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

    # Calling main() function
    main()
