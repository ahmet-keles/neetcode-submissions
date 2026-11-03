class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = 0
        ptr2 = 0
        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == 0 and ptr1 >= m:
                nums1[ptr1] = nums2[ptr2]
                ptr2 += 1
            elif nums2[ptr2] <= nums1[ptr1]:
                nums2[ptr2], nums1[ptr1] = nums1[ptr1], nums2[ptr2]
                for i in range(len(nums2)-1):
                    if nums2[i] > nums2[i+1]:
                        nums2[i], nums2[i+1] = nums2[i+1], nums2[i]
            ptr1 += 1
