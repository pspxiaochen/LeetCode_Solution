def maxProfit_1(prices):
    if not prices:
        return 0
    allMaxPrice = 0
    for i in range(1,len(prices)):
        maxPrice = prices[i] - prices[i-1]
        maxPrice = max(0,maxPrice)
        allMaxPrice += max(0,maxPrice)
    return allMaxPrice

def maxProfit_2(prices):
    if not prices:
        return 0
    startIndex = 0
    allPrice = 0
    i = 1
    while(i < len(prices)):
        if (prices[i] < prices[i-1]):
            allPrice += prices[i-1] - prices[startIndex]
            startIndex = i
        i += 1
    if prices[i-1] > prices[startIndex]:
        allPrice += prices[i-1] - prices[startIndex]
    return allPrice
