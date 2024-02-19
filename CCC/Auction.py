N = int(input())
if N<=1 and N >=100:
    exit()
Name = []
Bid = []
for i in range(N):
    Name.append(input())
    Bid.append(int(input()))
position = Bid.index(max(Bid))
winner = Name[position]
print(winner)

