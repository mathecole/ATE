import random
essais = 0
nombre_mystere = random.randint(0,1000)
guess = []
print(nombre_mystere)
nombre_guess = int(input("Essaye de deviner mon nombre mystère, il se situe entre 0 et 1000 "))
while (nombre_mystere != nombre_guess):
  essais += 1
  guess.append(nombre_guess)
  nombre_guess = int(input("non c'est pas %s, btw ça fait %s fois que t'essaye"%(nombre_guess, essais)))
  
  if nombre_guess in guess:
    print("ta déja essayer %s"%nombre_guess)

print("Tu l'as eu c'était %s."%nombre_mystere)