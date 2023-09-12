print("Ce programme compte le nombre de mots présent dans une phrase de votre choix\n")
phrase = input("Veuillez écrire la phrase de que vous souhaitez.\n")

def word_counter(phrase):
    count = len(phrase .split())
    return count
print("votre phrase contient %d mots"%word_counter(phrase))