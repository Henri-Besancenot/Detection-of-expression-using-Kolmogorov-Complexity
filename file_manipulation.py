# The purpose of this file is to compress images.
# We should be able to :
#   - compress together different images.
#   - get the images sizes.
#   - delete or change directory of image
# To train the model we're going to use FER-2013 Dataset

import zipfile
import zlib
import os
import shutil

def zip_two_files(file1:str,zip_filename:str,file2=None)->None:
    # programm that zip two files in a same zip folder
    # Not that zip_filename shoud end with .zip
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(file1, compress_type=zipfile.ZIP_DEFLATED)
        if file2:
            zipf.write(file2, compress_type=zipfile.ZIP_DEFLATED)


def zip_files(zip_filename:str, file_list:list[str]|str = [])->None:
    """
    :param file_list: List of all the files (paths) you want to zip.
    :param zip_filename: Name of the receiving file. Should end with .zip to work well.
    Create a zip file, named zip_filename, of all the file contained in file_list.  
    """
    if type(file_list) is str: file_list = [file_list]
    zipf = zipfile.ZipFile(zip_filename, 'w')
    for file in file_list:
        zipf.write(file, compress_type=zipfile.ZIP_DEFLATED)


def get_file_size(file_path:str)->int:
    """
    :param file_path: Le chemin d'un fichier
    :return: La taille du fichier a l'emplacement de file_path
    """
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    else:
        return -1  # File doesn't exist


def get_folder_size(folder_path:str)->int:
    """
    :param folder_path: Le chemin d'un fichier
    :return: La taille du dossier a l'emplacement de folder_path
    """
    if not os.path.exists(folder_path):
        return -1
    
    size = 0
    for f in os.listdir(folder_path):
        f_name = os.path.join(folder_path, f)
        if os.path.isdir(f_name): size += get_folder_size(f_name)
        else: size += get_file_size(f_name)
    return size


def delete_file(file_path):
    #program that deletes a given file
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_path}'.")


def empty_folder(folder_path):
    for file in os.listdir(folder_path):
        delete_file(os.path.join(folder_path, file))


def copy_file(source_file, destination_file):
    try:
        shutil.copy2(source_file, destination_file)
        #print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Source file '{source_file}' not found.")
    except PermissionError:
        print(f"Permission denied to copy file '{source_file}'.")





if __name__ == '__main__':
    choice = int(input("Choix :\t"))

    # Compression des fichiers d'entrainement
    if choice == 1:
        empty_folder("./compressed")
        print("Emptied folder")
        for emotion in os.listdir("./train"):
            f_name = os.path.join("./train", emotion)
            # Calcul le positionnement des fichiers dans chaque sous dossier
            relative_path_list =  [os.path.join(f_name, file) for file in os.listdir(f_name)]
            zip_files(os.path.join("./compressed", emotion+".zip"), relative_path_list)

    # Comparaison taille des fichiers compressés
    elif choice == 2:
        print("="*10, "NOT COMPRESSED", "="*10)
        for fold in os.listdir("./train"): 
            folder_size = get_folder_size(os.path.join('./train', fold))
            print(f"{fold} -> {folder_size}")
        Z1 = get_folder_size('./train')
        print(f"TOTAL = {Z1}")

        print("\n")

        print("="*10, "COMPRESSED", "="*10)
        for file in os.listdir("./compressed"): 
            folder_size = get_file_size(os.path.join('./compressed', file))
            print(f"{file} -> {folder_size}")
        Z2 = get_folder_size('./compressed')
        print(f"TOTAL = {Z2}")
        print("\n")

        print(f"\nGAIN TOTAL = {Z1-Z2}")

    # TEST
    if choice == -1:
        ...