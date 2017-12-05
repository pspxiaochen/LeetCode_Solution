def intersect(nums1,nums2):
    out = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            out.append((nums1[i]))
            nums2.remove(nums1[i])
    return out