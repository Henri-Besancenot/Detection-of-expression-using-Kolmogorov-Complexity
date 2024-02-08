import indicatorv2 as ind
import os
import statistics

def is_emotion(file, emotion):
    dir_emotion_path = os.path.join("./train", emotion)
    list_image_emotion = [os.path.join(dir_emotion_path, fname) for fname in os.listdir(dir_emotion_path)] 
    return ind.NCD(file, list_image_emotion)

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

    dir_emotion_path = os.path.join("./train", emotion_comp)
    list_image_emotion = [os.path.join(dir_emotion_path, fname) for fname in os.listdir(dir_emotion_path)] 
    # Traitement des fichiers présent dans, par exemple : ./test/angry/
    for file in os.listdir(os.path.join("./test", emotion_input)):
        file_name = os.path.join("./test", emotion_input, file)

        # Calcul du NCD en comparaison avec le zip de l'emotion 2
        # list_NCD.append(is_emotion(file_name, emotion_comp))
        list_NCD.append(ind.NCD(file_name, list_image_emotion))

        # Affichage de l'avance
        number_treated += 1
        print("Pourcentage fait : ", round(100*number_treated/number_of_file,2), "%")    

    # AFFICHAGE DES STATS
    stat = statistics.mean(list_NCD), statistics.median(list_NCD),statistics.pstdev(list_NCD), min(list_NCD),max(list_NCD)
    print(f"========== IMAGE {emotion_input.upper()} IS {emotion_comp.upper()}==========")
    print("Average NCD :\t\t", stat[0])
    print("Mediane value of NCD :\t", stat[1])
    print("Standard deviation of NCD:\t", stat[2])
    print("Lower value of NDC :\t", stat[3])
    print("Upper value of NDC :\t", stat[4])

    return stat

if __name__ == "__main__":
    f("angry","disgust")