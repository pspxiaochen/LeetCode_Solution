<<<<<<< HEAD
def removeElement(nums, val):
    if not nums:
        return 0
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

nums = [2,3,3,3,2,2,2,2,3,3]
val =3
print(removeElement(nums,val))


=======
def removeElement(nums, val):
    if not nums:
        return 0
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

nums = [2,3,3,3,2,2,2,2,3,3]
val =3
print(removeElement(nums,val))


>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
