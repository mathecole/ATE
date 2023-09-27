import random
print("Jeu de dnd")
vie = 20
def interaction(vie, force, combats, adversaire, defaite, victoire):
    print("Adversaire: %s\n Force de l'adversaire: %s\n Niveau de vie\n Combat %s: %s victoires et %s défaites"%(adversaire, force, vie, combats, victoire, defaite))

while(vie>0):
    force = random.randint(1, 5)
