
import os

# Get the list of all files and directories
path = r"C:\Users\Raghu\Desktop\Udemy Python Practise\pdf_extractor"
dir_list = os.listdir(path)

# prints all files
print(f"Files and directories in {path}  : ")
 

# print(dir_list)

def file_extract(path, file_type):
    for x in dir_list:                  # dir_list or os.listdir(path)
        if x.endswith(file_type):
            # Prints any type of file present in My Folder
            return x

res = file_extract(path, '.py')
print(res)






