import random
print("Jeu de dnd")
vie = 20
defaite = 0
combats = 0
force = 0
adversaire = 0
defaite = 0
victoire = 0
def interaction(vie, force, combats, adversaire, defaite, victoire):
    action=0
    print(" Adversaire: %s\n Force de l'adversaire: %s\n Niveau de vie: %s\n Combats %s: victoires %s et défaites %s"%(adversaire, force, vie, combats, victoire, defaite))
    while(action != 1 or action != 2 or action != 3 or action != 4):
        action = input("Que voulez-vous faire ?\n1- Combattre l'adversaire\n2- Fuir\n3- Règles\n4- Quitter\n")
        if (action != 1 or action != 2 or action != 3 or action != 4):
            print("Tu ne peux pas répondre autre que 1, 2, 3 ou 4, réessaye")
        if action == 1:
            print("roulement de dés...")
            attaque = random.randint(1,6)
            if attaque < force:
                vie -= force
                print("vous avez perdu %s points de vie, vous avez maintenant %s points de vie"%(force, vie))
            elif attaque > force:
                vie += force
                print("vous avez gagnez %s points de vie, vous avez maintenant %s points de vie"%(force,vie))
        if action == 2:
            print("Vous êtes un vrai lâche, vous avez fuit. Pour votre manque de bravour, vous avez reçu une défaite.")
            print("Vous possèdez maintenant %s défaites"%defaite)
        if action == 3:
            print("Voici les règles du jeu.\n Vous commencez la partie avec 20 points de vies, vôtre tâche sera d'accumuler")
            print("le plus de victoires possibles, pour vaincre ces adversaires vous allez devoir")
while(vie>0):
    adversaire += 1
    force = random.randint(1, 5)
    interaction(vie, force, combats, adversaire, defaite, victoire)
    combats += 1