def distributeCandies(candies):
    if len(set(candies)) < len(candies) / 2:
        return len(set(candies))
    else:
        return len(candies) / 2
