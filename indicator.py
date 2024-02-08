import data_manipulation as dm

def Z(list_images:list[str]|str)->int:
    if type(list_images) is str : list_images = [list_images]
    data_images = dm.images_byte_concat(list_images)
    return len(dm.compress_bytes(data_images))

def NCD(list_image_1, list_image_2):
    if type(list_image_1) is str : list_image_1 = [list_image_1]
    if type(list_image_2) is str : list_image_2 = [list_image_2]
    
    Z_1 = Z(list_image_1)
    Z_2 = Z(list_image_2)
    Z_12 = min(Z(list_image_1 + list_image_2), Z(list_image_2 + list_image_1))
    return (Z_12 - min(Z_1, Z_2))/max(Z_1,Z_2)

