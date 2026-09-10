class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        left = 0
        right = len(nums1)
        half = (len(nums1) + len(nums2)) // 2
        while left <= right:
            i = left + (right - left) // 2
            j = half - i
            left1  = nums1[i-1] if i > 0 else float("-inf")
            right1 = nums1[i]   if i < len(nums1) else float("inf")
            left2  = nums2[j-1] if j > 0 else float("-inf")
            right2 = nums2[j]   if j < len(nums2) else float("inf")
            if left1 > right2:
                right = i - 1
            elif right1 < left2:
                left = i + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return  min(right1, right2)
