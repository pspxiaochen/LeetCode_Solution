def findRadius(houses,heaters):
    houses = sorted(houses)
    heaters = sorted(heaters)
    result = 0
    j = 0
    temp = 0
    for i in range(len(houses)):
        while j < len(heaters)  and heaters[j] < houses[i]:
            j += 1
        if j == len(heaters):
            temp = houses[i] - heaters[j-1]
        elif j == 0:
            temp = heaters[j] - houses[i]
        elif heaters[j] == houses[i]:
            temp = 0
        else:
            temp = min(houses[i] - heaters[j-1],heaters[j] - houses[i])
        result = max(result,temp)
    return result

