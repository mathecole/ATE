N = int(input())
pepper = []
for i in range(N):
    specificpepper = input()
    if specificpepper == "Poblano":
        pepper.append(1500)
    elif specificpepper == "Mirasol":
        pepper.append(6000)
    elif specificpepper == "Serrano":
        pepper.append(15500)
    elif specificpepper == "Cayenne":
        pepper.append(40000)
    elif specificpepper == "Thai":
        pepper.append(75000)
    elif specificpepper == "Habanero":
        pepper.append(125000)
    else:
        exit()
print(sum(pepper))