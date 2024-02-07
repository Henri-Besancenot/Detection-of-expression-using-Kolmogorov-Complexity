# The purpose of this file is to compress images.
# We should be able to :
#   - compress together different images.
#   - get the images sizes.
#   - get few indicators such as NCD
# To train the model we're going to use FER-2013 Dataset

import zipfile
import os
import shutil

def zip_files(file1,zip_filename,file2=None):
    #programm that zip two files in a same zip folder
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(file1)
        if file2:
            zipf.write(file2)


def get_file_size(file_path):
    #returns the size of a given file
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        return -1  # File doesn't exist

def create_empty_zip(zip_filename):
    #create an empty zip folder
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        pass

def delete_file(file_path):
    #program that deletes a given file
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_path}'.")

def copy_file(source_file, destination_file):
    try:
        shutil.copy2(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
    except PermissionError:
        print(f"Permission denied to copy file '{source_file}'.")

def Z(file1,file2 = None):
    create_empty_zip('temp') #creates a temporary zip file
    zip_files(file1,'temp',file2,) #compresses given files into this folder
    Z = get_file_size('temp') # gives the size of the zipped folder
    delete_file('temp') #suppresses the zip file
    return Z

def Zopti(file1,file2):
    copy_file(file1,'temp')
    with zipfile.ZipFile('temp', 'w') as zipf:
        zipf.write(file2)
    Z = get_file_size('temp')
    delete_file('temp')
    return Z


def NCD(file1,file2):
    Z1 = Z(file1)
    Z2 = Z(file2)
    Zmin = min(Z1,Z2)
    Zmax = max(Z1,Z2)
    Z12 = Z(file1,file2)
    return(Z12-Zmin)/Zmax

def NCDopti(file1,file2):
    Z1 = get_file_size(file1)
    Z2 = Z(file2)
    Zmin = min(Z1,Z2)
    Zmax = max(Z1,Z2)



##
