def containsDuplicate_1(nums):
    return False if len(set(nums)) == len(nums)   else True

def containsDuplicate_2(nums):
    return len(nums) > len(set(nums))
