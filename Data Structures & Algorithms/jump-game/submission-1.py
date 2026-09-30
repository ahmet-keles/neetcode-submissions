class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can = 0
        for i in range(len(nums)):
            if can < nums[i]:
                can = nums[i]
            if can == 0 and i != len(nums) - 1:
                return False
            can -= 1

        return True