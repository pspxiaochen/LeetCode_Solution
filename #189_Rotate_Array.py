def rotate_1(nums,k):
    nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
a =[1,2,3,4,5,6,7]


def rotate_2(nums,k):
    k %= len(nums)
    reverse(nums,0,len(nums)-1)
    reverse(nums,0,k-1)
    reverse(nums,k,len(nums)-1)


def reverse(nums,start,end):
    while(start<end):
        temp=nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1