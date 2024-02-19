N = int(input())
Players = []
Points = []
Fouls = []
GoodPlayers = 0
for i in range(N):
    Points = int(input())*5
    Fouls = int(input())*3
    Star = Points - Fouls
    if Star >40:
        GoodPlayers+=1
if GoodPlayers == N:
    print(str(GoodPlayers) + "+")
else:
    print(GoodPlayers)