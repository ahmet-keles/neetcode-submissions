class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        n1 = 0
        while n1 < len(nums1):
            n2 = 0
            while n2 < len(nums2):
                if nums1[n1] == nums2[n2]:
                    res.add(nums1[n1])
                n2 += 1
            n1 += 1
        return list(res)