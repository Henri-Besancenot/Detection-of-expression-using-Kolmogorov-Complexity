import NCD_calculator as NCD
import os
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def emotion_guessed_for_real_emotion(real_emotion):
    guess = []
    for file in os.listdir(f"./test/{real_emotion}"):
        guess_list= NCD.guess_emotion(f"./test/{real_emotion}/{file}")
        guess.append(guess_list[0])

    compteur_guess = Counter(guess)

    guess = list(compteur_guess.keys())
    occurrences = list(compteur_guess.values())
    plt.bar(guess, occurrences)
    plt.xlabel("Guess")
    plt.ylabel("Number of appearance")
    plt.title(f"Guess for {real_emotion}")
    plt.show()

def average_classement_for_real_emotion(real_emotion):
    guess_list = []
    total = len(os.listdir(f"./test/{real_emotion}"))
    i=1
    for file in os.listdir(f"./test/{real_emotion}"):
        guess= NCD.guess_emotion(f"./test/{real_emotion}/{file}")
        guess_list.append(guess)
        print(f"{i}/{total} done.")
        i+=1

    # Calcul du positionnement moyen de chaque mot
    emotion_list = list(set([emotion for guess in guess_list for emotion in guess]))
    positionnements_moyens = [np.mean([guess.index(emotion) + 1 if emotion in guess else 0 for guess in guess_list]) for emotion in emotion_list]

    mots_positionnements_tries = sorted(zip(emotion_list, positionnements_moyens), key=lambda x: x[1])

    emotion_list = [mot[0] for mot in mots_positionnements_tries]
    positionnements_moyens = [mot[1] for mot in mots_positionnements_tries]

    # Création du graphique
    plt.bar(emotion_list, positionnements_moyens)
    plt.title(f"Ranking guess for {real_emotion}")
    plt.xlabel('Guess')
    plt.ylabel('Average position')
    plt.show()



if __name__ == "__main__":
    for emotion in os.listdir("./test"):
        average_classement_for_real_emotion(emotion)
