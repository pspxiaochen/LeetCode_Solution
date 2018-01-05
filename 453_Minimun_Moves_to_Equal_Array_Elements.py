# 首先将sum定义为初始数组中所有数字的总和; minNum作为列表中的最小数字; n是列表的长度;
# 之后，移动m次，我们得到所有的数字为x，我们将得到以下等式
# sum + m （n-1）= x n
# 实际上， x = minNum + m
# 最后，通过计算会得到 sum - minNum * n = m
def minMove(nums):
    sumNum = sum(nums)
    minNum = min(nums)
    long = len(nums)
    return sumNum - minNum * long