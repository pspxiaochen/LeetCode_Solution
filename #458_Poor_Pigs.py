def poorPigs(buckets,minutesToDie,minutesToTest):
    if buckets == 1:
        return 0
    count = minutesToTest // minutesToDie + 1 ##如果没死 则最后一桶水有毒
    for i in range(1,buckets):
        if count ** i >= buckets:
            return i

