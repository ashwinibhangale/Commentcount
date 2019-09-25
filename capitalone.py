#import needed libraries
import tkinter # python library for GUI
from tkinter import filedialog # module in tkinter that supports opening and saving of files
from tkinter.filedialog import askopenfilename 
import re # python library for finding patterns / regular expressions
root = tkinter.Tk() # to create the initial window in gui
root.withdraw() # to prevent the root window from appearing and to directly get upload file option
FILE =  filedialog.askopenfilename(title = "Choose your file") # show a pop up box to ask for uploading file that needs to be scanned, it returns the path to the file
if(re.search(r'\.', FILE)): # To check if file path has '.' in it
    if(re.search(r'/\.',FILE)): # To check if file starts with '.'
        print("File starting with '.' has been ignored!")
        exit()
else:
    print("Extensionless File has been ignored!")
    exit()
if FILE:
    num_lines = sum(1 for line in open(str(FILE))) # Opens the file and adds 1 for each line
    print("Total # of lines:",num_lines) # Prints the total number of lines
    fileextension=FILE.split('.')[-1] # To extract the file extension
    # To initialise counters
    num_slcomments=0
    num_commentsinblocks=0
    num_blccomments=0
    num_TODO=0
    num_mmcomments=0
    # List to track if a line is comment or not 
    a=[]
    # Counter to track line number
    i=0
    if(fileextension=='py'): # For counting needed comment's details for python files
        for line in open(str(FILE)): # Loop for each line in the file
            if not re.search('#',line): # If there is no # in the line, we can consider it to be a no-comment line
                a.append('No')
                i=i+1
                continue
            cc=0 # Below code is to confirm if # is not present in a print statement or as a text
            flag=1
            for c in line: # c is each character in the line 
                if c in ['"',"'"]:
                    cc=cc+1
                if((c=='#') and (cc%2!=0)): # If there are odd number of quotes before #, it means that particular # is not commenting the line , eg: print("# This is not a comment")
                    flag=0
                if((c=='#') and (cc%2==0)):
                    flag=1
            if(flag==0):
                a.append('No')
                i=i+1
                continue
            a.append('Yes') # Add Yes to list since at this point # is present in line , and is not present in a text
            num_slcomments=num_slcomments+1   
            if('TODO' in line): 
                num_TODO=num_TODO+1
            if(i!=0 and a[i-1]=='Yes' and a[i]=="Yes"): # Checking if previous line is a comment, if yes, increment comments in block counter
                num_commentsinblocks=num_commentsinblocks+1
                if(i!=1 and a[i-1-1]=='No'): # Check if previous to previous line is not a comment : then this comment is a part of a block
                    num_blccomments=num_blccomments+1
            i=i+1
        # Display all the calculated data
        print("Total # of single line comments:",num_slcomments) # Prints the total number of lines
        print("Total # of comment lines within block comments:",num_commentsinblocks+num_blccomments) # Prints the total number of lines
        print("Total # of block line comments:",num_blccomments)
        print("Total # of TODO’s:",num_TODO)
else:
    print('Cancelled')

