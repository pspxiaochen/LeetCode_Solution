def numberOfBoomerangs(points):
    count = 0
    for i in points:
        diss = {}
        for j in points:
            if i == j:
                continue
            else:
                dis = (i[0] - j[0]) * (i[0] - j[0]) + (i[1]-j[1]) * (i[1] - j[1])
                if dis not in diss:
                    diss[dis] = 1
                else:
                    diss[dis] += 1
        for i in diss:
            if diss[i] > 1:
                count += diss[i] * (diss[i] -1)
    return count

