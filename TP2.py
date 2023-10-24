import random
#Mathéo Vinh Bui
#2023-10-24


#Cette fonction s'ocuppe d'analyzer le code de l'utilisateur
def analyze(essais, nombre_mystere, guess, nombre_guess, jouer):
  while (nombre_mystere != nombre_guess):
    if(nombre_guess > nombre_mystere):
     print("le nombre est plus petit")

    elif(nombre_guess < nombre_mystere):
      print("le nombre est plus grand")

    essais +=1
    nombre_guess = int(input("non ce n'est pas %s, il fait %s fois que vous essayez"%(nombre_guess, essais)))
    #détecte les inputs réutilisés
    if nombre_guess in guess:
      print("vous déja essayez %s"%nombre_guess)
    guess.append(nombre_guess)

  print("Tu l'as eu c'était %s."%nombre_mystere)
#Cette boucle s'occupe de terminer/recommencer une partie
  while True:
    jouer = input("voulez vous rejouer? o/n")
    if jouer == "o":
      break
    elif jouer == "n":
      quit()
    else:
      print("Vous n'avez pas inséré o/n, réessasyez")
  guess.clear()
  return(jouer)




#Cette boucle while s'occupe de démarrer une partie
jouer = "o"
while(jouer == "o"):
  essais = 0
  nombre_mystere = random.randint(0,1000)
  guess = []
  nombre_guess = int(input("Essayez de deviner mon nombre mystère, il se situe entre 0 et 1000 "))
  guess.append(nombre_guess)
  jouer = analyze(essais, nombre_mystere, guess, nombre_guess, jouer)