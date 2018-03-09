def canPlaceFlowers(flowerbed,n):
    i = 0
    count = 0
    while i < len(flowerbed) and count < n:
        if flowerbed[i] == 0:
            next = 0 if i == len(flowerbed) - 1 else flowerbed[i+1]
            prev = 0 if i == 0 else flowerbed[i-1]
            if next == 0 and prev == 0:
                flowerbed[i] = 1
                count += 1
        i += 1
    return count == n
