class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            found = False
            j = 0
            while j < len(nums2):
                print(nums2[j], nums1[i])
                if nums2[j] == nums1[i] and not found:
                    found = True
                if nums2[j] > nums1[i] and found:
                    res[i] = nums2[j]
                    break
                j += 1
            print(res[i])

        return res