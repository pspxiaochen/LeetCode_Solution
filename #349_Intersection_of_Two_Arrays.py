def intersection(nums1,nums2):
    if not nums1 or not nums2:
        return []
    nums1_ = set(nums1)
    nums2_ = set(nums2)
    nums1 = list(nums1_)
    nums2 = list(nums2_)
    out = []
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            out.append(nums1[i])
    return out

def intersection_2(nums1,nums2):
    return list(set(nums1)&set(nums2))