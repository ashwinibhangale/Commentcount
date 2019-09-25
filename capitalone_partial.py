#import needed libraries
import tkinter # python library for GUI
from tkinter import filedialog # module in tkinter that supports opening and saving of files
from tkinter.filedialog import askopenfilename 
import re # python library for finding patterns / regular expressions
root = tkinter.Tk() # to create the initial window in gui
root.withdraw() # to prevent the root window from appearing and to directly get upload file option
FILE =  filedialog.askopenfilename(title = "Choose your file") # show a pop up box to ask for uploading file that needs to be scanned, it returns the path to the file
if(re.search(r'\.', FILE)):
    if(re.search(r'/\.',FILE)):
        print("File starting with '.' has been ignored!")
        exit()
else:
    print("Extensionless File has been ignored!")
    exit()
if FILE:
    num_lines = sum(1 for line in open(str(FILE))) # Opens the file and adds 1 for each line
    print("Total # of lines:",num_lines) # Prints the total number of lines
    fileextension=FILE.split('.')[-1]
    num_slcomments=0
    num_commentsinblocks=0
    num_blccomments=0
    num_TODO=0
    num_mmcomments=0
    a=[]
    i=0 
    if((fileextension=='java') or (fileextension=='js')):
        flag1=1 # flag to signify that /* is found
        flag2=0 # flag to signify that */ is found
        flag3=1 # flag to signify that // was present ( to be used to check if // comment leads to a block comment ; if followed by another // or /* */ )
        for line in open(str(FILE)):
            if (not ((re.search('//',line) or re.search('/\*',line)))  and (flag1!=0)):
                a.append('No')
                i=i+1
                continue
            if(re.search('//',line)):
                a.append('Yes') 
                num_slcomments=num_slcomments+1
                flag3=0 #TODO needs to be tested
            if(re.search('\*/',line)):
                #a.append("Yes")
                flag2=1
                flag1=0   
            if(re.search('\\*',line)):
                if(flag2!=1):
                    a.append("Yes")
                    flag1=0
            else:
                if((flag1==0 and flag2==0) and (not re.search('\\*',line))):
                    a.append("Yes")
            
            if(i!=0):
                if((flag1==0) or (flag3==0) or (a[i-1]=='Yes' and a[i]=="Yes")):
                    num_commentsinblocks=num_commentsinblocks+1
                    if(flag3==0): #needs to be tested
                        flag3=1
                    if(i!=1 and a[i-1-1]=='No'):
                        num_blccomments=num_blccomments+1
            if('TODO' in line): 
                num_TODO=num_TODO+1
            i=i+1
        print("Total # of single line comments:",num_slcomments) # Prints the total number of lines
        print("Total # of comment lines within block comments:",num_commentsinblocks) # Prints the total number of lines
        print("Total # of block line comments:",num_blccomments)
        print("Total # of TODO’s:",num_TODO)
    if(fileextension=='py'):
        for line in open(str(FILE)):
            if not re.search('#',line):
                a.append('No')
                i=i+1
                continue
            cc=0
            flag=1
            for c in line:
                if c in ['"',"'"]:
                    cc=cc+1
                if((c=='#') and (cc%2!=0)):
                    flag=0
                if((c=='#') and (cc%2==0)):
                    flag=1
            if(flag==0):
                a.append('No')
                i=i+1
                continue
            a.append('Yes') 
            num_slcomments=num_slcomments+1   
            if('TODO' in line): 
                num_TODO=num_TODO+1
            if(i!=0 and a[i-1]=='Yes' and a[i]=="Yes"):
                num_commentsinblocks=num_commentsinblocks+1
                if(i!=1 and a[i-1-1]=='No'):
                    num_blccomments=num_blccomments+1
            i=i+1
        print("Total # of single line comments:",num_slcomments) # Prints the total number of lines
        print("Total # of comment lines within block comments:",num_commentsinblocks+num_blccomments) # Prints the total number of lines
        print("Total # of block line comments:",num_blccomments)
        print("Total # of TODO’s:",num_TODO)
else:
    print('Cancelled')

