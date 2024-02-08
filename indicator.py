import file_manipulation as fm

def Z(list_files:list[str])-> int:
    """
    :param list_files:
    :return: The size of the Zip version of the file containing all the ones present in list_files
    """
    fm.zip_two_files(list_files,"temp.zip")
    Z = fm.get_file_size("temp.zip")
    fm.delete_file("temp.zip")
    return Z


def Z_opti(file1,file2):
    fm.copy_file(file1,'temp.zip')
    with fm.zipfile.ZipFile('temp.zip', 'a') as zipf:
        zipf.write(file2)
    Z = fm.get_file_size('temp.zip')
    fm.delete_file('temp.zip')
    return Z


def NCD(file1,file2):
    Z1 = Z(file1)
    Z2 = Z(file2)
    Zmin = min(Z1,Z2)
    Zmax = max(Z1,Z2)
    Z12 = Z([file1,file2])
    return (Z12-Zmin)/Zmax


def NCD_G(list_file1, list_file2):
    Z1 = Z(list_file1)
    Z2 = Z(list_file2)
    Z12 = Z(list_file1+list_file2)
    return (Z12 - min(Z1, Z2))/max(Z1,Z2)


def NCD_opti(file1,file2):
    Z1 = fm.get_file_size(file1)
    Z2 = Z(file2)
    Zmin = min(Z1,Z2)
    Zmax = max(Z1,Z2)
    Z12 = Z_opti(file1,file2)
    return (Z12-Zmin)/Zmax