import random
essais = 0
nombre_mystere = random.randint(0,1000)

nombre_guess = input("Essaye de deviner mot nombre mystère, il se situe entre 0 et 100 ")
while (nombre_mystere != nombre_guess):
    essais += 1

    nombre_guess = input("non c'est pas %s, btw ça fait %s fois que t'essaye"%(nombre_guess, essais))
print("fuck you t'es une #### de #######, comment tu savais c'était %s?"%nombre_mystere)