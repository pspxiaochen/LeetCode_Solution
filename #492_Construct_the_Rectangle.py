import math
def constructRectangle(area):
    temp = int(math.sqrt(area))
    if temp * temp == area:
        return [temp,temp]
    else:
        start = temp
        while start > 1:
            if area % start == 0:
                return [int(max(start,area / start)),int(min((start,area / start)))]
            else:
                start -= 1
    return [area,1]




