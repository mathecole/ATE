#codé avec la pate à modeler
c1 = 3
c2 = 4
c3 = 2
c4 = 6
c5 = 8
c6 = 7
c7 = 1
c8 = 5
c9= 0
case0 = 0
if c1 == 0:
  case0 = 1
if c2 == 0:
  case0 =2
if c3 == 0:
  case0 =3
if c4 == 0:
  case0 =4
if c5 == 0:
  case0 =5
if c6 == 0:
  case0 =6
if c7 == 0:
  case0 =7
if c8 == 0:
  case0 =8
if c9 == 0:
  case0 =9
print("case0=%s"%case0)

print("Vous pouvez uniquement choisir les cases à coté de 0")

def jeu(case0, c1, c2, c3, c4, c5, c6, c7, c8, c9):
  # je sais pas quoi faire man
  right = [1, 2, 4, 5, 7, 8]
  left = [2, 3, 5, 6, 8, 9]
  down = [1, 2, 3, 4, 5, 6]
  up = [4, 5, 6, 7, 8, 9]
  while True:
    try:
      print("%s %s %s\n%s %s %s\n%s %s %s"%(c1, c2, c3, c4, c5, c6, c7, c8, c9))
      case = input("\nchoisissez la case que vous souhaitez choisir\n")
      if case == "up":
        if case0 in up:
          fuckoff = case0
          case0 = case0 - 3
        else:
          crash = int(bin1)
      if case == "down":
        if case0 in down:
          fuckoff = case0
          case0 = case0 + 3
        else:
          crash = int(bin1)
      if case == "left":
        if case0 in left:
          fuckoff = case0
          case0 = case0 - 1
        else:
          crash = int(bin1)
      if case == "right":
        if case0 in right:
          fuckoff = case0
          case0 = case0 + 1
        else:
          crash = int(bin1)
      if case0 == 1:
        case0 = 1
        if fuckoff == 1:
          c1 = c1
        if fuckoff == 2:
          c2 = c1
        if fuckoff == 3:
          c3 = c1
        if fuckoff == 4:
          c4 = c1
        if fuckoff == 5:
          c5 = c1
        if fuckoff == 6:
          c6 = c1
        if fuckoff == 7:
          c7 = c1
        if fuckoff == 8:
          c8 = c1
        if fuckoff == 9:
          c9 = c1
        c1 = 0
      if case0 == 2:

        case0 = 2
        if fuckoff == 1:
          c1 = c2
        if fuckoff == 2:
          c2 = c2
        if fuckoff == 3:
          c3 = c2
        if fuckoff == 4:
          c4 = c2
        if fuckoff == 5:
          c5 = c2
        if fuckoff == 6:
          c6 = c2
        if fuckoff == 7:
          c7 = c2
        if fuckoff == 8:
          c8 = c2
        if fuckoff == 9:
          c9 = c2
        c2 = 0
      if case0 == 3:

        case0 = 3
        if fuckoff == 1:
          c1 = c3
        if fuckoff == 2:
          c2 = c3
        if fuckoff == 3:
          c3 = c3
        if fuckoff == 4:
          c4 = c3
        if fuckoff == 5:
          c5 = c3
        if fuckoff == 6:
          c6 = c3
        if fuckoff == 7:
          c7 = c3
        if fuckoff == 8:
          c8 = c3
        if fuckoff == 9:
          c9 = c3
        c3 = 0
      if case0 == 4:

        case0 = 4
        if fuckoff == 1:
          c1 = c4
        if fuckoff == 2:
          c2 = c4
        if fuckoff == 3:
          c3 = c4
        if fuckoff == 4:
          c4 = c4
        if fuckoff == 5:
          c5 = c4
        if fuckoff == 6:
          c6 = c4
        if fuckoff == 7:
          c7 = c4
        if fuckoff == 8:
          c8 = c4
        if fuckoff == 9:
          c9 = c4
        c4 = 0
      if case0 == 5:

        case0 = 5
        if fuckoff == 1:
          c1 = c5
        if fuckoff == 2:
          c2 = c5
        if fuckoff == 3:
          c3 = c5
        if fuckoff == 4:
          c4 = c5
        if fuckoff == 5:
          c5 = c5
        if fuckoff == 6:
          c6 = c5
        if fuckoff == 7:
          c7 = c5
        if fuckoff == 8:
          c8 = c5
        if fuckoff == 9:
          c9 = c5
        c5 = 0

      if case0 == 6:

        case0 = 6
        if fuckoff == 1:
          c1 = c6
        if fuckoff == 2:
          c2 = c6
        if fuckoff == 3:
          c3 = c6
        if fuckoff == 4:
          c4 = c6
        if fuckoff == 5:
          c5 = c6
        if fuckoff == 6:
          c6 = c6
        if fuckoff == 7:
          c7 = c6
        if fuckoff == 8:
          c8 = c6
        if fuckoff == 9:
          c9 = c6
        c6 = 0

      if case0 == 7:

        case0 = 7
        if fuckoff == 1:
          c1 = c7
        if fuckoff == 2:
          c2 = c7
        if fuckoff == 3:
          c3 = c7
        if fuckoff == 4:
          c4 = c7
        if fuckoff == 5:
          c5 = c7
        if fuckoff == 6:
          c6 = c7
        if fuckoff == 7:
          c7 = c7
        if fuckoff == 8:
          c8 = c7
        if fuckoff == 9:
          c9 = c7
        c7 = 0

      if case0 == 8:
        case0=8
        if fuckoff == 1:
          c1 = c8
        if fuckoff == 2:
          c2 = c8
        if fuckoff == 3:
          c3 = c8
        if fuckoff == 4:
          c4 = c8
        if fuckoff == 5:
          c5 = c8
        if fuckoff == 6:
          c6 = c8
        if fuckoff == 7:
          c7 = c8
        if fuckoff == 8:
          c8 = c8
        if fuckoff == 9:
          c9 = c8
        c8 = 0

      if case0 == 9:
        case0= 9
        if fuckoff == 1:
          c1 = c9
        if fuckoff == 2:
          c2 = c9
        if fuckoff == 3:
          c3 = c9
        if fuckoff == 4:
          c4 = c9
        if fuckoff == 5:
          c5 = c9
        if fuckoff == 6:
          c6 = c9
        if fuckoff == 7:
          c7 = c9
        if fuckoff == 8:
          c8 = c9
        if fuckoff == 9:
          c9 = c9
        c9 = 0

    except:
      print("\nERREUR, réessayez\n")
jeu(case0, c1, c2, c3, c4, c5, c6, c7, c8, c9)
print("test")