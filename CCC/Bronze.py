N=int(input())
SortScore= []
EachScore = []
SameScore = []
for i in range(N):
    EachScore.append(int(input()))
for i in range(N):
    EachScore.pop(EachScore.index(EachScore(max)))
    N-=1
SortScore.append(EachScore[EachScore.index(EachScore(max))])
EachScore.pop(EachScore.index(EachScore(max)))
while True:
    SortScore.append(EachScore[EachScore.index(EachScore(max))])
    EachScore.pop(EachScore.index(EachScore(max)))
    if SortScore[-1] in EachScore:
        continue
    else:
        break
print(SortScore[-1] + len(SortScore))