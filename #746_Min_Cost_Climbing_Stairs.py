def minCostClimbingStairs(cost):
    dp0 = dp1 = dp2 = 0
    for i in range(2,len(cost)+1):
        dp2 = min(dp0 + cost[i-2],dp1 + cost[i-1])
        dp0 = dp1
        dp1 = dp2
    return dp2


