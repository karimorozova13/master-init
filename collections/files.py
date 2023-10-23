from pathlib import Path

file_path = Path('/home/dowmloads.py')
root_path = Path() #current folder
print(file_path.name)
print(file_path.parent)
print(file_path.suffix)

# Path.exists() Bollean, depends if exist
# Path.is_dir() True, if it's directory
# Path.is_file() True, if it's file
# Path.iterdir() iteration of all files and folders

folder_path = Path('/home/user/downloads')
for p in folder_path.iterdir(): #return all files and folders in the directory
    print("p") # Path obj as well