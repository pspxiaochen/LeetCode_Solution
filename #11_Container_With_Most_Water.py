def maxArea(height):
    left = 0
    right = len(height) - 1
    res = 0
    while left < right:
        temp = (right - left) * min(height[left],height[right])
        if temp > res:
            res = temp
        if height[left] >= height[right]:
            right -= 1
        else:
            left += 1
    return res
