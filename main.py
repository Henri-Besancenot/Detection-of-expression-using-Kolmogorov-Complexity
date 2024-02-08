# Given an image, we should be able to tell if the face express happiness, sadness, angryness etc...

import indicator as ind
import NCD_calculator as NCD
import statistics

def get_NCD_list(matrice, emotion_input, emotion_comp):
    return matrice[emotion_input][emotion_comp]

def get_stat(matrice, emotion_input, emotion_comp):
    list_NCD = get_NCD_list(matrice, emotion_input, emotion_comp)
    stat = statistics.mean(list_NCD),statistics.median(list_NCD),statistics.pstdev(list_NCD), max(list_NCD), min(list_NCD)
    return stat

def get_ordre_by_stat(matrice, emotion,stat:int):
    """
    :param stat: Entre 0 et 4. Correspond à ce qui est retourné par get_stat
    """
    NCD_dict = matrice[emotion]
    stats = []
    for emotion_comp in NCD_dict:
        stats.append((emotion_comp, get_stat(matrice,emotion, emotion_comp)))
    stats.sort(key=lambda a: a[1][stat], reverse = True)
    return [(s[0], s[1][stat]) for s in stats]

def print_tuple_list(tuple_list):
    for elem in tuple_list:
        print(f"{elem[0]} -> {elem[1]}")




if __name__ == "__main__":
    matrice = NCD.load("matrice_NCD")

    print_tuple_list(get_ordre_by_stat(matrice, "", 0))
