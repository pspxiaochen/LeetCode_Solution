class NumArray(object):
    def __init__(self,nums):
        self.array = len(nums) * [0]
        for i in range(len(nums)-1):
            self.array[i] = sum(nums[:i+1])

    def sumRange(self,i,j):
        if i == 0:
            return self.array[j]
        else:
            return self.array[j] - self.array[i-1]
