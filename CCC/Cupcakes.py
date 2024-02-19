R = int(input())
S = int(input())
if R >= 0 and S >= 0:
    cupcakes = R*8 + S*3 - 28
    if cupcakes < 0:
        print(0)
    else:
        print(cupcakes)