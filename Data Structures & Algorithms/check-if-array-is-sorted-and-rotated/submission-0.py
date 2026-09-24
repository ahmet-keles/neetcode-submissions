class Solution:
    def check(self, nums: List[int]) -> bool:
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] > nums[(i + 1) % length]:
                count += 1

        return count <= 1