def maxProfit_1(prices):
    maxPrice = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] - prices[i] > maxPrice:
                maxPrice = prices[j] - prices[i]
    return maxPrice

def maxProfit_2(prices):
    maxPrice = 0
    allMaxPrice = 0
    for i in range(1,len(prices)):
        maxPrice += prices[i] - prices[i-1]
        maxPrice = max(0,maxPrice)
        allMaxPrice = max(allMaxPrice,maxPrice)
    return allMaxPrice

def maxProfit_3(prices):
    minPrice = 9999999999
    maxPro = 0
    for i in range(len(prices)):
        minPrice = min(minPrice,prices[i])
        maxPro = max(maxPro,prices[i] - minPrice)
    return maxPro
