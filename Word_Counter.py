print("Ce programme compte le nombre de charactère présent dans le mot ou phrase de votre choix\n")
mot = input("Veuillez écrire le mot ou phrase de que vous souhaitez.\n")

def word_counter():
    count = len(mot)
    return count
print(word_counter())
print("votre mot ou phrase contient %d lettres"%word_counter())