import zlib
import os
import shutil



def image_to_bytes(image_path):
    return open(image_path, "rb").read()

def images_byte_concat(list_images):
    barray_images = bytearray()
    for image in list_images:
        barray_images.extend(image_to_bytes(image))
    return bytes(barray_images)

def compress_bytes(data):
    return zlib.compress(data, 9)

def get_data_size(data):
    return len(data)

def get_folder_size(folder_path:str)->int:
    """
    :param folder_path: Le chemin d'un fichier
    :return: La taille du dossier a l'emplacement de folder_path
    """
    size = 0
    for f in os.listdir(folder_path):
        f_name =os.path.join(folder_path,f)
        if os.path.isdir(f_name): size += get_folder_size(f_name)
        else: size += get_data_size(image_to_bytes(f_name))
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




if __name__ == "__main__":
    for emotion in os.listdir("./train"):
        print(f"========== {emotion.upper()} ==========")
        data = images_byte_concat([f"./train/{emotion}/{fname}" for fname in os.listdir(f"./train/{emotion}")])
        size = get_data_size(data)
        zip_size = get_data_size(compress_bytes(data))
        print("SIZE = ", size)
        print("ZIP SIZE = ", zip_size)
        print(f"SIZE GAINED = {size-zip_size}")