import random
jouer="o"

#Cette boucle while s'occupe de démarrer une partie
while(jouer == "o"):
  essais = 0
  nombre_mystere = random.randint(0,1000)
  guess = []
  nombre_guess = int(input("Essayez de deviner mon nombre mystère, il se situe entre 0 et 1000 "))

#Cette boucle analyse l'input de l'utilisateur
  while (nombre_mystere != nombre_guess):
    if(nombre_guess > nombre_mystere):
     print("le nombre est plus petit")

    elif(nombre_guess < nombre_mystere):
      print("le nombre est plus grand")

    essais +=1
    nombre_guess = int(input("non ce n'est pas %s, il fait %s fois que vous essayez"%(nombre_guess, essais)))
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