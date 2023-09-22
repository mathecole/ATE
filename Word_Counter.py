# Mathéo Vinh Bui
# Tp1 Word Counter


print("Ce programme compte le nombre de mots présent dans une phrase de votre choix\n")
# introduit l'utilisateur
phrase = input("Veuillez écrire la phrase de que vous souhaitez.\n")
# détenir la phrase


def word_counter(phrase):
    count = len(phrase.split())
    # compte le nombre de phrases dans la variable
    return count


print("votre phrase contient %d mots" % word_counter(phrase))
# envoi le nombre de phrases à l'utilisateur
