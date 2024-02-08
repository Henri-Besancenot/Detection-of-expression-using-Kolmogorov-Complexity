import indicatorv2 as ind
import os
import statistics
import pickle

# CREATION ET CALCUL DES DONNEES

def is_emotion(file, emotion):
    dir_emotion_path = os.path.join("./train", emotion)
    list_image_emotion = [os.path.join(dir_emotion_path, fname) for fname in os.listdir(dir_emotion_path)] 
    return ind.NCD(file, list_image_emotion)

def compute_NCD_Emotion_comp(emotion_input, emotion_comp, show = False):
    """
    :param emotion_input: Emotion de l'image qu'on test
    :param emotion_comp: Emotion que l'on compare
    :return: Moyenne, medianne, minimum et maximum des NCDs calcules
    """
    list_NCD = []
    #print("Start")

    # Compteur pour pourcentage
    # number_of_file = len(os.listdir(os.path.join("./test", emotion_input)))
    # number_treated = 0 

    dir_emotion_path = os.path.join("./train", emotion_comp)
    list_image_emotion = [os.path.join(dir_emotion_path, fname) for fname in os.listdir(dir_emotion_path)] 
    # Traitement des fichiers présent dans, par exemple : ./test/angry/
    for file in os.listdir(os.path.join("./test", emotion_input)):
        file_name = os.path.join("./test", emotion_input, file)

        # Calcul du NCD en comparrant l'image avec celles des list_images_emotion
        # list_NCD.append(is_emotion(file_name, emotion_comp))
        list_NCD.append(ind.NCD(file_name, list_image_emotion))

        # Affichage de l'avance
        # number_treated += 1
        # print("Pourcentage fait : ", round(100*number_treated/number_of_file,2), "%")    

    # AFFICHAGE DES STATS
    if show:
        stat = statistics.mean(list_NCD), statistics.median(list_NCD),statistics.pstdev(list_NCD), min(list_NCD),max(list_NCD)
        print(f"========== IMAGE {emotion_input.upper()} IS {emotion_comp.upper()}==========")
        print("Average NCD :\t\t\t", stat[0])
        print("Mediane value of NCD :\t\t", stat[1])
        print("Standard deviation of NCD:\t", stat[2])
        print("Lower value of NDC :\t\t", stat[3])
        print("Upper value of NDC :\t\t", stat[4])
        print("\n")

    return list_NCD

def get_matrice_NCD():
    emotion_list = os.listdir("./test")
    print("EMOTIONS ARE IN THIS ORDER : ", emotion_list)
    matrice_NCD = {emotion_input:{emotion_comp:[] for emotion_comp in emotion_list} for emotion_input in emotion_list}

    i=1
    total = len(emotion_list)**2
    for emotion_input in emotion_list:
        for emotion_comp in emotion_list:
            matrice_NCD[emotion_input] = (emotion_comp, compute_NCD_Emotion_comp(emotion_input, emotion_comp))
            print(f"{i}/{total} : {emotion_input} -> {emotion_comp} done.")
            i+=1
    return matrice_NCD



# STOCKAGE DES DONNEES

def stock(data,file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def load(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


if __name__ == "__main__":
    print("========== DEBUT DU CALCUL DE LA MATRICE ==========")
    matrice_NCD = get_matrice_NCD()
    print("========== FIN DU CALCUL DE LA MATRICE ==========")
    print("========== STOCKAGE DE LA MATRICE ==========")
    stock(matrice_NCD, "matrice_NCD")
    print("========== STOCKAGE TERMINE ==========")