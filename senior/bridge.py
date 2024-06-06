simultaneous = 0
bridge_weight = 0
weight = int(input())
n = int(input())
dunno = True
Cars = []
for i in range(n):
    if len(Cars) == 4:
        bridge_weight -= Cars[0]
        Cars.pop(0)
    car_weight = int(input())

    Cars.append(car_weight)
    simultaneous +=1
    bridge_weight += car_weight
    if bridge_weight > weight and i == 0:
        numb_cars = i
        dunno = False
    elif bridge_weight > weight and dunno == True:
        numb_cars = i+1
        dunno = False

if dunno:
    print(n)
else:
    print(numb_cars)