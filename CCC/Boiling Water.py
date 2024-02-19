B = int(input())
if B <=200 and B >= 80:
    P = 5*B-400
    if P < 100:
        print(P)
        print(1)
    if P > 100:
        print(P)
        print(-1)
    if P == 100:
        print(P)
        print(0)