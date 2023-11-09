import random
print("Jeu de dnd")
vie = 20
defaite = 0
combats = 0
force = 0
adversaire = 0
defaite = 0
victoire = 0
boss = 0
twocards = 0
bossmode = 0
def setup():
    global bossmode
    global twocards
    retry = 1
    while True:
        bossmode = input("Ce jeu possède manières de jouer, souhaitez vous\n 1- Jouer avec un Boss\n 2- Jouer sans boss")
        twocards = input("Vous pouvez aussi jouer avec un ou deux dés, les ennemis dans le mode à 2 dés sont plus forts.\n"
                         " 1-Jouer avec un dé\n 2- Jouer avec deux dés")
        if bossmode == "1":
            print("Boss activé")
        elif bossmode == "2":
            print("Boss déasctivé")
        else:
            print("Une erreur a eu lieu avec ton choix, reessaye")
            continue
        if twocards == "1":
            print("Un dé")
        elif twocards == "2":
            print("Deux dés")
        else:
            print("Une erreur a eu lieu avec ton choix,reessaye")
            continue
        break



def interaction(force, combats, adversaire):
    global defaite
    global boss
    global victoire
    global vie
    action = 0
    while True:
        print("\n Adversaire: %s\n Force de l'adversaire: %s\n Niveau de vie: %s\n Combats %s: victoires %s et défaites %s" % (adversaire, force, vie, combats, victoire, defaite))
        action = input(str("Que voulez-vous faire ?\n1- Combattre l'adversaire\n2- Fuir\n3- Règles\n4- Quitter\n"))
        if action == "1":
            print("roulement de dés...")
            attaque1 = random.randint(1,6)
            print("Votre premier d%s"%attaque1)
            if attaque1 + attaque2 <= force:
                vie -= force
                print("vous avez perdu %s points de vie, vous avez maintenant %s points de vie\n"%(force, vie))
                defaite += 1
            else:
                vie += force
                victoire += 1
                boss+=1
                print("vous avez gagnez %s points de vie, vous avez maintenant %s points de vie"%(force,vie))
            break
        elif action == "2":
            print("Vous êtes un vrai lâche, vous avez fuit. Pour votre manque de bravour, vous avez reçu une défaite.")
            defaite += 1
            print("Vous possèdez maintenant %s défaites"%defaite)
            break
        elif action == "3":
            print(" Voici les règles du jeu.\n Vous commencez la partie avec 20 points de vies, vôtre tâche sera d'accumuler")
            print(" le plus de victoires possibles, pour vaincre ces adversaires vous allez devoir rouler un dé si le chiffre")
            print(" est supérieur à la force de l'adversaire, vous gagnez une victoire et s'il est égal ou inférieur à celui-ci, vous perdez.")
            print(" Vous pouvez ausi vous enfuir si vous ne souhaitez pas faire face à l'énnemi, ceci vous donnera par contre un défaite.")
            print(" Après 3 Victoires, vous allez faire face à un boss qui possède beaucoup plus de force qu'un monstre banal.")
            print(" Vous pouvez aussi demander les règles, où ce message apparêtra. Lorsque votre niveau de vie atteint 0 la partie se termine.")
            break
        elif action == "4":
            print("Le code va s'arreter")
            quit()
        else:
            print("Tu ne peux pas repondre autre que 1, 2, 3 ou 4, reessaye")
setup()
while(vie>0):
    adversaire += 1
    if boss == 3 and bossmode == 1:
        print("\nVous faites face à un boss, cet ennemi est bien plus puissant")
        force = random.randint(6,11)
        boss = 0
    elif twocards == 2:
        force = random.randint(2, 8)
    else:

    interaction(force, combats, adversaire)
    combats +=1
print("\nVous avez perdu")