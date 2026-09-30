class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        
        for i in range(len(res) - 1, -1, -1):
            if (nums[l] * nums[l]) < (nums[r] * nums[r]):
                res[i] = (nums[r] * nums[r])
                r -= 1
            else:
                res[i] = (nums[l] * nums[l])
                l += 1
        return res