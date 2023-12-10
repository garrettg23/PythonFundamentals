# Use os module in python, provides a way to interact with the operating system.
# This includes functions for file and directory manipulation

import os

# Basics
# If anything in the path has a space, you must use double backslashes.
def path_check(path):
    if os.path.exists(path): # Checks Path Exists
        print("That location exists.")
        if os.path.isfile(path):
            print("That is a file.")
        elif os.path.isdir(path):
            print("That is a directory!")
    else:
        print("That location does not exist.")

path = "C:\\Documents\\PythonOsTraining\\New Test.txt"

path_check(path)

# Using other functions / example 2
def is_file_exists(file_path):
    return os.path.exists(file_path)

def is_directory(path):
    return os.path.isdir(path)

def is_file(file_path):
    return os.path.isfile(file_path)

def list_files_in_directory(directory):
    if is_directory(directory):
        return os.listdir(directory)
    else:
        print(f"{directory} is not a valid directory.")

# Example usage,put in full path to file you and directory you want to check.
file_path = "C:\Documents\PythonOsTraining\sample.txt"
directory_path = "C:\Documents\PythonOsTraining"

# Check if a file exists
if is_file_exists(file_path):
    print(f"{file_path} exists.")
else:
    print(f"{file_path} does not exist.")

# Check if a path is a directory
if is_directory(directory_path):
    print(f"{directory_path} is a directory.")
else:
    print(f"{directory_path} is not a directory.")

# Check if a path is a file
if is_file(file_path):
    print(f"{file_path} is a file.")
else:
    print(f"{file_path} is not a file.")

# List files in a directory
files_in_directory = list_files_in_directory(directory_path)
if files_in_directory:
    print(f"Files in {directory_path}: {', '.join(files_in_directory)}")
