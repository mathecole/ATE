    import random
def diceroll():
    dice = []
    dice.append(random.randint(4, 6))
    dice.append(random.randint(4, 6))
    dice.append(random.randint(4, 6))
    dice.append(random.randint(4, 6))
    dice.remove(dice[0])
    return sum(dice)

class NPC:
    def __init__(self,force,agilite,constitution,intelligence,sagesse,charisme):
        self.force = diceroll()
        self.agilite = diceroll()
        self.constitution = diceroll()
        self.intelligence = diceroll()
        self.sagesse = diceroll()
        self.charisme = diceroll()
        self.armure = random.randint(1, 12)
        self.nom = None
        self.race = None
        self.vie = random.randint(1, 20)
        self.profession = None
    def afficher_caracteristiques(self):
        print("Force : %s"%self.force)
        print("Agilite : %s"%self.agilite)
        print("constitution : %s" % self.constitution)
        print("Intelligence : %s" % self.intelligence)
        print("Sagesse : %s" % self.sagesse)
        print("Charisme : %s" % self.charisme)
        print("Armure : %s" % self.armure)
        print("Nom : %s" % self.nom)
        print("Race : %s" % self.race)
        print("Vie : %s" % self.vie)
        print("Profession : %s" % self.profession)


class Dragon(NPC):

  def __init__(self):
    super(NPC).__init__()
    self.race = "Dragon"
    self.espece = "Lézard"
    self.profession = "Énnemi"


class Hero(NPC):
  def __init__(self):
    super(NPC).__init__()
    self.race = "Hyrulien"
    self.espece = "Humain"
    self.profession = "Héro"
    self.nom = "Bertrand"