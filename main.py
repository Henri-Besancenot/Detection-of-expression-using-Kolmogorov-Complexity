# Given an image, we should be able to tell if the face express happiness, sadness, angryness etc...

import indicator as ind
import zipfile
import os
import shutil
import numpy
import statistics


def is_emotion(file:str,emotion:str)->float:
    """
    :param file: Path to the image we want to test
    :param emotion: Emotion we want to look for
    :return: The normalized compression distance of the corresponding train folder and the image 
    
    path_to_emo = os.path.join("./train", emotion)
    emotion_train = [os.path.join(path_to_emo, f) for f in os.listdir(path_to_emo)]
    return cpr.NCD_G([file],emotion_train)
    """
    return ind.NCD_opti(f"./compressed/{emotion}.zip", file)


def f(emotion_input, emotion_comp):
    """
    :param emotion_input: Emotion de l'image qu'on test
    :param emotion_comp: Emotion que l'on compare
    :return: Moyenne, medianne, minimum et maximum des NCDs calcules
    """

    list_NCD = []
    print("Start")

    # Compteur pour pourcentage
    number_of_file = len(os.listdir(os.path.join("./test", emotion_input)))
    number_treated = 0 

    # Traitement des fichiers présent dans, par exemple : ./test/angry/
    for file in os.listdir(os.path.join("./test", emotion_input)):
        file_name = os.path.join("./test", emotion_input, file)

        # Calcul du NCD en comparaison avec le zip de l'emotion 2
        # Qui peut etre par exemple : ./compressed/disgust.zip
        list_NCD.append(is_emotion(file_name, emotion_comp))

        # Affichage de l'avance
        number_treated += 1
        print("Pourcentage fait : ", round(100*number_treated/number_of_file,2), "%")    

    # AFFICHAGE DES STATS
    stat = statistics.mean(list_NCD), statistics.median(list_NCD), min(list_NCD),max(list_NCD)
    print(f"========== IMAGE {emotion_input.upper()} IS {emotion_comp.upper()}==========")
    print("Average NCD :\t\t", stat[0])
    print("Mediane value of NCD :\t", stat[1])
    print("Lower value of NDCD :\t", stat[2])
    print("Upper value of NDCD :\t", stat[3])

    return stat

if __name__ == "__main__":

    f("disgust","disgut")

    # print(is_emotion("./test/happy/PrivateTest_4871052.jpg", "angry"))
    # print(is_emotion("./test/angry/PrivateTest_1290484.jpg", "angry"))
    


    # ind.NCDopti("./compressed/fear.zip","./test/fear/PrivateTest_134207.jpg")